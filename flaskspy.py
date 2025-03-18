# Gets geolocation (City, Country, ISP, Latitude & Longitude) and many more infoooooooo
# Extracts User-Agent & Referer from requests
# Saves logs in connections.log for tracking 
# Multi-threaded (handles multiple clients at once)
# Sends a response to the client
# also show server info

from flask import Flask, request, jsonify, render_template_string
import requests
import platform
import psutil
import json

app = Flask(__name__)

# HTML Template to collect client-side data
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <script>
        async function getClientInfo() {
            let screenRes = screen.width + "x" + screen.height;
            let timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
            let language = navigator.language;
            let plugins = [...navigator.plugins].map(p => p.name).join(", ");
            let cpuCores = navigator.hardwareConcurrency;
            let memory = navigator.deviceMemory || "Unknown";
            let battery = "Unknown";
            
            if (navigator.getBattery) {
                let batteryObj = await navigator.getBattery();
                battery = (batteryObj.level * 100) + "%";
            }
            
            fetch("/log", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    screenRes, timezone, language, plugins, cpuCores, memory, battery
                })
            });
        }
        window.onload = getClientInfo;
    </script>
</head>
<body>
    <h1>Loading...</h1>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/log', methods=['POST'])
def log_data():
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')
    referer = request.headers.get('Referer', 'None')
    
    data = request.get_json()
    
    # Get GeoIP Data
    geo_data = requests.get(f"http://ip-api.com/json/{client_ip}").json()
    city = geo_data.get("city", "Unknown")
    region = geo_data.get("regionName", "Unknown")
    country = geo_data.get("country", "Unknown")
    isp = geo_data.get("isp", "Unknown")
    vpn = "Yes" if geo_data.get("proxy", False) else "No"
    
    # Get Server System Info
    server_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "CPU Cores": psutil.cpu_count(logical=True),
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Total RAM (GB)": round(psutil.virtual_memory().total / (1024**3), 2),
        "Available RAM (GB)": round(psutil.virtual_memory().available / (1024**3), 2),
        "Uptime (Seconds)": round(psutil.boot_time())
    }

    log_entry = {
        "IP Address": client_ip,
        "User-Agent": user_agent,
        "Referer": referer,
        "Screen Resolution": data.get("screenRes", "Unknown"),
        "Timezone": data.get("timezone", "Unknown"),
        "Language": data.get("language", "Unknown"),
        "Browser Plugins": data.get("plugins", "Unknown"),
        "CPU Cores": data.get("cpuCores", "Unknown"),
        "RAM (GB)": data.get("memory", "Unknown"),
        "Battery Level": data.get("battery", "Unknown"),
        "ISP": isp,
        "City": city,
        "Region": region,
        "Country": country,
        "VPN/Proxy": vpn,
        "Server Info": server_info
    }
    
    print(json.dumps(log_entry, indent=4))
    
    with open("client_logs.txt", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    
    return jsonify({"status": "logged"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)