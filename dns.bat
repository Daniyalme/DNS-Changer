@echo off
:: Check for administrative privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :main
) else (
    echo Requesting administrative privileges...
    :: Restart script with administrative privileges
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:main
:: Run the Python script
:: Add the directory into the environment variables 
python {PLACE YOUR DIRECTORY HERE} %*
pause
