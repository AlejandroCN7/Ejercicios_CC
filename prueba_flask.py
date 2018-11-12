from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask("Prueba")
api = Api(app)

#@app.route("/")

#def hello():
    #return "Hola Mundo !! :)

todos = {
"Todos":"Aqui se muestran todas las rutas a continuacion",
"tarea1":"Esta es la primera ruta.",
"tarea2":"Esta es la segunda ruta.",
"tarea3":"Esta es la tercera ruta.",
}

def abortar_ruta_inexistente(id):
    if id not in todos:
        abort(404, message="404,La ruta {} no existe".format(id))

class Principal(Resource):

    def get(self):
        return {'status':'OK'}

class Todo(Resource):

    def get(self,id):
        abortar_ruta_inexistente(id)
        return {id:todos[id]}

    def put(self,id):
        todos[id]=request.form['data']
        return {id:todos[id]}

    def delete(self,id):
        abortar_ruta_inexistente(id)
        del todos[id]
        return '',204

class Todos(Resource):

    def get(self):
        return todos

    def post(self):
        id = "tarea" + str(len(todos))
        todos[id]= request.form['data']
        return {id:todos[id]},201

api.add_resource(Principal,'/','/principal')
api.add_resource(Todos,'/todos')
api.add_resource(Todo,'/todos/<string:id>')

if (__name__ == '__main__'):
    app.run(debug=True)
