# app.py
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

@app.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()
    message = data.get("message", "No message provided.")

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    response = requests.post(url, json=payload)
    return jsonify({"status": "sent", "response": response.json()}), 200

@app.route("/", methods=["GET"])
def root():
    return "Relay is active.", 200
