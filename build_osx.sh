echo "Hello world sh file"
pipenv run pyinstaller --noconsole sandbox/__main__.py --name sandbox
sleep 1
hdiutil create dist/sandbox.dmg -srcfolder dist/sandbox.app -ov
echo Remove sandbox directory
rm -rfv dist/sandbox
echo Remove sandbox.app directory
rm -rfv dist/sandbox.app
echo "dist content:"
ls dist
tree
