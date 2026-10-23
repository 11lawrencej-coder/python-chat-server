from flask import Flask, jsonify

app = Flask(__name__)

CHAT_MESSAGE = "Hello world from Python!"

@app.route("/chat")
def chat():
    return jsonify({"msg": CHAT_MESSAGE})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
