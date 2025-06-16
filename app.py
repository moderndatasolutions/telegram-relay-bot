from flask import Flask, request, jsonify
from bigquery_writer import insert_prediction
from telegram_sender import send_telegram_message

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is live"

@app.route("/test-telegram")
def test_telegram():
    status, response = send_telegram_message("Hi Andrew 👋 – Telegram is working!")
    return jsonify({"status": status, "response": response})

@app.route("/push-prediction", methods=["POST"])
def push_prediction():
    payload = request.json
    errors = insert_prediction(payload)
    if errors == []:
        send_telegram_message("✅ Prediction saved to BigQuery.")
        return jsonify({"message": "Success", "errors": None})
    else:
        return jsonify({"message": "Insert failed", "errors": errors})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
