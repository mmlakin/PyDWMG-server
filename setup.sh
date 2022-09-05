#!/usr/bin/env sh

mkdir package
cp pydwmg_server.py package
#pip3 install -r requirements.txt -t ./package
cd package
zip -r ../pydwmg-pkg.zip ./*
cd ..
rm -rf package

aws lambda update-function-code --function-name pydwmg_server --zip-file fileb://pydwmg-pkg.zip
if [[ $? -ne 0 ]]; then
    echo "Error updating labmda function code, try again."
else
    echo "Upload successful"
fi

rm -rf pydwmg-pkg.zip
