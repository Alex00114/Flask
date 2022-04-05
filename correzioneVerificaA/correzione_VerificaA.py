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

stazioni = pd.read_csv("/workspace/Flask/correzioneVerificaA/templates/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv", sep = ";")
stazioni_geo = geopandas.read_file("/workspace/Flask/correzioneVerificaA/templates/ds710_coordfix_ripetitori_radiofonici_milano_160120_loc_final.geojson")
milano = geopandas.read_file("/workspace/Flask/correzioneVerificaA/ds964_nil_wm.zip")


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args["Scelta"]
    if scelta == "Es1":
        return redirect(url_for("numero"))
    elif scelta == "Es2":
        return redirect(url_for("input"))
    else:
        return redirect(url_for("dropdown"))

@app.route('/numero', methods=['GET'])
def numero():
    global risultato
    risultato = stazioni.groupby("MUNICIPIO")["OPERATORE"].count().reset_index()
    return render_template('es1.html', ris = risultato.to_html())

@app.route('/grafico', methods=['GET'])
def grafico():
    # costruzione del grafico:
    fig, ax = plt.subplots(figsize = (12,6))
    x = risultato.MUNICIPIO
    y = risultato.OPERATORE
    ax.bar(x, y, color = "#304C89")

    # visualizzazione grafico:
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/input', methods=['GET'])
def input():
    return render_template('input.html')

@app.route('/ricerca', methods=['GET'])
def ricerca():
    user = request.args["Scelta"]
    mappa_quartiere = milano[milano.NIL.str.contains(user)]
    radio_quart = stazioni_geo[stazioni_geo.within(mappa_quartiere.geometry.squeeze())]
    return render_template('elenco.html', elencoRadio = radio_quart.OPERATORE.sort_values(ascending = True))

@app.route('/dropdown', methods=['GET'])
def dropdown():
    nomi_stazioni = stazioni.OPERATORE.to_list()
    nomi_stazioni = list(set(nomi_stazioni))
    nomi_stazioni.sort()
    return render_template('dropdown.html', radio = nomi_stazioni)

@app.route('/scelta_stazione', methods=['GET'])
def scelta_stazioni():
    global quartiere1, stazione_utente
    stazione = request.args["Stazione"]
    stazione_utente = stazioni_geo[stazioni_geo.OPERATORE == stazione]
    quartiere1 = milano[milano.contains(stazione_utente.geometry.squeeze())]
    return render_template('vista_stazione.html', quartiere = quartiere1.NIL)

@app.route('/mappa_quart', methods=['GET'])
def mappa_quart():
    fig, ax = plt.subplots(figsize = (12,8))

    stazione_utente.to_crs(epsg=3857).plot(ax=ax, color = "k")
    quartiere1.to_crs(epsg=3857).plot(ax=ax, alpha=0.6, edgecolor = "k")
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)