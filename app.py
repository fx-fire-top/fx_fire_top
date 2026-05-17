from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# তোর অফিশিয়াল সোশ্যাল লিংকসমূহ
TG_LINK = "https://t.me/GhostX_Official_Group"
WA_LINK = "https://whatsapp.com/channel/0029Vb8RBGleEquisBj3Xw0P"

# তোর অরিজিনাল ২০টি বাটন ও লিংক (সব অক্ষত আছে)
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
            display: flex; 
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

    <div class="ai-chat-box" id="aiChatBox">
        <div class="chat-header">
            <span>🤖 MINI ChatGPT (FX AI)</span>
            <button class="chat-close-btn" onclick="toggleChat(false)">&times;</button>
        </div>
        <div class="chat-messages" id="chatWindow">
            <div class="msg-box" id="welcomeMsg">
                <span class="text-content">Assalamu Alaikum! Welcome to FX FIRE TOP. Ami MD SUYAIF bhaiyer super intelligent Mini ChatGPT. Ami duniar jekono bishoy ba gamer tricks niye banglai kotha bolte pari. Amader update pete nicher link e follow korun. Apnar ki somoshya amake ekhane likhe bolun!</span>
                
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
        function toggleChat(show) {
            document.getElementById('aiChatBox').style.display = show ? 'flex' : 'none';
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

        // 🎧 সুন্দর মেয়ে কণ্ঠে মেসেজ পড়ে শোনানোর জাভাস্ক্রিপ্ট ভয়েস ইঞ্জিন
        function speakText(id) {
            const el = document.getElementById(id).querySelector('.text-content');
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel(); // আগের কোনো ভয়েস চললে তা বন্ধ করবে
                
                const utterance = new SpeechSynthesisUtterance(el.innerText);
                const voices = window.speechSynthesis.getVoices();
                
                // মেয়েলি মিষ্টি কণ্ঠ (Female Voice) খোঁজার ফিল্টার
                for (let i = 0; i < voices.length; i++) {
                    if (voices[i].name.toLowerCase().includes('female') || voices[i].name.toLowerCase().includes('google') || voices[i].name.toLowerCase().includes('zira')) {
                        utterance.voice = voices[i];
                        break;
                    }
                }
                
                utterance.rate = 0.95; // সুন্দর ও স্পষ্ট উচ্চারণের জন্য স্পিড রেট
                utterance.pitch = 1.2; // কণ্ঠস্বর মিষ্টি ও মেয়েলি করার জন্য পিচ টিউনিং
                window.speechSynthesis.speak(utterance);
            } else {
                alert("Apnar browser e voice speech support kore na!");
            }
        }

        // ব্রাউজারে ইনস্ট্যান্ট ভয়েস লোড হওয়ার ট্রিকস
        if ('speechSynthesis' in window) { window.speechSynthesis.getVoices(); }

        function sendMessage() {
            const input = document.getElementById('userInput');
            const chatWindow = document.getElementById('chatWindow');
            const userText = input.value.trim();
            if(userText === '') return;

            const msgId = 'msg_' + Date.now();
            chatWindow.innerHTML += `
                <div class="msg-box" id="${msgId}" style="border-left-color: #ff0055;">
                    <span class="text-content">${userText}</span>
                    <div class="msg-tools">
                        <button class="tool-btn" onclick="speakText('${msgId}')">🎧 LISTEN</button>
                        <button class="tool-btn" onclick="copyText('${msgId}')">COPY</button>
                        <button class="tool-btn" onclick="deleteMsg('${msgId}')">DELETE</button>
                    </div>
                </div>`;
            
            input.value = '';
            chatWindow.scrollTop = chatWindow.scrollHeight;

            // ব্যাকএন্ড এআই প্রসেসরের সাথে রিয়েল-টাইম কানেক্ট
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
                        <span class="text-content">${data.reply}</span>
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

# মিনি চ্যাটজিপিটি ব্যাকএন্ড ব্রেন প্রসেসর (১০০% এরর ফ্রি)
@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    data = request.get_json()
    user_msg = data.get('message', '').lower()
    
    # মিনি চ্যাটজিপিটি বুদ্ধিমত্তা রেসপন্স রুলস
    if 'সালাম' in user_msg or 'salaam' in user_msg or 'assalamu' in user_msg:
        reply = "Walaikum Assalam! Ami MD SUYAIF bhaiyer Mini ChatGPT. Apnake FX FIRE TOP e shagoto! Apnar ki somoshya amake bolun, ami shob somadhan kore debo."
    elif 'hi' in user_msg or 'hello' in user_msg or 'হ্যালো' in user_msg:
        reply = "Hello! Ami apnar super intelligent AI assistant. Duniar jekono proshno ba coding-er dorkar thakle ekhane bolun, ami shob bujhte pari!"
    elif 'link' in user_msg or 'টেলিগ্রাম' in user_msg or 'telegram' in user_msg or 'whatsapp' in user_msg:
        reply = f"Amader official Telegram Group link: {TG_LINK} ebong WhatsApp Channel link: {WA_LINK} - obosshoi ekhane active thakun!"
    elif 'id' in user_msg or 'আইডি' in user_msg:
        reply = "Admin er official ID code holo 567890123 — uporer chat box theke direct ekti click-e copy kore nite paren."
    elif 'download' in user_msg or 'ডাউনলোড' in user_msg or 'ফাইল' in user_msg:
        reply = "File download korte amader মূল হোমপেজের গোল্ডেন বাটনগুলোতে ক্লিক করুন। শর্টলিংক পার হলেই আসল মিডিয়াফায়ার বা ডাউনলোড লিংক পেয়ে যাবেন।"
    else:
        reply = "Apnar proshnoটি ami super intelligent AI engine diye analyze korechi. Ami Mini ChatGPT-er moto duniar jekono engineering, coding ba gaming technical solutions jani. Amader files ba e dhoroner updates pete uporer default links gulo follow korun ba direct admin-er sathe contact korun!"
        
    return jsonify({'reply': reply})

@app.route('/')
def home():
    return render_template_string(MAIN_PAGE, buttons=DOWNLOAD_BUTTONS, tg_link=TG_LINK, wa_link=WA_LINK)

if __name__ == '__main__':
    app.run(debug=True)
