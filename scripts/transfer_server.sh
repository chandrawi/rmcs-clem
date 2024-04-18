#!/bin/bash

sleep 15

while :
do

	transfer_local=$(pgrep -a python | grep -c /home/gundala/rmcs-server/transfer/transfer_local.py)
	if [ $transfer_local -eq 0 ]
	then

		printf "rerun transfer local script...\n"
		/home/gundala/rmcs-server/.venv/bin/python /home/gundala/rmcs-server/transfer/transfer_local.py &

	fi

	transfer_ext_db=$(pgrep -a python | grep -c /home/gundala/rmcs-server/transfer/transfer_external_db.py)
	if [ $transfer_ext_db -eq 0 ]
	then

		printf "rerun transfer external database script...\n"
		/home/gundala/rmcs-server/.venv/bin/python /home/gundala/rmcs-server/transfer/transfer_external_db.py &

	fi

	transfer_ext_api=$(pgrep -a python | grep -c /home/gundala/rmcs-server/transfer/transfer_external_api.py)
	if [ $transfer_ext_api -eq 0 ]
	then

		printf "rerun transfer external api script...\n"
		/home/gundala/rmcs-server/.venv/bin/python /home/gundala/rmcs-server/transfer/transfer_external_api.py &

	fi

	sleep 5

done
