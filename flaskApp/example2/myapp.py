
from flask import Flask, render_template
from flask_sockets import Sockets
import json
import random

app = Flask(__name__)
sockets = Sockets(app)


quotes = json.load(open('quotes.json'))

quotesList = quotes["quotes"]

def getQuotes():
    return quotesList


@app.route('/')
def hp():
    quotesList = getQuotes()
    
    title = 'd3 server'
    quotes = quotesList
    oneQuote = random.choice(quotesList)
    
    return render_template('temp.html', title=title,quotes=quotesList,oneQuote=oneQuote)
    

if __name__ == '__main__':
    app.run(debug=True)