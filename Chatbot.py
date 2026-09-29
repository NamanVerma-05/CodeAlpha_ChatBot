def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm doing fine, thanks for asking! How are you?"
    elif user_input in ["what is your name", "what is your name?"]:
        return "I am a basic rule-based Python chatbot!"
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day ahead!"
    else:
        return "I'm sorry, I don't understand that. Try asking 'hello', 'how are you', or 'bye'."

def chatbot():
    print("=" * 40)
    print("        B A S I C   C H A T B O T        ")
    print("=" * 40)
    print(">> Type 'bye' or 'exit' to end the chat <<")
    print("-" * 40)

    while True:
        user_message = input("\nYou: ")
        
        if user_message.lower().strip() in ["bye", "goodbye", "exit"]:
            print(f"\nBot: {get_bot_response(user_message)}")
            print("=" * 40)
            break
            
        response = get_bot_response(user_message)
        print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot()
