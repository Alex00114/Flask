#realizzare un server web che permetta di conoscere i capoluoghi di regione. L'utente inserisce il nome della regione ed il programma restituisce il nome del capoluogo di regione.
#caricare i capoluoghi e le regioni in un'opportuna struttura dati.
#modificare poi l'esercizio precedente per permettere all'utente di inserire un capoluogo e di avere la regione in cui si trova.
#L'utente sceglie se avere la regione o il capoluogo selezionando un radio button
from flask import Flask, render_template, request
app = Flask(__name__)
capoluoghiRegione = {"Abruzzo" :"L'Aquila", "Basilicata" : "Potenza", "Calabria" : "Catanzaro", "Campania" : "Napoli", "Emilia-Romagna" :"Bologna", "Friuli-Venezia" : "Trieste", "Lazio" :	"Roma", "Liguria" :	"Genova", "Lombardia" :	"Milano", "Marche" : "Ancona", "Molise" :	"Campobasso", "Piemonte"	: "Torino", "Puglia" :	"Bari", "Sardegna" :	"Cagliari", "Sicilia" :	"Palermo", "Toscana"	: "Firenze", "Trentino-Alto Adige" :	"Trento", "Umbria" :	"Perugia", "Valle d'Aosta" :	"Aosta", "Veneto" :	"Venezia" }


@app.route('/', methods=['GET'])
def home_page():
    return render_template("capoluoghi.html")

@app.route('/risultato', methods=['GET'])
def ris():
    regione = request.args["testo"]
    risposta = capoluoghiRegione[regione]
    return render_template("risultato.html", ris = risposta)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)