#!/bin/bash
echo "Starting the shell script"
# Exit immediately if a command exits with a non-zero status.
set -e
# Enable the globstar shell option
shopt -s globstar
# Make sure we are inside the github workspace
cd $GITHUB_WORKSPACE
echo "Printing pwd"
pwd
echo "list files"
ls
echo "listing files---"
ls -Rlh
# Compile all *.ino files for the Arduino Uno
#for f in **/*.ino ; do
cd /home/ubuntu/Documents/myagent/_work/1/s/arduino_sketch_devops
arduino-cli compile -b Seeeduino:samd:zero -e
ls -l
#arduino_sketch_devops.ino
#done
