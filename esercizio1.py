from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/', methods=['GET'])
def immagini():
    return render_template("immagini.html")

@app.route('/meteo', methods=['GET'])
def meteo():
  nran = random.randint(0,8)
  if nran <= 2:
        immagine = "static/images/pioggia.jpg"
  elif nran <= 5:
        immagine = "static/images/nuvoloso.jpg"
  else:
        immagine = "static/images/sole.jpg"
  return render_template("previsioni.html", meteo = immagine)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)