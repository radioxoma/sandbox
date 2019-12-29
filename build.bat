echo Hello world bat file
pyinstaller --onefile --noconsole sandbox\__main__.py --name sandbox
sleep 1
dist/sandbox.exe
