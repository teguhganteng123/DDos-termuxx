#!/bin/bash
clear
echo "╔═══════════════════════════════════════╗"
echo "║    🔥 DDOS TERMUX INSTALLER           ║"
echo "║    By: RpaezzXploit                ║"
echo "║    GitHub: teguhganteng123            ║"
echo "╚═══════════════════════════════════════╝"
echo ""
echo "⚠️  WARNING: For educational use only!"
echo ""

# Check if running in Termux
if [ ! -d "/data/data/com.termux/files/home" ]; then
    echo "❌ This script must be run in Termux!"
    exit 1
fi

echo "📦 Updating packages..."
pkg update -y && pkg upgrade -y

echo "🐍 Installing Python..."
pkg install python -y

echo "📦 Installing Git..."
pkg install git -y

echo "🔧 Installing dependencies..."
pip install requests

echo "⬇️  Cloning repository..."
git clone https://github.com/teguhganteng123/DDos-termuxx

echo "📁 Moving to directory..."
cd DDos-termuxx

echo "🔒 Making scripts executable..."
chmod +x ddos.py
chmod +x install.sh

echo ""
echo "════════════════════════════════════════"
echo "✅ INSTALLATION COMPLETE!"
echo ""
echo "📝 USAGE:"
echo "1. Run Python script:"
echo "   python3 ddos.py"
echo ""
echo "2. Open web interface:"
echo "   Open index.html in browser"
echo ""
echo "3. One-line attack:"
echo "   python3 ddos.py --target http://example.com"
echo ""
echo "⚠️  LEGAL TARGETS FOR TESTING:"
echo "   http://testphp.vulnweb.com"
echo "   http://testasp.vulnweb.com"
echo "   http://zero.webappsecurity.com"
echo ""
echo "📞 Support: GitHub Issues"
echo "════════════════════════════════════════"
echo ""
echo "💡 Tip: Run 'python3 ddos.py --help' for options"
echo ""
echo "⚡ Starting tool in 5 seconds..."
sleep 5
python3 ddos.py
