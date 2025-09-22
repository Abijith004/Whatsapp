from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bot import process_message

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h1>WhatsApp Bot is running!</h1>"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.values.get("Body", "")
    resp = MessagingResponse()
    reply = process_message(incoming_msg)
    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
