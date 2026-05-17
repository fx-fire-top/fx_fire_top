from flask import Flask, render_template_string

app = Flask(__name__)

# ১ম পেজের ডিজাইন (২০টি বাটন এবং AI চ্যাটবক্স)
MAIN_PAGE = """
<!DOCTYPE html>
<html lang="bn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FX START - Ultimate AI Portal</title>
    <style>
        body { background-color: #000; color: #fff; font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        .download-container { max-width: 500px; margin: 0 auto; }
        .btn-download { display: block; background-color: #1a1a1a; color: #ffcc00; padding: 15px; margin: 10px 0; text-decoration: none; font-weight: bold; border: 2px solid #333; border-radius: 5px; font-size: 16px; }
        .btn-download:hover { border-color: #ffcc00; }
        
        /* AI Chatbot */
        .ai-chat-box { position: fixed; bottom: 20px; right: 20px; width: 300px; height: 400px; background: #111; border: 2px solid #ffcc00; border-radius: 10px; display: flex; flex-direction: column; overflow: hidden; box-shadow: 0 0 15px rgba(255,204,0,0.3); z-index: 1000; }
        .chat-header { background: #ffcc00; color: #000; padding: 10px; font-weight: bold; font-size: 14px; }
        .chat-messages { flex: 1; padding: 10px; overflow-y: auto; text-align: left; font-size: 13px; }
        .msg-box { position: relative; background: #222; padding: 8px; margin: 5px 0; border-radius: 5px; border-left: 3px solid #ffcc00; }
        .msg-tools { font-size: 10px; color: #888; margin-top: 5px; cursor: pointer; text-align: right; }
        .chat-input-area { display: flex; border-top: 1px solid #333; }
        .chat-input { flex: 1; background: #000; color: #fff; border: none; padding: 10px; outline: none; }
        .chat-send { background: #ffcc00; color: #000; border: none; padding: 10px; font-weight: bold; cursor: pointer; }
    </style>
</head>
<body>

    <h2 style="color: #ffcc00;">★ FX START ★</h2>
    <p>Welcome to FX START Ultimate AI Portal</p>

    <div class="download-container">
        <a href="https://shrinkme.click/P6sAI8p" class="btn-download">📥 DOWNLOAD GUILD GLORY BOT</a>
        <a href="https://shrinkme.click/b6WLB" class="btn-download">📥 DOWNLOAD MTH TEAM MOD MENU</a>
        <a href="https://shrinkme.click/aPR7Z" class="btn-download">📥 DOWNLOAD GOD X MOD</a>
        <a href="https://shrinkme.click/jVMqIIZq" class="btn-download">📥 DOWNLOAD MODIFY FREESTYLE MACROID</a>
        <a href="https://shrinkme.click/9uw8mgAq" class="btn-download">📥 DOWNLOAD GIFT SEND PROXY SERVER</a>
        <a href="https://shrinkme.click/0okZ" class="btn-download">📥 DOWNLOAD GHOST PROXY SERVER</a>
        <a href="https://shrinkme.click/2N68at" class="btn-download">📥 DOWNLOAD SIGMA GAME</a>
        <a href="https://shrinkme.click/XJwJU" class="btn-download">📥 DOWNLOAD ITACHI MACRO</a>
        <a href="https://shrinkme.click/Y46h" class="btn-download">📥 DOWNLOAD OB53 TCP BOT</a>
        <a href="https://shrinkme.click/SkJ7C" class="btn-download">📥 DOWNLOAD FAKE LAG VIP</a>
        <a href="https://shrinkme.click/SrxqXW" class="btn-download">📥 DOWNLOAD FREE LIKE WEBSITE</a>
        <a href="https://shrinkme.click/ArKl" class="btn-download">📥 DOWNLOAD EX EMULATOR</a>
        <a href="https://shrinkme.click/BSbBa" class="btn-download">📥 DOWNLOAD SENSI FLASH</a>
        <a href="https://shrinkme.click/VNTOih" class="btn-download">📥 DOWNLOAD GIFT SEND PROXY</a>
        <a href="https://shrinkme.click/7qZM" class="btn-download">📥 DOWNLOAD SENSI PROXY</a>
        <a href="https://shrinkme.click/2N68at" class="btn-download">📥 DOWNLOAD MAIN ID INJECTOR</a>
        <a href="https://shrinkme.click/ptF0Y" class="btn-download">📥 DOWNLOAD BLUSTRACK</a>
        <a href="https://shrinkme.click/Y46h" class="btn-download">📥 DOWNLOAD OB53 EMOTE BOT</a>
        
        <a href="https://shrinkme.click/P6sAI8p" class="btn-download">📥 DOWNLOAD VIP CONFIG PACK PRO</a>
        <a href="https://shrinkme.click/P6sAI8p" class="btn-download">📥 DOWNLOAD ANTIBAN BYPASS V20</a>
    </div>

    <div class="ai-chat-box">
        <div class="chat-header">🤖 FX SUPER AI ASSISTANT</div>
        <div class="chat-messages" id="chatWindow">
            <div class="msg-box" id="welcomeMsg">Assalamu Alaikum! Ami MD SUYAIF bhaiyer special AI Assistant. Aponar somosyar kotha bolun, ami sob somosyar somadhan debo! 🚀<div class="msg-tools" onclick="copyText('welcomeMsg')">Copy</div></div>
        </div>
        <div class="chat-input-area">
            <input type="text" id="userInput" class="chat-input" placeholder="Yekono prosno ekhane likhun...">
            <button class="chat-send" onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        function sendMessage() {
            const input = document.getElementById('userInput');
            const chatWindow = document.getElementById('chatWindow');
            if(input.value.trim() === '') return;

            const msgId = 'msg_' + Date.now();
            chatWindow.innerHTML += `<div class="msg-box" id="${msgId}">${input.value}<div class="msg-tools"><span onclick="copyText('${msgId}')">Copy</span> | <span onclick="deleteMsg('${msgId}')">Delete</span></div></div>`;
            
            setTimeout(() => {
                const aiId = 'ai_' + Date.now();
                chatWindow.innerHTML += `<div class="msg-box" id="${aiId}" style="border-left-color: #00ff00;">Ami aponar message ti peyechi. Fileটি download korte oporer button e click kore ad par korun.<div class="msg-tools"><span onclick="copyText('${aiId}')">Copy</span> | <span onclick="deleteMsg('${aiId}')">Delete</span></div></div>`;
                chatWindow.scrollTop = chatWindow.scrollHeight;
            }, 1000);

            input.value = '';
            chatWindow.scrollTop = chatWindow.scrollHeight;
        }
        function copyText(id) {
            const text = document.getElementById(id).innerText.replace('Copy', '').replace('| Delete', '');
            navigator.clipboard.writeText(text);
        }
        function deleteMsg(id) {
            document.getElementById(id).remove();
        }
    </script>
</body>
</html>
"""

# ২য় পেজের ডিজাইন (পাসওয়ার্ড ও আসল ডাউনলোড বাটন)
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
        .btn-telegram { background-color: #0088cc; color: #fff; }
    </style>
</head>
<body>

    <div class="container">
        <div class="file-name">📥 FILE VERIFIED SUCCESSFULLY</div>
        <div class="password-text">Password: <span style="color: #fff;">NO PASSWORD / 1234</span></div>
        
        <a href="https://www.mediafire.com" class="btn-action btn-download" target="_blank">📥 CLICK HERE TO DOWNLOAD</a>
        
        <p style="color: #aaa; font-size: 14px; margin-top: 30px;">এরকম ওয়েবসাইট তৈরি করতে হলে আমাদের এডমিনদের সাথে যোগাযোগ করুন।</p>
        <a href="https://t.me/your_telegram_group" class="btn-action btn-telegram" target="_blank">💬 JOIN TELEGRAM GROUP</a>
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
