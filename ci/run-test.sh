#!/bin/bash
echo "Starting the shell script"
# Exit immediately if a command exits with a non-zero status.
set -e
# Enable the globstar shell option
shopt -s globstar
# Make sure we are inside the github workspace

ls -lRh
cd $HOME/Documents/myagent/_work/2/s/custom_library/test/
arduino-cli compile -b Seeeduino:samd:zero -e
arduino-cli upload -p /dev/ttyACM0 -b Seeeduino:samd:zero

sleep 5
python SerialRead.py

