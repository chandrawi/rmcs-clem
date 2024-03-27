import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from typing import Union
from dataclasses import dataclass
import uuid
from uuid import UUID
import uuid
from rmcs_api_client.auth import Auth
from rmcs_api_client.resource import Resource, DataType
import config


@dataclass
class ModelConfig:
    name: str
    value: Union[int, float, str, None]
    category: str

@dataclass
class Model:
    category: str
    name: str
    description: str
    types: list[DataType]
    configs: list[list[ModelConfig]]

@dataclass
class Type:
    name: str
    description: str
    models: list[str]

@dataclass
class DeviceConfig:
    name: str
    value: Union[int, float, str]
    category: str

@dataclass
class Device:
    serial_number: str
    name: str
    description: str
    type: str
    configs: list[DeviceConfig]

@dataclass
class Group:
    category: str
    name: str
    description: str
    members: list[str]


MODELS = {
    "testing_6b": Model(
        "RAW", 
        "6 bytes testing", 
        "6 bytes testing raw data", 
        [DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8],
        []
    ),
    "time_counter": Model(
        "DATA", 
        "timestamp and counter", 
        "timestamp and counter", 
        [DataType.U32, DataType.U16],
        []
    ),
    "running_hour_raw": Model(
        "RAW", 
        "running hour raw data", 
        "14 bytes binary data", 
        [DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8, DataType.U8],
        []
    ),
    "running_hour_data": Model(
        "DATA",
        "running hour sensor data",
        "Active and reactive energy, frequency, peak current and voltage floating point data and working status",
        [DataType.F64, DataType.F64, DataType.F32, DataType.F64, DataType.F64, DataType.U8],
        [
            [
                ModelConfig("scale", "active energy", "SCALE"),
                ModelConfig("unit", "watt", "UNIT"),
                ModelConfig("symbol", "W", "SYMBOL")
            ],
            [
                ModelConfig("scale", "reactive energy", "SCALE"),
                ModelConfig("unit", "volt-ampere", "UNIT"),
                ModelConfig("symbol", "VA", "SYMBOL")
            ],
            [
                ModelConfig("scale", "frequency", "SCALE"),
                ModelConfig("unit", "hertz", "UNIT"),
                ModelConfig("symbol", "hz", "SYMBOL")
            ],
            [
                ModelConfig("scale", "peak current", "SCALE"),
                ModelConfig("unit", "ampere", "UNIT"),
                ModelConfig("symbol", "A", "SYMBOL")
            ],
            [
                ModelConfig("scale", "peak voltage", "SCALE"),
                ModelConfig("unit", "voltage", "UNIT"),
                ModelConfig("symbol", "V", "SYMBOL")
            ],
            [
                ModelConfig("name", "working status", "NAME"),
                ModelConfig("BREAKDOWN", 0, "ENUMERATION"),
                ModelConfig("STANDBY", 1, "ENUMERATION"),
                ModelConfig("RUNNING", 2, "ENUMERATION")
            ]
        ]
    ),
    "running_hour_sensor": Model(
        "ANALYSIS",
        "running hour sensor",
        "Running time period of an equipment obtained from the sensor automatically",
        [DataType.U32],
        [
            [
                ModelConfig("scale", "running period", "SCALE"),
                ModelConfig("unit", "second", "UNIT"),
                ModelConfig("symbol", "s", "SYMBOL")
            ]
        ]
    ),
    "running_hour_user": Model(
        "EXTERNAL",
        "running hour user",
        "Time period with working status of an equipment obtained from the user",
        [DataType.U32, DataType.U8],
        [
            [
                ModelConfig("scale", "working period", "SCALE"),
                ModelConfig("unit", "second", "UNIT"),
                ModelConfig("symbol", "s", "SYMBOL")
            ],
            [
                ModelConfig("name", "working status", "NAME"),
                ModelConfig("BREAKDOWN", 0, "ENUMERATION"),
                ModelConfig("STANDBY", 1, "ENUMERATION"),
                ModelConfig("RUNNING", 2, "ENUMERATION")
            ]
        ]
    ),
    "working_parameter_shift": Model(
        "ANALYSIS",
        "working parameter shift",
        "Working parameter of equipment calculated from running hour sensor and user for every working shift",
        [DataType.U8, DataType.U8, DataType.F64],
        [
            [
                ModelConfig("name", "shift", "NAME")
            ],
            [
                ModelConfig("name", "working parameter", "NAME"),
                ModelConfig("PA", 0, "ENUMERATION"),
                ModelConfig("UA", 1, "ENUMERATION"),
                ModelConfig("MA", 2, "ENUMERATION"),
                ModelConfig("EU", 3, "ENUMERATION")
            ],
            [
                ModelConfig("scale", "working data", "SCALE"),
                ModelConfig("unit", "percent", "UNIT"),
                ModelConfig("symbol", "%", "SYMBOL")
            ]
        ]
    ),
    "working_parameter_period": Model(
        "ANALYSIS",
        "working parameter period",
        "Working parameter of equipment calculated from averaging working parameter shift at a period (week, month, quarter, year)",
        [DataType.U8, DataType.U8, DataType.F64],
        [
            [
                ModelConfig("name", "period", "NAME"),
                ModelConfig("WEEKLY", 0, "ENUMERATION"),
                ModelConfig("MONTHLY", 1, "ENUMERATION"),
                ModelConfig("QUARTER", 2, "ENUMERATION"),
                ModelConfig("ANNUAL", 3, "ENUMERATION")
            ],
            [
                ModelConfig("name", "working parameter", "NAME"),
                ModelConfig("PA", 0, "ENUMERATION"),
                ModelConfig("UA", 1, "ENUMERATION"),
                ModelConfig("MA", 2, "ENUMERATION"),
                ModelConfig("EU", 3, "ENUMERATION")
            ],
            [
                ModelConfig("scale", "working data", "SCALE"),
                ModelConfig("unit", "percent", "UNIT"),
                ModelConfig("symbol", "%", "SYMBOL")
            ]
        ]
    ),
    "working_parameter_command": Model(
        "COMMAND",
        "working parameter command",
        "Command message for starting running hour and working parameter analysis, contain analysis type and period",
        [DataType.U32],
        [
            [
                ModelConfig("scale", "analysis period", "SCALE"),
                ModelConfig("unit", "second", "UNIT"),
                ModelConfig("symbol", "s", "SYMBOL")
            ]
        ]
    )
}

TYPES = {
    "gateway": Type(
        "gateway blank",
        "gateway with no model",
        []
    ),
    "time_counter": Type(
        "timestamp and counter",
        "testing device with timestamp and counter data",
        ["testing_6b", "time_counter"]
    ),
    "running_hour": Type(
        "running hour sensor",
        "electric energy meter used for running hour sensor and working parameter analysis",
        ["running_hour_raw", "running_hour_data", "running_hour_sensor", "running_hour_user", "working_parameter_shift", "working_parameter_period"]
    )
}

GATEWAY = Device(
    "GATE01",
    "Gateway_1",
    "",
    "gateway",
    []
)

DEVICES = [
    Device(
        "TESTLOR01",
        "LoRa device testing",
        "LoRa device testing with timestamp and counter data",
        "time_counter",
        [
            DeviceConfig("gateway_id", 0x00, "COMMUNICATION"),
            DeviceConfig("node_id", 0x01, "COMMUNICATION"),
            DeviceConfig("data_length", 6, "COMMUNICATION"),
            DeviceConfig("period_time", 10, "COMMUNICATION"),
            DeviceConfig("offset_time", 2, "COMMUNICATION")
        ]
    ),
    Device(
        "TESTLOR02",
        "LoRa device testing",
        "LoRa device testing with timestamp and counter data",
        "time_counter",
        [
            DeviceConfig("gateway_id", 0x00, "COMMUNICATION"),
            DeviceConfig("node_id", 0x02, "COMMUNICATION"),
            DeviceConfig("data_length", 6, "COMMUNICATION"),
            DeviceConfig("period_time", 10, "COMMUNICATION"),
            DeviceConfig("offset_time", 4, "COMMUNICATION")
        ]
    ),
    Device(
        "TESTRHS01",
        "Running hour sensor 1",
        "Running hour sensor 1 for testing",
        "running_hour",
        [
            DeviceConfig("gateway_id", 0x01, "COMMUNICATION"),
            DeviceConfig("node_id", 0x01, "COMMUNICATION"),
            DeviceConfig("data_length", 14, "COMMUNICATION"),
            DeviceConfig("period_time", 60, "COMMUNICATION"),
            DeviceConfig("offset_time", 5, "COMMUNICATION"),
            DeviceConfig("aenergy_offset", 62, "ANALYSIS"),
            DeviceConfig("vaenergy_offset", 1116, "ANALYSIS"),
            DeviceConfig("aenergy_coefficient", 1.0, "ANALYSIS"),
            DeviceConfig("vaenergy_coefficient", 1.0, "ANALYSIS"),
            DeviceConfig("ipeak_coefficient", 1.0, "ANALYSIS"),
            DeviceConfig("vpeak_coefficient", 1.0, "ANALYSIS"),
            DeviceConfig("clk_freq", 3579545, "ANALYSIS"),
            DeviceConfig("standby_ths", 6000, "ANALYSIS"),
            DeviceConfig("running_ths", 36000, "ANALYSIS")
        ]
    ),
    Device(
        "TESTRHS02",
        "Running hour sensor 2",
        "Running hour sensor 2 for testing",
        "running_hour",
        [
            DeviceConfig("gateway_id", 0x01, "COMMUNICATION"),
            DeviceConfig("node_id", 0x02, "COMMUNICATION"),
            DeviceConfig("data_length", 14, "COMMUNICATION"),
            DeviceConfig("period_time", 60, "COMMUNICATION"),
            DeviceConfig("offset_time", 10, "COMMUNICATION"),
            DeviceConfig("aenergy_offset", 62, "ANALYSIS"),
            DeviceConfig("vaenergy_offset", 1116, "ANALYSIS"),
            DeviceConfig("aenergy_coefficient", 1.0, "ANALYSIS"),
            DeviceConfig("vaenergy_coefficient", 1.0, "ANALYSIS"),
            DeviceConfig("ipeak_coefficient", 1.0, "ANALYSIS"),
            DeviceConfig("vpeak_coefficient", 1.0, "ANALYSIS"),
            DeviceConfig("clk_freq", 3579545, "ANALYSIS"),
            DeviceConfig("standby_ths", 6000, "ANALYSIS"),
            DeviceConfig("running_ths", 36000, "ANALYSIS")
        ]
    )
]

GROUPS = [
]


# admin login
address_auth = config.SERVER_LOCAL['address_auth']
address_resource = config.SERVER_LOCAL['address_resource']
auth = Auth(address_auth)
login = auth.user_login(config.SERVER_LOCAL['admin_name'], config.SERVER_LOCAL['admin_password'])
resource = Resource(address_resource, login.access_tokens[0].access_token)

# create data model and add data types and configs
model_map = {}
for key, model in MODELS.items():
    model_id = resource.create_model(uuid.uuid4(), model.category, model.name, model.description)
    resource.add_model_type(model_id, model.types)
    for index, configs in enumerate(model.configs):
        for conf in configs:
            resource.create_model_config(model_id, index, conf.name, conf.value, conf.category)
    model_map[key] = model_id

# create type
type_map = {}
for key, type_ in TYPES.items():
    type_id = resource.create_type(uuid.uuid4(), type_.name, type_.description)
    for model_key in type_.models:
        model_id = model_map[model_key]
        resource.add_type_model(type_id, model_id)
    type_map[key] = type_id

# create gateway
gateway_map = {}
gateway_id = UUID(config.GATEWAY_LORA['id'])
# gateway_id = uuid.uuid4()
type_id = type_map[GATEWAY.type]
resource.create_gateway(gateway_id, type_id, GATEWAY.serial_number, GATEWAY.name, GATEWAY.description)
for conf in GATEWAY.configs:
    resource.create_gateway_config(gateway_id, conf.name, conf.value, conf.category)
gateway_map[GATEWAY.serial_number] = gateway_id

# create devices
device_map = {}
for device in DEVICES:
    device_id = uuid.uuid4()
    type_id = type_map[device.type]
    resource.create_device(device_id, gateway_id, type_id, device.serial_number, device.name, device.description)
    for conf in device.configs:
        resource.create_device_config(device_id, conf.name, conf.value, conf.category)
    device_map[device.serial_number] = device_id

# create groups
group_map = {}
for group in GROUPS:
    group_id = uuid.uuid4()
    resource.create_group_device(group_id, group.name, group.category, group.description)
    for member in group.members:
        if member in device_map:
            resource.add_group_device_member(group_id, device_map[member])
    group_map[group.name] = group_id

print("LOGIN:")
print("user_id       = {}".format(login.user_id))
print("auth_token    = {}".format(login.auth_token))
for token in login.access_tokens:
    print("api_id        = {}".format(token.api_id))
    print("access_token  = {}".format(token.access_token))
    print("refresh_token = {}".format(token.refresh_token))
print("MODELS:")
for name in model_map:
    print("{}: {}".format(model_map[name], name))
print("TYPES:")
for name in type_map:
    print("{}: {}".format(type_map[name], name))
print("GATEWAY:")
for name in gateway_map:
    print("{}: {}".format(gateway_map[name], name))
print("DEVICES:")
for name in device_map:
    print("{}: {}".format(device_map[name], name))
print("GROUP:")
for name in group_map:
    print("{}: {}".format(group_map[name], name))
