#!/bin/bash

# Kill previous processes
echo "🔁 Cleaning up..."
pkill -f mjpeg-streamer 2>/dev/null && echo "Stopped previous mjpeg-streamer."
pkill -f ngrok 2>/dev/null && echo "Stopped previous ngrok."

# Start MJPEG streamer
echo "📷 Starting MJPEG streamer..."
mjpeg-streamer -s 0 --quality 50 --fps 30 --port 8080 &
STREAMER_PID=$!
sleep 3

# Start ngrok
echo "🌐 Starting ngrok..."
ngrok http 8080 > /dev/null &
NGROK_PID=$!

# Wait for ngrok to be ready
echo "⏳ Waiting for ngrok tunnel..."
for i in {1..10}; do
  PUBLIC_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | python3 -c "
import sys, json
try:
    data = json.load(sys.stdin)
    for t in data.get('tunnels', []):
        if t['proto'] == 'https':
            print(t['public_url'])
            break
except:
    pass
")
  if [[ -n "$PUBLIC_URL" ]]; then
    echo "✅ Ngrok tunnel: $PUBLIC_URL/source_0"
    echo "$PUBLIC_URL/source_0" > ~/Desktop/webcam_url.txt
    break
  fi
  sleep 1
done

# Fail if tunnel didn't come up
if [[ -z "$PUBLIC_URL" ]]; then
  echo "❌ Failed to get ngrok URL. Exiting."
  kill $STREAMER_PID $NGROK_PID 2>/dev/null
  exit 1
fi

# Wait until user presses ENTER
read -p "🔴 Press ENTER to stop streaming..."

# Cleanup
echo "🧹 Stopping streamer and ngrok..."
kill $STREAMER_PID $NGROK_PID

