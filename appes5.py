#Si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta.
#L'utente deve poter inserire il nome della squadra e la data di fondazione e la città.
#Deve, inoltre, poter effettuare delle ricerche inserendo uno dei valori dele colonne ed ottenendo i dati presenti.
from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd


@app.route('/', methods=['GET'])
def home():
    return render_template('serieA.html')

@app.route('/inserisci', methods=['GET'])
def inserisci():
    return render_template('inserisci.html')


@app.route('/dati', methods=['GET'])
def dati():
    # inserimento dei dati nel file csv
    # lettura dei dati dal form html 
    squadra = request.args['Squadra']
    anno = request.args['Anno']
    citta = request.args['Citta']
    # lettura dei dati dal file nel dataframe
    df = pd.read_csv('/workspace/Flask/templates/dati.csv')
    # aggiungiamo i nuovi dati nel dataframe 
    nuovi_dati = {'Squadra':squadra,'Anno':anno,'Città':citta}
    df = df.append(nuovi_dati,ignore_index=True)
    # salviamo il dataframe sul file dati.csv
    df.to_csv('/workspace/Flask/templates/dati.csv', index=False)
    return df.to_html()

@app.route('/ricerca', methods=['GET'])
def ricerca():
    return render_template('ricerca.html')

@app.route('/dati2', methods=['GET'])
def dati2():
  df = pd.read_csv('/workspace/Flask/templates/dati.csv')
  testo = request.args["Ricerca"]
  user = request.args["Scelta"]
  if user == "S":
    df1 = df[df["Squadra"] == testo]
  elif user == "C":
    df1 = df[df["Città"] == testo]
  else:
    df1 = df[df["Anno"] == int(testo)]
  return df1.to_html()


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)