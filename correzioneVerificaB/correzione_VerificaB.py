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

milano = geopandas.read_file("/workspace/Flask/correzioneVerificaB/ds964_nil_wm.zip")
stazioni = geopandas.read_file("/workspace/Flask/correzioneVerificaB/templates/ds710_coordfix_ripetitori_radiofonici_milano_160120_loc_final.geojson")


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/elenco', methods=['GET'])
def elenco():
    return render_template('radio_button.html', quartieri = milano["NIL"].sort_values(ascending = True))

@app.route('/radio', methods=['GET'])
def radio():
    user = request.args["Quartieri"]
    quartiere = milano[milano["NIL"] == user]
    radio_quart = stazioni[stazioni.within(quartiere.geometry.squeeze())]
    return render_template('elenco.html', elencoRadio = radio_quart["OPERATORE"].sort_values(ascending = True))

@app.route('/mappa', methods=['GET'])
def mappa():
    return render_template('input.html')

@app.route('/ricerca', methods=['GET'])
def ricerca():
    global mappa_quartiere, stazioni_quart
    user = request.args["Quartiere"]
    mappa_quartiere = milano[milano.NIL.str.contains(user)]
    stazioni_quart = stazioni[stazioni.within(mappa_quartiere.geometry.squeeze())]
    return render_template('mappa.html')

@app.route('/mappaQuartiere', methods=['GET'])
def mappaQuartiere():
    fig, ax = plt.subplots(figsize = (12,8))

    stazioni_quart.to_crs(epsg=3857).plot(ax=ax, color = "k")
    mappa_quartiere.to_crs(epsg=3857).plot(ax=ax, alpha=0.5, edgecolor = "k")
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/numero', methods=['GET'])
def numero():
    global numero_municipio
    numero_municipio = stazioni.groupby("MUNICIPIO")["OPERATORE"].count().reset_index()
    numero_municipio.sort_values(by = "MUNICIPIO", ascending = True)
    return render_template('grafico.html', tabella = numero_municipio.to_html())

@app.route('/grafico', methods=['GET'])
def grafico():
    # costruzione del grafico:
    fig, ax = plt.subplots(figsize = (12,6))
    x = numero_municipio.MUNICIPIO
    y = numero_municipio.OPERATORE
    ax.bar(x, y, color = "#304C89")

    # visualizzazione grafico:
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)