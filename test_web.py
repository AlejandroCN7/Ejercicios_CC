import unittest
from model import Jugador
from principal import *
import json

#Obtenemos el diccionario de python a partir del contenido expresado en JSON
def obtenerContenidoPaquete(respuesta):
    contenido = respuesta.data.decode('utf8').replace("'", '"')
    return json.loads(contenido)


class TestModel(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # respuesta.headers para consultar el tipo MIME del contenido
    # respuesta.status_code para saber el código de la cabecera de respuesta.
    def testGetRaiz(self):
        
        respuesta = self.app.get('/')

        self.assertEqual(respuesta.status_code,200,"El servidor no se encuentra levantado.")
        self.assertEqual(respuesta.headers['content-type'],'application/json',"Tipo MIME de la cabecera no es JSON.")
        contenido = respuesta.data.decode('utf8').replace("'", '"')
        contenido = json.loads(contenido)
        self.assertEqual(contenido['status'],"OK","El contenido de la raíz no es correcta.")

        

    def testGetPrincipal(self):

        respuesta = self.app.get('/principal')

        self.assertEqual(respuesta.status_code, 200, "El servidor no se encuentra levantado.")
        self.assertEqual(respuesta.headers['content-type'], 'application/json', "Tipo MIME de la cabecera no es JSON.")
        contenido = obtenerContenidoPaquete(respuesta)
        self.assertEqual(contenido['status'], "OK", "El contenido de la raíz no es correcta.")
        
    def testError404(self):

        respuesta = self.app.get('/rutaInexistente')
        self.assertEqual(respuesta.status_code,404,"El servidor no muestra correctamente el estado de un recurso no encontrado (404), muestra en su lugar el código " + str(respuesta.status_code) + ".")


    def testGetJugadores(self):

        respuesta = self.app.get('/jugadores')
        self.assertEqual(respuesta.status_code, 200, "El recurso de jugadores no se encuentra disponible.")
        self.assertEqual(respuesta.headers['content-type'], 'application/json', "Tipo MIME de la cabecera no es JSON.")
        contenido = obtenerContenidoPaquete(respuesta)
        print(contenido)
        jugadores = contenido.keys()
        self.assertIn('jugador1',jugadores,"El jugador 1 no se encuentra disponible.")
        #self.assertIn('jugador2', jugadores, "El jugador 2 no se encuentra disponible.")
        self.assertIn('jugador3', jugadores, "El jugador 3 no se encuentra disponible.")

    def testGetJugador(self):

        respuesta = self.app.get('/jugadores/jugador1')
        self.assertEqual(respuesta.status_code, 200, "El recurso de jugador1 no se encuentra disponible." )
        self.assertEqual(respuesta.headers['content-type'], 'application/json', "Tipo MIME de la cabecera no es JSON.")
        contenido = obtenerContenidoPaquete(respuesta)
        self.assertEqual(contenido['jugador1']['Nick'],"Hapneck","El nick del jugador1 no es Hapneck.")

    def testPostJugadores(self):

        respuesta = self.app.get('/jugadores')
        self.assertEqual(respuesta.status_code, 200, "El recurso de jugadores no se encuentra disponible.")
        self.assertEqual(respuesta.headers['content-type'], 'application/json', "Tipo MIME de la cabecera no es JSON.")
        contenido = obtenerContenidoPaquete(respuesta)
        self.assertEqual(len(contenido.keys()),3,"Número de jugadores debería ser 3 en este punto.")

        respuesta = self.app.post('/jugadores',data = Jugador("EjemploPost", "Alberto", "Soriano Martinez", 15, ["juego1", "juego2", "juego3"], True).__dict__())
        contenido = obtenerContenidoPaquete(respuesta)
        self.assertEqual(respuesta.status_code, 201, "El recurso no se ha añadido correctamente con post.")
        self.assertEqual(respuesta.headers['content-type'], 'application/json', "Tipo MIME de la cabecera no es JSON.")
        self.assertEqual(contenido['Nick'],"EjemploPost","Parece que POST no ha añadido el jugador de la forma correcta.")

        respuesta = self.app.get('/jugadores')
        self.assertEqual(respuesta.status_code, 200, "El recurso de jugadores no se encuentra disponible.")
        self.assertEqual(respuesta.headers['content-type'], 'application/json', "Tipo MIME de la cabecera no es JSON.")
        contenido = obtenerContenidoPaquete(respuesta)
        self.assertEqual(len(contenido.keys()), 4, "Número de jugadores debería de ser 4 después de haber realizado un POST.")
        self.assertEqual(contenido['jugador4']['Edad'], 15, "Parece que el nuevo jugador no ha sido creado correctamente.")


    def testDeleteJugador(self):

        respuesta = self.app.get('/jugadores')
        self.assertEqual(respuesta.status_code, 200, "El recurso de jugadores no se encuentra disponible.")
        self.assertEqual(respuesta.headers['content-type'], 'application/json', "Tipo MIME de la cabecera no es JSON.")
        contenido = obtenerContenidoPaquete(respuesta)
        self.assertEqual(len(contenido.keys()), 3, "Número de jugadores debería ser 3 en este punto.")

        respuesta = self.app.delete('/jugadores/jugador2')
        self.assertEqual(respuesta.status_code, 204, "Ha habido algún error en el borrado del jugador2.")
        self.assertEqual(respuesta.headers['content-type'], 'application/json', "Tipo MIME de la cabecera no es JSON.")

        respuesta = self.app.get('/jugadores')
        self.assertEqual(respuesta.status_code, 200, "El recurso de jugadores no se encuentra disponible.")
        self.assertEqual(respuesta.headers['content-type'], 'application/json', "Tipo MIME de la cabecera no es JSON.")
        contenido = obtenerContenidoPaquete(respuesta)
        self.assertEqual(len(contenido.keys()), 2, "Número de jugadores debería encontrarse en 2.")

        respuesta = self.app.get('/jugadores/jugador2')
        self.assertEqual(respuesta.status_code, 404, "El recurso jugador2 no debería poder encontrarse.")
        self.assertEqual(respuesta.headers['content-type'], 'application/json', "Tipo MIME de la cabecera no es JSON.")


if __name__ == '__main__':
    unittest.main()