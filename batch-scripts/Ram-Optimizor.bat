@echo off
REM Disable automatic page file management using WMIC
wmic computersystem where name="%computername%" set AutomaticManagedPagefile=False

REM Optional: Pause to keep the window open and check output
echo Finished Ram Opimization
pause