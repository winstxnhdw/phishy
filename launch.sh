PORT=$1

python server.py $PORT
ngrok http $PORT
