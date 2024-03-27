#!/bin/bash

sleep 15

while :
do

	analysis_rhd=$(pgrep -a python | grep -c /opt/rmcs-gateway/analysis/analysis_running_hour_data.py)
	if [ $analysis_rhd -eq 0 ]
	then

		printf "rerun running hour data analysis script...\n"
		/opt/rmcs-gateway/.venv/bin/python /opt/rmcs-gateway/analysis/analysis_running_hour_data.py &

	fi

	analysis_twpa=$(pgrep -a python | grep -c /opt/rmcs-gateway/analysis/timing_working_parameter_analysis.py)
	if [ $analysis_twpa -eq 0 ]
	then

		printf "rerun timing working parameter analysis script...\n"
		/opt/rmcs-gateway/.venv/bin/python /opt/rmcs-gateway/analysis/timing_working_parameter_analysis.py &

	fi

	analysis_rhs=$(pgrep -a python | grep -c /opt/rmcs-gateway/analysis/analysis_running_hour_sensor.py)
	if [ $analysis_rhs -eq 0 ]
	then

		printf "rerun running hour sensor analysis script...\n"
		/opt/rmcs-gateway/.venv/bin/python /opt/rmcs-gateway/analysis/analysis_running_hour_sensor.py &

	fi

	sleep 5

done
