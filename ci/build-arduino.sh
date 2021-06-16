#!/bin/bash
echo "Starting the shell script"
# Exit immediately if a command exits with a non-zero status.
set -e
# Enable the globstar shell option
shopt -s globstar
# Make sure we are inside the github workspace
cd $GITHUB_WORKSPACE
# Create directories
mkdir $HOME/Arduino
mkdir $HOME/Arduino/libraries
# Install Arduino IDE
export PATH="$GITHUB_WORKSPACE/bin:$PATH"
export PATH="$HOME/bin:$PATH"
curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
arduino-cli config init
echo "# arduino-cli.yaml
board_manager:
  additional_urls:
    - http://arduino.esp8266.com/stable/package_esp8266com_index.json
    - https://adafruit.github.io/arduino-board-index/package_adafruit_index.json
    - https://files.seeedstudio.com/arduino/package_seeeduino_boards_index.json" > /home/vsts/.arduino15/arduino-cli.yaml
    
cat /home/vsts/.arduino15/arduino-cli.yaml
arduino-cli core update-index

arduino-cli core search Seeeduino

# Install Arduino AVR core
arduino-cli core install arduino:avr

# Install Seeeduino samd core
arduino-cli core install Seeeduino:samd

# Link Arduino library
ln -s $GITHUB_WORKSPACE $HOME/Arduino/libraries/CI_Test_Library

arduino-cli lib search AUnit

cd $HOME/Arduino/libraries

echo "Printing pwd"
pwd
echo "list files"
ls
echo "listing files---"
ls -Rlh
# Compile all *.ino files for the Arduino Uno
#for f in **/*.ino ; do
cd $HOME/work/1/s
arduino-cli compile -b Seeeduino:samd:zero 
ls -l
#arduino_sketch_devops.ino
#done
