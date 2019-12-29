echo Windows build script invoked
pyinstaller --onefile --noconsole sandbox\__main__.py --name sandbox
sleep 1
dist/sandbox.exe
