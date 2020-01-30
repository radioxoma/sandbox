echo Windows build script invoked
pyinstaller --onefile --noconsole sandbox/__main__.py --name sandbox
sleep 1
dist/sandbox.exe
rem SET WINDOWS_FILE="dist/sandbox.exe"
