echo Mac OS X build script invoked
python -m PyInstaller --noconsole sandbox/__main__.py --name sandbox
sleep 1
hdiutil create dist/sandbox.dmg -srcfolder dist/sandbox.app -ov
echo Remove sandbox directory
rm -rfv dist/sandbox
echo Remove sandbox.app directory
rm -rfv dist/sandbox.app
echo "dist content:"
ls dist
tree
# export OSX_FILE="dist/sandbox.dmg"
