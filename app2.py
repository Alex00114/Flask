#realizzare un server web che visualizzi l'ora e colori lo sfondo in base all'orario: un colore per la mattina, uno per il pomeriggio ed un per la notte
from flask import Flask, render_template
app = Flask(__name__)

from datetime import datetime
tempo = datetime.time

@app.route('/', methods=['GET'])
def ciao_mondo():
    return (tempo)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)