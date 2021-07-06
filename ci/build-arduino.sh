#!/bin/bash
echo "Starting the shell script"
# Exit immediately if a command exits with a non-zero status.
set -e
# Enable the globstar shell option
shopt -s globstar
# Make sure we are inside the github workspace
cd ../
arduino-cli compile -b Seeeduino:samd:zero -e
cd build/Seeeduino.samd.zero/
python ../ci/sign.py private.pem * 1
