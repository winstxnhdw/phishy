PORT=5000

if [ ! -z "$1" ]
then
  PORT=$1
fi

$TERM -e python server.py $PORT &
$TERM -e ngrok http $PORT &
