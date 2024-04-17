import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from dataclasses import dataclass
import time
from datetime import datetime
from uuid import UUID
import grpc
from rmcs_api_client.auth import Auth
from rmcs_api_client.resource import Resource, DeviceSchema
import config


# user login on local server
address_auth = config.SERVER_LOCAL['address_auth']
address_resource = config.SERVER_LOCAL['address_resource']
auth = Auth(address_auth)
login = auth.user_login(config.SERVER_LOCAL['admin_name'], config.SERVER_LOCAL['admin_password'])
resource = Resource(address_resource, login.access_tokens[0].access_token)

# user login on main server
address_auth = config.SERVER_MAIN['address_auth']
address_resource = config.SERVER_MAIN['address_resource']
auth_main = Auth(address_auth)
login_main = auth_main.user_login(config.SERVER_MAIN['admin_name'], config.SERVER_MAIN['admin_password'])
resource_main = Resource(address_resource, login_main.access_tokens[0].access_token)

print("LOCAL LOGIN:")
print("user_id       = {}".format(login.user_id))
print("auth_token    = {}".format(login.auth_token))
for token in login.access_tokens:
    print("api_id        = {}".format(token.api_id))
    print("access_token  = {}".format(token.access_token))
    print("refresh_token = {}".format(token.refresh_token))
print("MAIN LOGIN:")
print("user_id       = {}".format(login_main.user_id))
print("auth_token    = {}".format(login_main.auth_token))
for token in login_main.access_tokens:
    print("api_id        = {}".format(token.api_id))
    print("access_token  = {}".format(token.access_token))
    print("refresh_token = {}".format(token.refresh_token))

# read devices on a gateway
devices: list[DeviceSchema] = []
for gateway_id in config.GATEWAYS:
    device_list = resource.list_device_by_gateway(UUID(gateway_id))
    for index, device in enumerate(device_list):
        if device.id == device.gateway_id:
            device_list.pop(index)
    devices = devices + device_list

print("DEVICES:")
device_map = {}
for device in devices:
    print("{}: {}".format(device.id, device.name))
    device_map[device.id] = device.name

while True:

    buffers = []
    try:
        buffers = resource.list_buffer_first(100, None, None, "TRANSFER_SERVER")
    except grpc.RpcError as error:
        if error.code() == grpc.StatusCode.UNAUTHENTICATED:
            login = auth.user_login(config.SERVER_LOCAL['admin_name'], config.SERVER_LOCAL['admin_password'])
            resource = Resource(address_resource, login.access_tokens[0].access_token)
            print("RELOGIN LOCAL")
        continue

    for buffer in buffers:

        # check if a buffer has associated device
        try:
            time_str = buffer.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            if buffer.device_id not in device_map:
                resource.delete_buffer(buffer.id)
                continue
            print("{}    {}    {}".format(time_str, buffer.device_id, device_map[buffer.device_id]))
        except grpc.RpcError as error:
            print(error)

        # try to create buffer on main server database
        main_exist = True
        try:
            resource_main.create_buffer(buffer.device_id, buffer.model_id, buffer.timestamp, buffer.data, "TRANSFER_LOCAL")
        except grpc.RpcError as error:
            if error.code() == grpc.StatusCode.UNAUTHENTICATED:
                login_main = auth_main.user_login(config.SERVER_MAIN['admin_name'], config.SERVER_MAIN['admin_password'])
                resource_main = Resource(address_resource, login_main.access_tokens[0].access_token)
                print("RELOGIN MAIN")
                break
            elif error.code() == grpc.StatusCode.UNAVAILABLE:
                print("UNAVAILABLE")
                break
            else:
                print(error)
                # check if buffer already exist
                try:
                    resource_main.read_buffer_by_time(buffer.device_id, buffer.model_id, buffer.timestamp)
                except grpc.RpcError as error:
                    main_exist = False
                    print(error)

        # delete buffer only if buffer on main exists
        if main_exist:
            try:
                resource.delete_buffer(buffer.id)
            except grpc.RpcError as error:
                print(error)

    time.sleep(config.TIMING['transfer_sleep'])
