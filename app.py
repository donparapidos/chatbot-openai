from flask import Flask, render_template, request, session
import os
import re
from lib.bot import *

app = Flask(__name__)
app.config['SECRET_KEY'] = flask_secret_key

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    chat_log = session.get('chat_log')
    question = request.args.get('question')
    if question == "clear history":
        chat_log = None
    if chat_log is not None:
        if len(chat_log) > 2000:
            reduced_string = re.sub(r'.', '', chat_log, count = len(question))
            chat_log = "\n".join(reduced_string.split("\n")[5:])
    botresponse = bot(prompt=question, chat_log=chat_log)
    session['chat_log'] = append_interaction_to_chat_log(question, botresponse, chat_log)
    return str(botresponse)

if __name__ == "__main__":
    app.run(debug = True)
