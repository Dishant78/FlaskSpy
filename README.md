# 🔍 FlaskSpy - Client & Server Information Logger  

## 📌 Overview  
**FlaskSpy** is a lightweight Flask-based server that logs detailed client and system information upon connection. It captures geolocation, ISP details, browser info, system specs, and more while saving the data in a log file (`client_logs.txt`).  

The repo also includes a **basic TCP server** (`demo_server.py`) to demonstrate a simple socket-based connection.  

---

## 📁 Files in this Repository  

- **`demo_server.py`** → A simple Python socket server that listens on port `9999`.  
- **`flaskspy.py`** → The advanced version using **Flask**, logs detailed client info, and saves it to `client_logs.txt`.  
- **`requirements.txt`** → Lists all dependencies needed to run the final version (`flaskspy.py`).  

---

## 🚀 Setup Guide  

### 1️⃣ Clone the Repository  

git clone https://github.com/your-username/FlaskSpy.git
cd FlaskSpy
### 2️⃣ Install Dependencies

pip install -r requirements.txt
### 3️⃣ Run the Basic Server (demo_server.py)

python demo_server.py
It listens on PORT 9999.
Accepts incoming connections and responds with a simple "Server is working!" message.
### 4️⃣ Run the Flask Spy Server (flaskspy.py)

python flaskspy.py
Runs a Flask server on PORT 9999.
Logs incoming connections and extracts detailed info.
Stores client info in client_logs.txt.
🌍 How to Access
Once the server is running, open a browser and visit:
http://localhost:9999
Whenever a client connects, their IP, geolocation, browser details, and system info are logged in client_logs.txt.

📜 Log File - client_logs.txt
Each connection generates a log entry in client_logs.txt with details like:
✅ IP Address, Geolocation (City, Country)
✅ ISP & VPN Detection
✅ User-Agent & Browser Plugins
✅ Screen Resolution, Language, Timezone
✅ CPU, RAM, Battery Level
✅ Server System Information

🛠 Features
✅ Basic TCP Server (demo_server.py)
✅ Advanced Flask Logger (flaskspy.py)
✅ Real-time Geolocation & ISP Lookup
✅ Logs User-Agent, Referer, Browser Data
✅ Extracts System Info (CPU, RAM, Battery, etc.)
✅ Saves Logs to client_logs.txt for Tracking
✅ Multi-Threaded for Handling Multiple Clients

Future Enhancements will be made