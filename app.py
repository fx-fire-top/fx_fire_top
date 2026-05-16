from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

# আপনার অফিশিয়াল সোশ্যাল লিংক
TG_LINK_1 = "https://t.me/GhostX_Official_Group"
WA_LINK = "https://whatsapp.com/channel/0029Vb8RBGlEquiSBj3XwB0P"

# আপনার ডাউনলোডের বাটন ও লিংকসমূহ
DOWNLOAD_BUTTONS = [
    {"title": "DOWNLOAD GUILD GLORY BOT", "url": "https://getmocha.com/apps/019c947b-02c6-7781-878a-f92e35070169"},
    {"title": "DOWNLOAD MTH TEAM MOD MENU", "url": "https://www.mediafire.com/file/qbyvwrlleoe0b48/MTH+TEAM+V51+AP.zip/file"},
    {"title": "DOWNLOAD GOD X MOD", "url": "https://www.mediafire.com/file/pb5tzrpoqgec4g2"},
    {"title": "DOWNLOAD SIGMA GAME", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD ITALY MACRO", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD GLITCH FILE VIP", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD VVIP INJECTOR", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD FREE FIRE MAX MOD", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD PANEL PRO MAX", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD AIMBOT CONFIG", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD AUTO HEADSHOT FILE", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD VIP RECOIL FIX", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD ESP HACK TOOL", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD ANTIBAN BYPASS", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD GHOST MOD MENU", "url": "https://www.mediafire.com"},
    {"title": "DOWNLOAD DIAMOND HACK SIM", "url": "https://www.mediafire.com"}
]

HOME_HTML = '''
<!DOCTYPE HTML>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FX START</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body{background:#000;color:#fff;font-family:sans-serif;text-align:center;padding:15px;}
        .box{max-width:450px;margin:20px auto;border:3px solid #ff0055;border-radius:15px;padding:20px;background:#050505;box-shadow:0 0 15px #ff0055;}
        .logo{font-size:32px;font-weight:900;color:#ffcc00;text-shadow:0 0 10px #ffcc00;}
        .profile{border:2px solid #ffcc00;padding:10px;border-radius:50px;display:inline-block;margin:15px;font-weight:bold;color:#ffcc00;}
        .btn{display:block;padding:12px;margin:10px 0;border-radius:8px;text-decoration:none;font-weight:bold;color:#fff;text-transform:uppercase;font-size:13px;}
        .tg1{background:linear-gradient(45deg, #0088cc, #00aacc);}
        .wa{background:linear-gradient(45deg, #25D366, #075E54);}
        .dl{background:linear-gradient(45deg, #ffcc00, #ffaa00);color:#000;margin-bottom:12px;}
    </style>
</head>
<body>
    <div class="box">
        <div class="logo">FX START</div>
        <div class="profile">★ MD SUYAIF ★</div>
        <a class="btn tg1" href="{{tg1}}" target="_blank"><i class="fab fa-telegram-plane"></i> JOIN TELEGRAM</a>
        <a class="btn wa" href="{{wa}}" target="_blank"><i class="fab fa-whatsapp"></i> WHATSAPP CHANNEL</a>
        
        <div style="margin-top:20px;">
            {{buttons_html | safe}}
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    btn_html = ""
    for b in DOWNLOAD_BUTTONS:
        btn_html += f'<a class="btn dl" href="{b["url"]}" target="_blank">📥 {b["title"]}</a>\n'
    return render_template_string(HOME_HTML, tg1=TG_LINK_1, wa=WA_LINK, buttons_html=btn_html)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 9797))
    app.run(host='0.0.0.0', port=port)
