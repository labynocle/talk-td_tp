#!/bin/bash

RUNIDE_SCRIPT='/home/erwan/Desktop/sikuli/runIDE'
SIKULI_TEST_DIRECTORY='/home/erwan/Dropbox/Work/Deezer/Sikuli_light_Talk/Test1.sikuli/'
CHROMIUM_BIN='/usr/bin/chromium-browser'

SCRIPT_NAME=`basename $0`

echo "$SCRIPT_NAME - `date` - start a Sikuli test..."

$CHROMIUM_BIN > /dev/null 2>&1 &

$RUNIDE_SCRIPT -r $SIKULI_TEST_DIRECTORY

if [ $? -ne 0 ]
then
	echo -e "$SCRIPT_NAME - `date` - \e[31mJob done - NOK\e[0m"
else	
	echo -e "$SCRIPT_NAME - `date` - \e[32mJob done - OK\e[0m"
fi
