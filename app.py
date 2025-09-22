from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bot import process_message
from config import *

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    # Get incoming message from Twilio
    incoming_msg = request.values.get("Body", "")
    from_number = request.values.get("From")  # Sender's WhatsApp number
    
    # Process the message
    reply = process_message(incoming_msg)
    
    # Prepare Twilio response
    resp = MessagingResponse()
    resp.message(reply)
    
    print(f"Message from {from_number}: {incoming_msg}")
    print(f"Reply: {reply}")
    
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
