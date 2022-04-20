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

comuni = geopandas.read_file("/workspace/Flask/correzioneVerificaA_2.1/Com01012021_g_WGS84.zip")
provincie = geopandas.read_file("/workspace/Flask/correzioneVerificaA_2.1/ProvCM01012021_g_WGS84.zip")
regioni = geopandas.read_file("/workspace/Flask/correzioneVerificaA_2.1/Reg01012021_g_WGS84.zip")
ripartizioni = geopandas.read_file("/workspace/Flask/correzioneVerificaA_2.1/templates/georef-italy-ripartizione-geografica.geojson")


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/input', methods=['GET'])
def input():
    return render_template("input.html")


@app.route('/comProv', methods=['GET'])
def comProv():
    global comuni_prov, mappa_prov
    provincia = request.args['Prov']

    mappa_prov = provincie[provincie['DEN_PROV'] == provincia]
    comuni_prov = comuni[comuni.within(mappa_prov.geometry.squeeze())]
    area = mappa_prov.geometry.area
    return render_template("comProv.html", text = area)

@app.route('/mappa', methods=['GET'])
def mappa():
    fig, ax = plt.subplots(figsize = (12,8))

    mappa_prov.to_crs(epsg=3857).plot(ax=ax, alpha=0.2, edgecolor = "k")
    comuni_prov.to_crs(epsg=3857).plot(ax=ax, alpha=0.4, edgecolor = "r")
    contextily.add_basemap(ax=ax)

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/dropdownReg', methods=['GET'])
def dropReg():
    return render_template("dropdownReg.html", regioni2 = regioni["DEN_REG"].sort_values(ascending = True))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)