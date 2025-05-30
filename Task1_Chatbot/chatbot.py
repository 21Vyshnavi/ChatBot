# chatbot.py

print("Welcome to CodBot! (type 'bye' to exit)")

while True:
    user_input = input("You: ").lower()

    if user_input in ['bye', 'exit']:
        print("CodBot: Goodbye! Have a great day!")
        break
    elif "hello" in user_input:
        print("CodBot: Hi there! How can I help you?")
    elif "name" in user_input:
        print("CodBot: I am CodBot, your AI assistant.")
    elif "help" in user_input:
        print("CodBot: Sure, I'm here to assist you. Ask me anything.")
    else:
        print("CodBot: I'm sorry, I didn't understand that.")
