from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response=requests.get("http://127.0.0.1:5000/api/provincias")
    return render_template('provincias.html', data=response.json())

@app.route('/cantones')
def cantones():
    provincia = request.args.get('provincia')
    response = requests.get("http://127.0.0.1:5000/api/cantones/" + provincia)
    prov_nombre = requests.get("http://127.0.0.1:5000/api/provincia/" + provincia)
    return render_template('cantones.html', data=response.json(), prov_ref=provincia, prov_nombre=prov_nombre.json())

@app.route('/distritos')
def distritos():
    provincia = request.args.get('provincia')
    canton = request.args.get('canton')
    response=requests.get("http://127.0.0.1:5000/api/distritos/"+provincia+"/"+canton)
    prov_nombre = requests.get("http://127.0.0.1:5000/api/provincia/" + provincia)
    cant_nombre = requests.get("http://127.0.0.1:5000/api/canton/" + provincia + "/" + canton)
    return render_template('distritos.html', data=response.json(), prov_ref=provincia, prov_nombre=prov_nombre.json(), cant_nombre=cant_nombre.json())


if __name__ == '__main__':
    app.run(port=8000)
