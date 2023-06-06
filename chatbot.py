import nltk
from nltk.chat.util import Chat, reflections

class ChatBot:
    def __init__(self, pairs):
        self.pairs = pairs
        self.chatbot = Chat(pairs, reflections)

    def start(self):
        print("Welcome to the ChatBot. Start chatting with the bot by typing in your message.")
        print("Enter 'quit' to exit the chat.")

        while True:
            user_input = input("User: ")

            if user_input.lower() == 'quit':
                print("ChatBot: Goodbye!")
                break

            response = self.chatbot.respond(user_input)
            print("ChatBot:", response)

# Example usage:
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am the ChatBot",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem"]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I assist you?"]
    ],
    [
        r"quit",
        ["Goodbye! Take care."]
    ]
]

chatbot = ChatBot(pairs)
chatbot.start()
