from flask import Flask, render_template
import random
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def immagini():
    return render_template("immagini.html")

@app.route('/meteo')
def meteo():
  nran = random.randint(0,8)
  if nran <= 2:
        immagine = "static/images/pioggia.jpg"
        previsione = "Piovoso"
  elif nran <= 5:
        immagine = "static/images/nuvoloso.jpg"
        previsione = "Nuvoloso"
  else:
        immagine = "static/images/sole.jpg"
        previsione = "Soleggiato"
  return render_template("previsioni.html", meteo = immagine, testo = previsione)

@app.route("/frasicelebri")
def libro():
    frasi = [{"Autore": "Frida Kahlo" , "Frase": "Innamorati di te, della vita e dopo di chi vuoi." },
    {"Autore": "Papa Giovanni paolo II" , "Frase": "Prendete in mano la vostra vita e fatene un capolavoro."},
    {"Autore": "Charlie Chaplin" , "Frase": "Un giorno senza un sorriso è un giorno perso."},{"Autore": "Francesco Bacone" , "Frase": "Sapere è potere."},
    {"Autore": "Italo Calvino" , "Frase": "Il divertimento è una cosa seria."},{"Autore": "Molière" , "Frase": "Maggiore è l'ostacolo, maggiore è la gloria nel superarlo."},
    {"Autore": "Les Brown", "Frase": "Più dura è la battaglia, più dolce è la vittoria."},{"Autore": "Luis Sepùlveda" , "Frase": "Vola solo chi osa farlo."},
    {"Autore": "Lucio Anneo Seneca", "Frase": "Se vuoi essere amato, ama."},{"Autore": "Voltaire", "Frase": "Chi non ha bisogno di niente non è mai povero."}]
    fraseRandom = random.randint(0,9)
    return render_template("citazioni.html", autore = frasi[fraseRandom]["Autore"], frase = frasi[fraseRandom]["Frase"])

@app.route("/quantomanca")
def calendario():
    now = datetime.now()
    fine = datetime(2022,6,8)
    return render_template("scuola.html", data = (fine - now).days)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)