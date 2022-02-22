from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html", testo = "Hello, world")

@app.route('/it', methods=['GET'])
def ciao():
    return render_template("index.html", testo = "Ciao, mondo")




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)