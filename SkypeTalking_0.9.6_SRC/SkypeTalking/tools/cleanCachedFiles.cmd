@echo off
echo Removing cashed files...
del /s /q .\*.pyc
del /s /q ..\src\*.pyc
echo Done!