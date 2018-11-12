from flask import Flask, request
from flask_restful import Resource, Api, abort
from model import Jugador

import os

app = Flask("app")
api = Api(app)

#@app.route("/")

#def hello():
    #return "Hola Mundo !! :)

j1 = Jugador("Hapneck","Alejandro","Campoy Nieves",22,["Fortnite","Hollow Knight","The Witcher"],None)
j2 = Jugador("Malcarutae","Alfonso","Barragan Lara",22,["Counter Strike"],True)
j3 = Jugador("Rekkles","Juan","Martinez Casado",22,["Fortnite","League of Legends","Counter Strike"],False)


recursos = {"jugador1":j1.__dict__(),
            "jugador2":j2.__dict__(),
            "jugador3":j3.__dict__()
            }

def abortar_ruta_inexistente(ruta):
    if ruta not in recursos:
        abort(404, message="Error 404. La ruta {} no existe".format(ruta))

class Principal(Resource):

    def get(self):
        return {'status':'OK'}

class JugadorIndividual(Resource):

    def get(self,ruta):
        abortar_ruta_inexistente(ruta)
        return {ruta:recursos[ruta]}

    def put(self,ruta):
        jugador = Jugador(request.form['nick'],request.form['nombre'],request.form['apellidos'],request.form['edad'],request.form['videojuegos'],request.form['competitivo'])
        recursos[ruta]=jugador.__dict__()
        return recursos[ruta]

    def delete(self,ruta):
        abortar_ruta_inexistente(ruta)
        del recursos[ruta]
        return '',204

class Jugadores(Resource):

    def get(self):
        return recursos

    def post(self):
        ruta = "jugador" + str(len(recursos)+1)
        jugador = Jugador(request.form['nick'], request.form['nombre'], request.form['apellidos'], request.form['edad'],
                          request.form['videojuegos'], request.form['competitivo'])
        recursos[ruta]= jugador.__dict__()
        return recursos[ruta],201

api.add_resource(Principal,'/','/principal')
api.add_resource(Jugadores,'/jugadores')
api.add_resource(JugadorIndividual,'/jugadores/<string:ruta>')

if (__name__ == '__main__'):
    # Esto es para que pueda abrirse desde cualquier puerto y direccion(de esta forma en heroku no nos da error).
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port,debug=True)
    #app.run(debug=True)