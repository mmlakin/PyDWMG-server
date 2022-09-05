#!/usr/bin/env sh
if [[ ! -r server_token ]];then
    echo "Save server token to file server_token to enable testing."
    exit
fi
export LOG_LEVEL="INFO"
echo "Testing pydwmg-server locally..."
python3 -c 'e={"queryStringParameters":{"token":"'$(cat server_token)'","update":{"test_user":"test_update"}}};import pydwmg_server; pydwmg_server.lambda_handler(e,"")'
