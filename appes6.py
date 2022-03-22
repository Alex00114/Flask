#Realizzare un sito web che restituisca la mappa dei quartieri di Milano.
#Ci deve essere una homepage con un link "quartieri di milano": cliccando su questo link si deve visualizzare la mappa dei quartieri di Milano.
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

milano = geopandas.read_file("/workspace/Flask/ds964_nil_wm.zip")


@app.route('/', methods=['GET'])
def home():
    return render_template('quartiere.html')

@app.route('/plot.png', methods=['GET'])
def plot_png():
    qrt = request.args['Quartiere']
    fig, ax = plt.subplots(figsize = (12,8))

    mappa_milano = milano[milano.NIL == qrt]
    mappa_milano.to_crs(epsg=3857).plot(ax=ax, alpha=0.6)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/plot', methods=("POST", "GET"))
def mpl():
    return render_template('plot.html', PageTitle = "Matplotlib")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)