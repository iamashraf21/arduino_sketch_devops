#!/bin/bash
echo "Starting the shell script"
# Exit immediately if a command exits with a non-zero status.
set -e
# Enable the globstar shell option
shopt -s globstar
# Make sure we are inside the github workspace

cd ../
OUTPUT=$(find . -type d -name "test")
if [ ${OUTPUT} = './test' ]
	then arduino-cli compile -b Moteino:samd:moteino_m0
fi
cd firmware
arduino-cli compile -b Moteino:samd:moteino_m0 -e
