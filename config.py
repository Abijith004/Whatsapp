import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Twilio Sandbox credentials
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Your personal WhatsApp number for testing
MY_WHATSAPP_NUMBER = os.getenv("MY_WHATSAPP_NUMBER")

