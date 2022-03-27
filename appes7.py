from flask import Flask, render_template, request, send_file, make_response, url_for, Response
app = Flask(__name__)
import io
import geopandas
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

regioni = geopandas.read_file("/workspace/Flask/Reg01012021_g_WGS84.zip")
province = geopandas.read_file("/workspace/Flask/ProvCM01012021_g_WGS84.zip")
comuni = geopandas.read_file("/workspace/Flask/Com01012021_g_WGS84.zip")


@app.route('/', methods=['GET'])
def home():
    return render_template('radio_button_Regioni.html', regioni = regioni.DEN_REG)

@app.route('/province', methods=['GET'])
def prov():
    regione = request.args["Regioni"]
    provRegione = province[province.within(regioni[regioni.DEN_REG == regione].geometry.squeeze())]
    return render_template('dropdown_province.html', reg = regione, provinceReg = provRegione.DEN_PROV)

@app.route('/comuni', methods=['GET'])
def com():
    provincia = request.args["Provincia"]
    comProvincia = comuni[comuni.within(province[province.DEN_PROV == provincia].geometry.squeeze())]
    return render_template('lista_comuni.html', comuniProv = comProvincia.COMUNE.sort_values(ascending = True))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)