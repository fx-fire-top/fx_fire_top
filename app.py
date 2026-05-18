from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# তোর অফিশিয়াল সোশ্যাল লিংকসমূহ
TG_LINK = "https://t.me/GhostX_Official_Group"
WA_LINK = "https://whatsapp.com/channel/0029Vb8RBGleEquisBj3Xw0P"

# তোর অরিজিনাল ২০টি বাটন ও লিংক (সব আগের মতো অক্ষত আছে)
DOWNLOAD_BUTTONS = [
    {"title": "DOWNLOAD GUILD GLORY BOT", "url": "https://shrinkme.click/P6sAI8p"},
    {"title": "DOWNLOAD MTH TEAM MOD MENU", "url": "https://shrinkme.click/b6WLB"},
    {"title": "DOWNLOAD GOD X MOD", "url": "https://shrinkme.click/aPR7Z"},
    {"title": "DOWNLOAD MODIFY FREESTYLE MACROID", "url": "https://shrinkme.click/2N68at"},
    {"title": "DOWNLOAD GIFT SEND PROXY SERVER", "url": "https://shrinkme.click/XJwJU"},
    {"title": "DOWNLOAD GHOST PROXY SERVER", "url": "https://shrinkme.click/SrxqXW"},
    {"title": "DOWNLOAD SIGMA GAME", "url": "https://shrinkme.click/2N68at"},
    {"title": "DOWNLOAD ITACHI MACRO", "url": "https://shrinkme.click/jVMqIIZq"},
    {"title": "DOWNLOAD GLITCH FILE VIP", "url": "https://shrinkme.click/9uw8mgAq"},
    {"title": "DOWNLOAD VVIP INJECTOR", "url": "https://shrinkme.click/0okZ"},
    {"title": "DOWNLOAD FREE FIRE MAX MOD", "url": "https://shrinkme.click/Y46h"},
    {"title": "DOWNLOAD PANEL PRO MAX", "url": "https://shrinkme.click/SkJ7C"},
    {"title": "DOWNLOAD AIMBOT CONFIG", "url": "https://shrinkme.click/ArKl"},
    {"title": "DOWNLOAD AUTO HEADSHOT FILE", "url": "https://shrinkme.click/BSbBa"},
    {"title": "DOWNLOAD VIP RECOIL FIX", "url": "https://shrinkme.click/VNTOih"},
    {"title": "DOWNLOAD ESP HACK TOOL", "url": "https://shrinkme.click/7qZM"},
    {"title": "DOWNLOAD ANTIBAN BYPASS", "url": "https://shrinkme.click/ptF0Y"},
    {"title": "DOWNLOAD GHOST MOD MENU", "url": "https://shrinkme.click/Y46h"},
    {"title": "DOWNLOAD DIAMOND HACK SIM", "url": "https://shrinkme.click/P6sAI8p"},
    {"title": "DOWNLOAD RECOIL ASSISTANT", "url": "https://shrinkme.click/b6WLB"}
]

MAIN_PAGE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FX FIRE TOP - VIP Portal</title>
    <style>
        body { 
            background-color: #000; 
            color: #fff; 
            font-family: Arial, sans-serif; 
            padding: 15px;
            margin: 0;
            display: flex;
            justify-content: center;
        }

        /* তোর অরিজিনাল রেড নিয়ন বর্ডার প্যানেল */
        .main-container {
            width: 100%;
            max-width: 450px;
            border: 3px solid #ff0055;
            border-radius: 15px;
            padding: 20px 15px;
            box-shadow: 0 0 15px #ff0055, inset 0 0 10px #ff0055;
            text-align: center;
            box-sizing: border-box;
        }

        /* ওপরে তোর নাম গ্লোয়িং স্টাইলে */
        .admin-badge {
            display: inline-block;
            border: 2px solid #ffcc00;
            color: #ffcc00;
            padding: 5px 20px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 15px;
            margin-bottom: 5px;
            text-shadow: 0 0 5px #ffcc00;
        }

        /* নামের নিচে সাইটের টাইটেল */
        .site-title {
            color: #ffcc00;
            font-size: 26px;
            font-weight: bold;
            text-shadow: 0 0 10px #ffcc00;
            margin-bottom: 20px;
        }

        /* হোমপেজে সুন্দর স্বাগতম নোটিশ বক্স */
        .welcome-board {
            background: rgba(255, 0, 85, 0.05);
            border: 1px dashed #ff0055;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            text-align: left;
            font-size: 13.5px;
            line-height: 1.5;
        }
        .welcome-board h3 {
            margin: 0 0 10px 0;
            color: #ffcc00;
            text-align: center;
            font-size: 16px;
        }

        .btn-social {
            display: block;
            padding: 12px;
            margin: 10px 0;
            text-decoration: none;
            font-weight: bold;
            border-radius: 8px;
            font-size: 14px;
            color: #fff;
            text-align: center;
        }
        .btn-telegram { background: #0088cc; box-shadow: 0 0 5px #0088cc; }
        .btn-whatsapp { background: #25d366; box-shadow: 0 0 5px #25d366; }

        /* গোল্ডেন ডাউনলোড বাটনসমূহ */
        .btn-dl {
            display: block;
            background: linear-gradient(145deg, #ffb300, #ffcc00);
            color: #000;
            padding: 13px;
            margin: 10px 0;
            text-decoration: none;
            font-weight: bold;
            border-radius: 8px;
            font-size: 13px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
            transition: 0.2s;
            text-align: center;
        }
        .btn-dl:hover {
            transform: scale(1.01);
            box-shadow: 0 0 10px #ffcc00;
        }

        /* --- মিনি চ্যাটজিপিটি চ্যাটবক্স ডিজাইন --- */
        .ai-chat-box { 
            position: fixed; 
            bottom: 15px; 
            right: 15px; 
            width: 320px; 
            height: 450px; 
            background: #111; 
            border: 2px solid #ffcc00; 
            border-radius: 12px; 
            display: none; 
            flex-direction: column; 
            overflow: hidden; 
            box-shadow: 0 0 15px rgba(255,204,0,0.4); 
            z-index: 1000; 
        }
        
        .chat-header { 
            background: #ffcc00; 
            color: #000; 
            padding: 10px 12px; 
            font-weight: bold; 
            font-size: 13.5px; 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
        }
        .chat-close-btn { background: none; border: none; color: #000; font-size: 18px; font-weight: bold; cursor: pointer; }
        .chat-messages { flex: 1; padding: 10px; overflow-y: auto; text-align: left; }
        
        .msg-box { 
            background: #1a1a1a; 
            padding: 10px; 
            margin: 8px 0; 
            border-radius: 8px; 
            border-left: 4px solid #ffcc00; 
            font-size: 13px;
            line-height: 1.4;
        }
        
        .id-copy-box {
            background: #222;
            border: 1px dashed #ffcc00;
            padding: 6px;
            margin-top: 10px;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .btn-id-copy {
            background: #ffcc00;
            color: #000;
            border: none;
            padding: 3px 8px;
            font-size: 11px;
            font-weight: bold;
            border-radius: 4px;
            cursor: pointer;
        }

        .msg-tools { 
            font-size: 11px; 
            color: #ffcc00; 
            margin-top: 6px; 
            display: flex; 
            gap: 10px; 
            justify-content: flex-end; 
        }
        .tool-btn { cursor: pointer; font-weight: bold; background: none; border: none; color: #ffcc00; padding: 0; font-size: 11px; }
        .tool-btn:hover { text-decoration: underline; }

        .chat-input-area { display: flex; border-top: 1px solid #222; background: #000; }
        .chat-input { flex: 1; background: #000; color: #fff; border: none; padding: 12px; outline: none; font-size: 13px; }
        .chat-send { background: #ffcc00; color: #000; border: none; padding: 0 15px; font-weight: bold; cursor: pointer; }

        /* ফ্লোটিং এআই চ্যাট বাটন */
        .chat-open-badge {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #ffcc00;
            color: #000;
            padding: 12px 20px;
            border-radius: 30px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 0 15px #ffcc00;
            z-index: 999;
        }

        /* --- স্পেশাল ডান্সিং পপআপ স্ক্রিন --- */
        .dance-overlay {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.9);
            display: none;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            z-index: 2000;
        }
        .dancing-emoji {
            font-size: 80px;
            animation: danceAnim 0.6s infinite alternate;
        }
        .dance-text {
            color: #ffcc00;
            font-size: 18px;
            font-weight: bold;
            margin-top: 20px;
            text-shadow: 0 0 10px #ffcc00;
        }
        @keyframes danceAnim {
            0% { transform: rotate(-20deg) scale(1); }
            100% { transform: rotate(20deg) scale(1.2); }
        }
    </style>
</head>
<body>

    <div class="main-container">
        <div class="admin-badge">★ MD SUYAIF ★</div>
        <div class="site-title">★ FX FIRE TOP ★</div>

        <div class="welcome-board">
            <h3>👋 আসসালামু আলাইকুম!</h3>
            <p>আমাদের <b>FX FIRE TOP</b> পোর্টালে আপনাকে স্বাগতম। নতুন সব আপডেট, ফাইল এবং সরাসরি সাপোর্টের জন্য আমাদের অফিশিয়াল হোয়াটসঅ্যাপ চ্যানেল এবং টেলিগ্রাম গ্রুপে অবশ্যই জয়েন হয়ে থাকুন।</p>
            <a href="{{ tg_link }}" class="btn-social btn-telegram" target="_blank">✈ JOIN TELEGRAM</a>
            <a href="{{ wa_link }}" class="btn-social btn-whatsapp" target="_blank">💬 WHATSAPP CHANNEL</a>
        </div>

        {% for btn in buttons %}
            <a href="{{ btn.url }}" class="btn-dl" target="_blank">📥 {{ btn.title }}</a>
        {% endfor %}
    </div>

    <div class="chat-open-badge" id="chatOpenBtn" onclick="startDanceShow()">🤖 AI CHAT</div>

    <div class="dance-overlay" id="danceOverlay">
        <div class="dancing-emoji">💃✨🕺</div>
        <div class="dance-text">Entering FX AI Premium Dashboard... 🚀</div>
    </div>

    <div class="ai-chat-box" id="aiChatBox">
        <div class="chat-header">
            <span>🤖 MINI ChatGPT (FX AI)</span>
            <button class="chat-close-btn" onclick="toggleChat(false)">&times;</button>
        </div>
        <div class="chat-messages" id="chatWindow">
            <div class="msg-box" id="welcomeMsg">
                <span class="text-content">👋 Assalamu Alaikum! Welcome to FX FIRE TOP 🥰. Ami MD SUYAIF bhaiyer super intelligent Mini ChatGPT 👑. Ami duniar jekono bishoy ba gamer tricks niye banglai khub sundor kore kotha bolte pari 💖. Amader update pete nicher link e follow korun ✨. Apnar ki somoshya amake ekhane likhe bolun! 👇</span>
                
                <div class="id-copy-box">
                    <span>🆔 Admin ID: <b id="adminIdCode">567890123</b></span>
                    <button class="btn-id-copy" onclick="copyAdminId()">COPY ID</button>
                </div>

                <div class="msg-tools">
                    <button class="tool-btn" onclick="speakText('welcomeMsg')">🎧 LISTEN</button>
                    <button class="tool-btn" onclick="copyText('welcomeMsg')">COPY</button>
                    <button class="tool-btn" onclick="deleteMsg('welcomeMsg')">DELETE</button>
                </div>
            </div>
        </div>
        <div class="chat-input-area">
            <input type="text" id="userInput" class="chat-input" placeholder="Duniar jekono prosno banglai likhun...">
            <button class="chat-send" onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        // চ্যাট বাটন ক্লিক করলে ছোট ডান্স শো হয়ে চ্যাটবক্সে ঢুকবে
        function startDanceShow() {
            document.getElementById('chatOpenBtn').style.display = 'none';
            const overlay = document.getElementById('danceOverlay');
            overlay.style.display = 'flex';
            
            // ১.৫ সেকেন্ড ডান্স দেখিয়ে সোজা চ্যাটবক্সে ঢুকিয়ে দেবে
            setTimeout(() => {
                overlay.style.display = 'none';
                toggleChat(true);
            }, 1500);
        }

        function toggleChat(show) {
            document.getElementById('aiChatBox').style.display = show ? 'flex' : 'none';
            if(!show) {
                document.getElementById('chatOpenBtn').style.display = 'block';
            }
        }

        function copyAdminId() {
            const idCode = document.getElementById('adminIdCode').innerText;
            navigator.clipboard.writeText(idCode);
            alert('Admin ID Copy Hoyeche: ' + idCode);
        }

        function copyText(id) {
            const el = document.getElementById(id).querySelector('.text-content');
            navigator.clipboard.writeText(el.innerText.trim());
        }

        function deleteMsg(id) {
            document.getElementById(id).remove();
        }

        // 🎧 ১০০% নিখুঁত মিষ্টি মেয়ে কণ্ঠে মেসেজ এবং ইমোজি পড়ে শোনানোর স্পেশাল ভয়েস কোড
        function speakText(id) {
            const el = document.getElementById(id).querySelector('.text-content');
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel(); // আগের ভয়েস অফ করবে
                
                const utterance = new SpeechSynthesisUtterance(el.innerText);
                const voices = window.speechSynthesis.getVoices();
                
                // নিখুঁত বাংলা ও ইংরেজি মিক্স মিষ্টি মেয়েলি কণ্ঠ (Female Speech Engine) ফিল্টার
                let femaleVoice = null;
                for (let i = 0; i < voices.length; i++) {
                    const name = voices[i].name.toLowerCase();
                    const lang = voices[i].lang.toLowerCase();
                    if ((name.includes('female') || name.includes('girl') || name.includes('zira') || name.includes('google') || name.includes('natural')) && (lang.includes('bn') || lang.includes('en'))) {
                        femaleVoice = voices[i];
                        break;
                    }
                }
                
                if(femaleVoice) { utterance.voice = femaleVoice; }
                
                utterance.rate = 0.92; // সুন্দর, ধীরে এবং স্পষ্ট করে কথা বলার রেট
                utterance.pitch = 1.3; // কণ্ঠস্বর একদম চিকন ও মিষ্টি ফিমেল ভয়েস করার টিউনিং
                window.speechSynthesis.speak(utterance);
            } else {
                alert("Apnar browser e voice speech support kore na!");
            }
        }

        // ব্রাউজার ভয়েস ইঞ্জিন অ্যাক্টিভেশন
        if ('speechSynthesis' in window) { window.speechSynthesis.getVoices(); }

        function sendMessage() {
            const input = document.getElementById('userInput');
            const chatWindow = document.getElementById('chatWindow');
            const userText = input.value.trim();
            if(userText === '') return;

            const msgId = 'msg_' + Date.now();
            chatWindow.innerHTML += `
                <div class="msg-box" id="${msgId}" style="border-left-color: #ff0055;">
                    <span class="text-content">👤 ${userText}</span>
                    <div class="msg-tools">
                        <button class="tool-btn" onclick="speakText('${msgId}')">🎧 LISTEN</button>
                        <button class="tool-btn" onclick="copyText('${msgId}')">COPY</button>
                        <button class="tool-btn" onclick="deleteMsg('${msgId}')">DELETE</button>
                    </div>
                </div>`;
            
            input.value = '';
            chatWindow.scrollTop = chatWindow.scrollHeight;

            fetch('/ask_ai', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: userText})
            })
            .then(res => res.json())
            .then(data => {
                const aiId = 'ai_' + Date.now();
                chatWindow.innerHTML += `
                    <div class="msg-box" id="${aiId}" style="border-left-color: #00ff00;">
                        <span class="text-content">🤖 ${data.reply}</span>
                        <div class="msg-tools">
                            <button class="tool-btn" onclick="speakText('${aiId}')">🎧 LISTEN</button>
                            <button class="tool-btn" onclick="copyText('${aiId}')">COPY</button>
                            <button class="tool-btn" onclick="deleteMsg('${aiId}')">DELETE</button>
                        </div>
                    </div>`;
                chatWindow.scrollTop = chatWindow.scrollHeight;
            });
        }
    </script>
</body>
</html>
"""

# মিনি চ্যাটজিপিটি ব্যাকএন্ড ব্রেন প্রসেসর (ইমোজি সহ ফিমেল স্ক্রিপ্ট ফ্রেন্ডলি)
@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    data = request.get_json()
    user_msg = data.get('message', '').lower()
    
    # মিষ্টি ইমোজি এক্সপ্রেশন সহ চ্যাটজিপিটি ইন্টেলিজেন্স সিস্টেম
    if 'সালাম' in user_msg or 'salaam' in user_msg or 'assalamu' in user_msg:
        reply = "Walaikum Assalam dear 🥰! Ami MD SUYAIF bhaiyer Mini ChatGPT 👑. Apnake FX FIRE TOP portal e shagoto ✨. Bolun ajke ki bishoye sahajjo dorkar? 💖"
    elif 'hi' in user_msg or 'hello' in user_msg or 'হ্যালো' in user_msg:
        reply = "Hello there Sweetheart! 🥳 Ami apnar super intelligent AI assistant 💕. Duniar jekono tough proshno ba coding er help lagle amake bolun, ami shob thik kore debo! ✨"
    elif 'link' in user_msg or 'টেলিগ্রাম' in user_msg or 'telegram' in user_msg or 'whatsapp' in user_msg:
        reply = f"Amader original VIP Telegram Group link: {TG_LINK} ✈️ ebong official WhatsApp Channel link: {WA_LINK} 💬. Sobাই ekhane add thakun please! 🥰"
    elif 'id' in user_msg or 'আইডি' in user_msg:
        reply = "Admin er official VIP ID code holo 567890123 🆔. Uporer main chat-box details theke direct ekti click-e copy kore nin visual proof er jonno! 💖"
    elif 'download' in user_msg or 'ডাউনলোড' in user_msg or 'ফাইল' in user_msg:
        reply = "File download korte amader মূল হোমপেজের গোল্ডেন বাটনগুলোতে ক্লিক করুন 📥। শর্টলিংক পার হলেই আসল মিডিয়াফায়ার বা ডাউনলোড লিংক পেয়ে যাবেন সোজাসুজি ✨।"
    else:
        reply = "Wow, apnar proshnoটি ami deeply analyze korechi 🧠! Ami Mini ChatGPT-er moto duniar jekono logic, bypass, coding ba high-level gaming technical solutions jani 🚀. Amader dynamic update pete uporer links follow korun ba srasori admin er sathe chat korun 🥰!"
        
    return jsonify({'reply': reply})

@app.route('/')
def home():
    return render_template_string(MAIN_PAGE, buttons=DOWNLOAD_BUTTONS, tg_link=TG_LINK, wa_link=WA_LINK)

if __name__ == '__main__':
    app.run(debug=True)
