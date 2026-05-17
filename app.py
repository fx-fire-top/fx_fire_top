from flask import Flask, render_template_string

app = Flask(__name__)

# হোমপেজে স্বাগতম নোটিশ, প্রিমিয়াম নেওন লুক এবং ইন্টেলিজেন্ট চ্যাটবক্স
MAIN_PAGE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FX FIRE TOP - VIP AI Panel</title>
    <style>
        body { 
            background-color: #000; 
            color: #fff; 
            font-family: 'Segoe UI', Arial, sans-serif; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            padding: 15px;
            margin: 0;
        }

        /* নেওন গ্লোয়িং বর্ডার প্যানেল */
        .neon-panel {
            width: 100%;
            max-width: 480px;
            background: #050505;
            border: 3px solid #ff0055;
            border-radius: 20px;
            padding: 25px 15px;
            box-shadow: 0 0 20px #ff0055, inset 0 0 10px #ff0055;
            text-align: center;
            box-sizing: border-box;
            position: relative;
        }

        /* ওপরে তোর নাম সুন্দর করে লেখা */
        .admin-badge {
            display: inline-block;
            border: 2px solid #ffcc00;
            color: #ffcc00;
            padding: 6px 25px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 16px;
            margin-bottom: 5px;
            text-shadow: 0 0 5px #ffcc00;
            background: rgba(255, 204, 0, 0.05);
        }

        /* নামের নিচে এফএক্স ফায়ার টপ টাইটেল */
        .panel-title {
            color: #ffcc00;
            font-size: 24px;
            font-weight: bold;
            text-shadow: 0 0 10px #ffcc00;
            margin-bottom: 15px;
        }

        /* হোমপেজের মূল স্বাগতম নোটিশ বক্স */
        .welcome-notice-box {
            background: rgba(255, 0, 85, 0.05);
            border: 1px dashed #ff0055;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 20px;
            text-align: left;
            font-size: 13px;
            line-height: 1.5;
        }
        .welcome-notice-box h3 {
            margin-top: 0;
            color: #ffcc00;
            text-align: center;
            font-size: 16px;
        }

        /* সোশাল মিডিয়া বাটন */
        .btn-social {
            display: block;
            padding: 12px;
            margin: 10px 0;
            text-decoration: none;
            font-weight: bold;
            border-radius: 8px;
            font-size: 14px;
            color: #fff;
            text-transform: uppercase;
            text-align: center;
        }
        .btn-telegram { background: #0088cc; box-shadow: 0 0 8px #0088cc; }
        .btn-whatsapp { background: #25d366; box-shadow: 0 0 8px #25d366; margin-bottom: 20px; }

        /* ডাউনলোড লিস্ট কন্টেইনার */
        .download-list {
            max-height: 350px;
            overflow-y: auto;
            padding-right: 5px;
        }
        .download-list::-webkit-scrollbar { width: 5px; }
        .download-list::-webkit-scrollbar-thumb { background: #ffcc00; border-radius: 10px; }

        /* গোল্ডেন ডাউনলোড বাটন */
        .btn-download {
            display: block;
            background: linear-gradient(145deg, #ffb300, #ffcc00);
            color: #000;
            padding: 12px;
            margin: 10px 0;
            text-decoration: none;
            font-weight: bold;
            border-radius: 8px;
            font-size: 14px;
            box-shadow: 0 4px 10px rgba(255, 204, 0, 0.3);
            transition: 0.2s;
            border: none;
            text-align: center;
        }
        .btn-download:hover {
            transform: scale(1.02);
            box-shadow: 0 0 15px #ffcc00;
        }

        /* --- এআই চ্যাটবক্স প্যানেল --- */
        .ai-chat-box { 
            position: fixed; 
            bottom: 20px; 
            right: 20px; 
            width: 330px; 
            height: 460px; 
            background: #111; 
            border: 2px solid #ffcc00; 
            border-radius: 12px; 
            display: flex; 
            flex-direction: column; 
            overflow: hidden; 
            box-shadow: 0 0 20px rgba(255,204,0,0.5); 
            z-index: 1000; 
        }
        
        .chat-header { 
            background: #ffcc00; 
            color: #000; 
            padding: 12px; 
            font-weight: bold; 
            font-size: 14px; 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
        }
        .chat-close-btn { 
            background: none; 
            border: none; 
            color: #000; 
            font-size: 20px; 
            font-weight: bold; 
            cursor: pointer; 
        }

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
            padding: 8px;
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
            padding: 4px 8px;
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
        .tool-btn { cursor: pointer; font-weight: bold; }
        .tool-btn:hover { text-decoration: underline; }

        .chat-input-area { display: flex; border-top: 1px solid #222; background: #000; }
        .chat-input { flex: 1; background: #000; color: #fff; border: none; padding: 12px; outline: none; font-size: 13px; }
        .chat-send { background: #ffcc00; color: #000; border: none; padding: 0 15px; font-weight: bold; cursor: pointer; }

        .chat-open-badge {
            position: fixed;
            bottom: 25px;
            right: 25px;
            background: #ffcc00;
            color: #000;
            padding: 12px 18px;
            border-radius: 30px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 0 15px #ffcc00;
            display: none;
            z-index: 999;
        }
    </style>
</head>
<body>

    <div class="neon-panel">
        <div class="admin-badge">★ MD SUYAIF ★</div>
        <div class="panel-title">★ FX FIRE TOP ★</div>

        <div class="welcome-notice-box">
            <h3>👋 আসসালামু আলাইকুম!</h3>
            <p>আমাদের <b>FX FIRE TOP</b> পোর্টালে আপনাকে স্বাগতম। সব নতুন আপডেট, ধামাকা ফাইল এবং সরাসরি সাপোর্ট পেতে আমাদের হোয়াটসঅ্যাপ চ্যানেল এবং টেলিগ্রাম গ্রুপে অবশ্যই জয়েন হয়ে থাকুন।</p>
            <a href="https://t.me/GhostX_Official_Group" class="btn-social btn-telegram" target="_blank">✈ JOIN TELEGRAM</a>
            <a href="https://whatsapp.com/channel/0029Vb8RBGleEquisBj3Xw0P" class="btn-social btn-whatsapp" target="_blank">💬 WHATSAPP CHANNEL</a>
        </div>

        <div class="download-list">
            <a href="https://shrinkme.click/P6sAI8p" class="btn-download">📥 DOWNLOAD GUILD GLORY BOT</a>
            <a href="https://shrinkme.click/b6WLB" class="btn-download">📥 DOWNLOAD MTH TEAM MOD MENU</a>
            <a href="https://shrinkme.click/aPR7Z" class="btn-download">📥 DOWNLOAD GOD X MOD</a>
            <a href="https://shrinkme.click/2N68at" class="btn-download">📥 DOWNLOAD SIGMA GAME</a>
            <a href="https://shrinkme.click/XJwJU" class="btn-download">📥 DOWNLOAD ITALY MACRO</a>
            <a href="https://shrinkme.click/SrxqXW" class="btn-download">📥 DOWNLOAD GLITCH FILE VIP</a>
            <a href="https://shrinkme.click/2N68at" class="btn-download">📥 DOWNLOAD VVIP INJECTOR</a>
            <a href="https://shrinkme.click/jVMqIIZq" class="btn-download">📥 DOWNLOAD FREE FIRE MAX MOD</a>
            <a href="https://shrinkme.click/9uw8mgAq" class="btn-download">📥 DOWNLOAD PANEL PRO MAX</a>
            <a href="https://shrinkme.click/0okZ" class="btn-download">📥 DOWNLOAD AIMBOT CONFIG</a>
            <a href="https://shrinkme.click/Y46h" class="btn-download">📥 DOWNLOAD AUTO HEADSHOT FILE</a>
            <a href="https://shrinkme.click/SkJ7C" class="btn-download">📥 DOWNLOAD VIP RECOIL FIX</a>
            <a href="https://shrinkme.click/ArKl" class="btn-download">📥 DOWNLOAD ESP HACK TOOL</a>
            <a href="https://shrinkme.click/BSbBa" class="btn-download">📥 DOWNLOAD ANTIBAN BYPASS</a>
            <a href="https://shrinkme.click/VNTOih" class="btn-download">📥 DOWNLOAD GHOST MOD MENU</a>
            <a href="https://shrinkme.click/7qZM" class="btn-download">📥 DOWNLOAD DIAMOND HACK SIM</a>
            <a href="https://shrinkme.click/ptF0Y" class="btn-download">📥 DOWNLOAD VIP CONFIG PACK PRO</a>
            <a href="https://shrinkme.click/Y46h" class="btn-download">📥 DOWNLOAD ANTIBAN BYPASS V20</a>
            <a href="https://shrinkme.click/P6sAI8p" class="btn-download">📥 DOWNLOAD MACRO SENSITIVITY</a>
            <a href="https://shrinkme.click/b6WLB" class="btn-download">📥 DOWNLOAD RECOIL ASSISTANT</a>
        </div>
    </div>

    <div class="ai-chat-box" id="aiChatBox">
        <div class="chat-header">
            <span>🤖 FX SUPER AI ASSISTANT</span>
            <button class="chat-close-btn" onclick="toggleChat(false)">&times;</button>
        </div>
        <div class="chat-messages" id="chatWindow">
            <div class="msg-box" id="welcomeMsg">
                👋 <b>Assalamu Alaikum! Welcome to FX FIRE TOP Portal!</b><br><br>
                Ami <b>MD SUYAIF</b> bhaiyer special Super Intelligent AI Assistant. Ami Bangla ebong English sob bhashai kotha bolte pari. Apnar ki somoshya amake ekhane likhe bolun! 🚀<br><br>
                📢 <b>Amader shonge thakte nicher links bebohar korun:</b><br>
                ✈ <a href="https://t.me/GhostX_Official_Group" style="color: #ffcc00; font-weight: bold;" target="_blank">Telegram Group Link</a><br>
                💬 <a href="https://whatsapp.com/channel/0029Vb8RBGleEquisBj3Xw0P" style="color: #25d366; font-weight: bold;" target="_blank">WhatsApp Channel Link</a>
                
                <div class="id-copy-box">
                    <span>🆔 Admin ID: <b id="adminIdCode">567890123</b></span>
                    <button class="btn-id-copy" onclick="copyAdminId()">COPY ID</button>
                </div>

                <div class="msg-tools">
                    <span class="tool-btn" onclick="copyText('welcomeMsg')">COPY</span>
                    <span class="tool-btn" onclick="deleteMsg('welcomeMsg')">DELETE</span>
                </div>
            </div>
        </div>
        <div class="chat-input-area">
            <input type="text" id="userInput" class="chat-input" placeholder="Type here / এখানে লিখুন (Bangla/English)...">
            <button class="chat-send" onclick="sendMessage()">Send</button>
        </div>
    </div>

    <div class="chat-open-badge" id="chatOpenBadge" onclick="toggleChat(true)">🤖 AI CHAT</div>

    <script>
        function toggleChat(show) {
            document.getElementById('aiChatBox').style.display = show ? 'flex' : 'none';
            document.getElementById('chatOpenBadge').style.display = show ? 'none' : 'block';
        }

        // অ্যাডভান্সড স্মার্ট এআই ইঞ্জিন
        function generateAIResponse(userText) {
            const text = userText.toLowerCase();
            
            if (text.includes('hi') || text.includes('hello') || text.includes('হ্যালো') || text.includes('হাই')) {
                return "Hello! Ami MD SUYAIF bhaiyer intelligent AI. Apnar ki help dorkar amake bolun, ami shob bhasha bujhte pari!";
            }
            if (text.includes('সালাম') || text.includes('salaam') || text.includes('assalamu') || text.includes('slm')) {
                return "Walaikum Assalam! FX FIRE TOP-e apnake shagoto. Apnar ki dorkar bolun, ami shob dhoroner proshner uttor dite ready.";
            }
            if (text.includes('link') || text.includes('টেলিগ্রাম') || text.includes('telegram') || text.includes('whatsapp') || text.includes('লিংক')) {
                return "Amader Telegram Group: https://t.me/GhostX_Official_Group ebong WhatsApp Channel: https://whatsapp.com/channel/0029Vb8RBGleEquisBj3Xw0P ekhane click kore yukto thakun.";
            }
            if (text.includes('download') || text.includes('ডাউনলোড') || text.includes('file') || text.includes('ফাইল') || text.includes('কাজ করে না')) {
                return "File download korte uporer golden button-gupote click korun. Prothome link open hobe, ad par korlei Mediafire ba original download file peye jaben.";
            }
            if (text.includes('id') || text.includes('আইডি') || text.includes('copy')) {
                return "Admin er official ID uporer message box-e dewa ache, ekti click-e COPY ID button chepe nite paren.";
            }
            if (text.includes('owner') || text.includes('suyaif') || text.includes('সুয়াইফ') || text.includes('admin')) {
                return "Eiti holo MD SUYAIF bhaiyer personal VIP panel, tini-ই eitir owner technical head.";
            }
            
            return "Apnar intelligent proshnoটি ami bujhte perechi. File download er jonno uporer dynamic golden buttons bebohar korun. Kono technical somosya thakle amader Telegram/WhatsApp channel link-e click kore srasori admin er sathe contact korun.";
        }

        function sendMessage() {
            const input = document.getElementById('userInput');
            const chatWindow = document.getElementById('chatWindow');
            const userText = input.value.trim();
            if(userText === '') return;

            const msgId = 'msg_' + Date.now();
            chatWindow.innerHTML += `
                <div class="msg-box" id="${msgId}" style="border-left-color: #ff0055;">
                    \${userText}
                    <div class="msg-tools">
                        <span class="tool-btn" onclick="copyText('${msgId}')">COPY</span>
                        <span class="tool-btn" onclick="deleteMsg('${msgId}')">DELETE</span>
                    </div>
                </div>`;
            
            input.value = '';
            chatWindow.scrollTop = chatWindow.scrollHeight;

            // এআই ব্রেন রেসপন্স
            setTimeout(() => {
                const aiId = 'ai_' + Date.now();
                const aiReply = generateAIResponse(userText);
                chatWindow.innerHTML += `
                    <div class="msg-box" id="${aiId}" style="border-left-color: #00ff00;">
                        \${aiReply}
                        <div class="msg-tools">
                            <span class="tool-btn" onclick="copyText('${aiId}')">COPY</span>
                            <span class="tool-btn" onclick="deleteMsg('${aiId}')">DELETE</span>
                        </div>
                    </div>`;
                chatWindow.scrollTop = chatWindow.scrollHeight;
            }, 1000);
        }

        function copyAdminId() {
            const idCode = document.getElementById('adminIdCode').innerText;
            navigator.clipboard.writeText(idCode);
            alert('Admin ID Copy Hoyeche: ' + idCode);
        }

        function copyText(id) {
            const el = document.getElementById(id);
            const text = el.innerText.replace('COPY', '').replace('DELETE', '').replace('COPY ID', '').trim();
            navigator.clipboard.writeText(text);
        }

        function deleteMsg(id) {
            document.getElementById(id).remove();
        }
    </script>
</body>
</html>
"""

# ২য় পেজের ডিজাইন
DOWNLOAD_PAGE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FILE VERIFIED - Second Page</title>
    <style>
        body { background-color: #000; color: #fff; font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        .container { border: 2px solid #ffcc00; border-radius: 10px; padding: 20px; max-width: 400px; margin: 80px auto; background-color: #0a0a0a; }
        .file-name { color: #ffcc00; font-size: 22px; font-weight: bold; margin-bottom: 15px; }
        .password-text { color: #ff3333; font-size: 18px; font-weight: bold; margin-bottom: 25px; }
        .btn-action { display: block; padding: 12px; text-decoration: none; font-weight: bold; border-radius: 5px; margin-bottom: 15px; font-size: 16px; }
        .btn-download { background-color: #ffcc00; color: #000; }
    </style>
</head>
<body>
    <div class="container">
        <div class="file-name">📥 FILE VERIFIED SUCCESSFULLY</div>
        <div class="password-text">Password: <span style="color: #fff;">NO PASSWORD / 1234</span></div>
        <a href="https://www.mediafire.com" class="btn-action btn-download" target="_blank">📥 CLICK HERE TO DOWNLOAD</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(MAIN_PAGE)

@app.route('/second_page')
def second_page():
    return render_template_string(DOWNLOAD_PAGE)

if __name__ == '__main__':
    app.run(debug=True)
