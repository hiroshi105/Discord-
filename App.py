from flask import Flask, render_template, request
import threading
from selfbot import run_selfbot

app = Flask(__name__)
bot_thread = None

@app.route("/", methods=["GET", "POST"])
def index():
    global bot_thread
    if request.method == "POST":
        token = request.form["token"]
        message = request.form["message"]
        amount = int(request.form["amount"])
        delay = float(request.form["delay"])

        if bot_thread is None or not bot_thread.is_alive():
            bot_thread = threading.Thread(target=run_selfbot, args=(token, message, amount, delay))
            bot_thread.start()

        return "✅ Selfbot started! Keep this tab open."
    return '''
        <form method="POST">
            Token: <input name="token"><br>
            Message: <input name="message"><br>
            Amount: <input name="amount"><br>
            Delay: <input name="delay"><br>
            <button type="submit">Start Bot</button>
        </form>
    '''
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
