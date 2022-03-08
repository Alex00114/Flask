#realizzare un server web che permetta di effettuare il login
#l'utente inserisce lo username e la password:
#se lo username è "admin" e la password è "xxx123##"
#il sito ci saluta con un messaggio di benvenuto
#altrimenti ci da un messaggio d'errore
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return render_template("login.html")

@app.route('/data', methods=['GET'])
def dati():
    nome = request.args['Username']
    password = request.args["Password"]
    if nome == "admin" and password == "xxx123##":
        return render_template("welcome.html", name = nome)
    else:
        return '<h1>Errore, username o password errati</h1>'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)