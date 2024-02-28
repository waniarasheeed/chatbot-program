import random


# Define a function to respond to user input
def chatbot_response(user_input):
    greetings = ["hi", "hello", "hey", "hola"]
    responses = ["Nice to meet you!", "Hello!", "Hi there!", "Hey! How can I help you?"]

    if user_input.lower() in greetings:
        return random.choice(responses)
    else:
        return "I'm just a simple chatbot. Say 'hi' to start a conversation!"


# Main loop to keep the chatbot running
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot:", chatbot_response(user_input))