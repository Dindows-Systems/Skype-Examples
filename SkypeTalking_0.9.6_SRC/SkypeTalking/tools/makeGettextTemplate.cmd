@echo off
echo Generating application translation strings...
cd ../src
..\Tools\pygettext.py -d ../Tools/SkypeTalking *.pyw *.py *\*.py *\*\*.py *\*\*\*.py *\*\*\*\*.py
echo Done!