from flask import Flask, render_template, request, send_file, make_response, url_for, Response, redirect
app = Flask(__name__)
import io
import geopandas
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tram_bus = geopandas.read_file("/workspace/Flask/correzioneVerificaC/tpl_percorsi_shp.zip")


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args["Scelta"]
    if scelta == "Es1":
        return redirect(url_for("lunghezza"))
    elif scelta == "Es2":
        return redirect(url_for("input"))
    else:
        return redirect(url_for("dropdown"))

@app.route('/lunghezza', methods=['GET'])
def lunghezza():
    return render_template("valori.html")

@app.route('/lunghezzaCompresa', methods=['GET'])
def lunghezzaCompresa():
    val1 = request.args["Valore1"]
    val2 = request.args["Valore2"]
    tram_bus_compresi = tram_bus[tram_bus["lung_km"].astype("float") > val1]
    tram_bus_compresi = tram_bus_compresi[tram_bus_compresi["lung_km"].astype("float") < val2]
    
    return render_template("elenco_compresi.html", tabella = tram_bus_compresi.to_html())












if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)