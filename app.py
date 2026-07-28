from flask import Flask, render_template, request, jsonify, session
from chatbot import ChatBot

app = Flask(__name__)
app.secret_key = "nova_ai_secret_key"


@app.route("/")
def home():

    if "chat_history" not in session:
        session["chat_history"] = [
            {
                "role": "system",
                "content": "You are Nova AI, a helpful and intelligent AI assistant."
            }
        ]

    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    chat_history = session["chat_history"]

    chat_history.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    answer = ChatBot(chat_history)

    chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    session["chat_history"] = chat_history

    return jsonify(
        {
            "response": answer
        }
    )
@app.route("/new_chat", methods=["POST"])
def new_chat():

    session["chat_history"] = [
        {
            "role": "system",
            "content": "You are Nova AI, a helpful and intelligent AI assistant."
        }
    ]

    return jsonify({
        "success": True
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
