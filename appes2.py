#Realizzare un sito web che permetta la registarzione degli utenti. L'utente inserisce il nome, uno username, una password, la conferma della password ed il sesso. 
#Se le informazioni sono corrette il sito salva le informazioni in una struttura dati opportuna.
#Prevedere la possibilit√† di fare il login inserendo username e password. Se sono corrette fornire un messaggio di benvenuto diverso a seconda del sesso.
from flask import Flask, render_template, request
app = Flask(__name__)
lista = []


@app.route('/', methods=['GET'])
def home_page():
    return render_template("registrazione.html")

@app.route('/data', methods=['GET'])
def dati():
    nome = request.args["Name"]
    username = request.args["Username"]
    conferma = request.args['ConfermaPsw']
    password = request.args["Password"]
    sesso = request.args["Sex"]
    if password == conferma:
        lista.append({'name':nome,'username':username,'password':password,'sex':sesso})
        return render_template("login_appes2.html", name = nome)
    else:
        return '<h1>Errore, password non coincidenti</h1>'

@app.route('/login', methods=['GET'])
def login():
    username_log = request.args["Username"]
    password_log = request.args["Password"]
    for utente in lista:
        if utente["username"] == username_log and utente["password"] == password_log:
            if utente["sex"] == "M":
                benv = "Benvenuto"
                return render_template("welcome.html", name = utente["name"], benvenuto = benv)
            else:
                benv = "Benvenuta"
                return render_template("welcome.html", name = utente["name"], benvenuto = benv)
    return '<h1><b>Errore, username o password non corretti</b></h1>'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)