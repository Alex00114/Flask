#Si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta.
#L'utente deve poter inserire il nome della squadra e la data di fondazione e la città.
#Deve, inoltre, poter effettuare delle ricerche inserendo uno dei valori dele colonne ed ottenendo i dati presenti.
from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd


@app.route('/', methods=['GET'])
def home():
    return render_template('serieA.html')









if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)