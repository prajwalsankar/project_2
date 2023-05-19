from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot
chatbot = ChatBot('MyBot')

# Train the chatbot on the English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Start chatting with the user
print('Hello, how can I help you?')
while True:
    try:
        user_input = input('> ')
        if user_input.lower() in ['exit', 'quit']:
            print('Goodbye!')
            break

        # Get a response from the chatbot
        bot_response = chatbot.get_response(user_input)
        print(bot_response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        print('Goodbye!')
        break
