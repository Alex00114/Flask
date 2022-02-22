#realizzare un server web che visualizzi l'ora e colori lo sfondo in base all'orario: un colore per la mattina, uno per il pomeriggio, uno per la sera ed un per la notte
from flask import Flask, render_template
app = Flask(__name__)

import datetime
ora = datetime.datetime.now()
ora = ora.hour

if ora >= 6 and ora < 13:
  @app.route('/', methods=['GET'])
  def mattina():
    return render_template("mattina.html")
elif ora >= 18 and ora < 22:
  @app.route('/', methods=['GET'])
  def pomeriggio():
    return render_template("pomeriggio.html")    
elif ora >= 18 and ora < 22:
  @app.route('/', methods=['GET'])
  def sera():
    return render_template("sera.html")
else:
  @app.route('/', methods=['GET'])
  def notte():
      return render_template("notte.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)