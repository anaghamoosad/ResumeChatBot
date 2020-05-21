####https://dev.to/sahilrajput/build-your-first-chatbot-in-5-minutes--15e3
######https://codepen.io/meesrutten/pen/wgvpQM

#imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from chatterbot.trainers import ChatterBotCorpusTrainer
app = Flask(__name__)
#create chatbot
chatbot = ChatBot("Candice",storage_adapter='chatterbot.storage.SQLStorageAdapter',
 logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }        
        
    ],
    database_uri='sqlite:///database.sqlite3')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')
trainer.train('chatterbot.corpus.custom.resume')
trainer.train("./resume.yml")
trainer = ListTrainer(chatbot)


trainer.train([
    'How are you?',
    'I am good.',
    'Thank you',
    'You are welcome.',
])
trainer.train([
    'What is your name',
    'My name is Anagha'
    
])



#define app routes
@app.route("/")
def index():
    return render_template("home.html")
@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))
if __name__ == "__main__":
    app.run()