from flask import Flask, render_template, request, jsonify
from flask_api import status
import configparser
import psycopg2

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('padronapi.ini')
cnx=psycopg2.connect(dbname=config['DB']['name'], user=config['DB']['user'], password=config['DB']['password'], host=config['DB']['host'], port=config['DB']['port'])
cur=cnx.cursor()

@app.route('/')
def index():
    return render_template('home.html')

# Devuelve todas las provincias
@app.route('/api/provincias',methods=['POST', 'GET', 'DELETE', 'PUT'])
def provincias():
    if request.method == 'GET':
        cur.execute("SELECT * FROM provincia")
        dataJson = []
        for provincia in cur.fetchall():
            dataDict = {
                'codigo': provincia[0],
                'nombre': provincia[1]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincias'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

# Devuelve el nombre de una provincia específica
@app.route('/api/provincia/<string:codigo>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def provincia(codigo):
    if request.method == 'GET':
        cur.execute("SELECT * FROM provincia WHERE codigo=%s;",(codigo,))
        provincia=cur.fetchone()
        if provincia is None :
            content = {'Error de código': 'La provincia con el código {} no existe.'.format(codigo)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'codigo': provincia[0],
                'nombre': provincia[1]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincia'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

# Devuelve los cantones basados en el código de la provincia
@app.route('/api/cantones/<string:provincia>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def cantones(provincia):
    if request.method == 'GET':
        cur.execute("SELECT * FROM canton WHERE provincia=%s;",(provincia,))
        cantones=cur.fetchall()
        if cantones is None :
            content = {'Error de código': 'La provincia con el código {} no existe.'.format(provincia)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataJson = []
            for canton in cantones:
                dataDict = {
                    'codigo': canton[1],
                    'nombre': canton[2]
                }
                dataJson.append(dataDict)
            return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para canton'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

# Devuelve el nombre de un cantón específico basado en el código de la provincia y el cantón
@app.route('/api/canton/<string:provincia>/<string:canton>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def canton(provincia, canton):
    if request.method == 'GET':
        cur.execute("SELECT * FROM canton WHERE provincia=%s AND codigo=%s;",(provincia,canton,))
        canton=cur.fetchone()
        if canton is None :
            content = {'Error de código': 'La provincia con el código {} o el canton con el código {} no existe.'.format(provincia,canton)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataDict = {
                'codigo': canton[1],
                'nombre': canton[2]
            }
            return jsonify(dataDict), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincia'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

# Devuelve los distritos basados en el código de la provincia y el cantón
@app.route('/api/distritos/<string:provincia>/<string:canton>',methods=['POST', 'GET', 'DELETE', 'PUT'])
def distritos(provincia,canton):
    if request.method == 'GET':
        cur.execute("SELECT * FROM distrito WHERE provincia=%s AND canton=%s",(provincia,canton,))
        distritos = cur.fetchall()
        if distritos is None :
            content = {'Error de código': 'La provincia con el código {} o el cantón con el código {} no existe.'.format(provincia,canton)}
            return content, status.HTTP_404_NOT_FOUND
        else :
            dataJson = []
            for distrito in distritos:
                dataDict = {
                    'codigo': distrito[2],
                    'nombre': distrito[3]
                }
                dataJson.append(dataDict)
            return jsonify(dataJson), status.HTTP_200_OK
    else :
        content = {'Error de método': 'Sólo se soporta GET para provincia'}
        return content, status.HTTP_405_METHOD_NOT_ALLOWED

if __name__ == '__main__':
    app.debug = True
    app.run()
