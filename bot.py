def process_message(message):
    """
    Simple bot logic: replies based on user message
    """
    msg = message.lower()
    
    if "hi" in msg or "hello" in msg:
        return "Hello! I am your WhatsApp bot 🤖. How can I help you today?"
    elif "help" in msg:
        return "You can say hi, hello or ask me anything."
    else:
        return "Sorry, I didn't understand that. Type 'help' for guidance."
