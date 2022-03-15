#Si vuole realizzare un sito web che permetta di visualizzare alcune informazioni sull'andamento dell'epidemia di covid nel nostro paese, a partire dai dati presenti nel file. 
#L'utente sceglie la regione da un elenco(menù a tendina), clicca su un bottone ed il sito deve visualizzare una tabela contenente le informazioni relative a quella regione.
#I dati da inserire nel menù a tendina devono essere caricati automaticamente dalla pagina
from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd 

df = pd.read_csv("https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/platea-dose-addizionale-booster.csv")

@app.route('/', methods=['GET'])
def home():
    reg = df['nome_area'].drop_duplicates().to_list()
    return render_template('covid.html', reg=reg)

@app.route('/data', methods=['GET'])
def risultato():
    regione = request.args['vaccini']
    df3 = df[df['nome_area']== regione]
    return render_template('covid1.html', tables=[df3.to_html()], titles=[''])

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)