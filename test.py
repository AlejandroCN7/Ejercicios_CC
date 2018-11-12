import unittest
import subprocess
from principal import Principal, Jugadores, JugadorIndividual
from model import Jugador

class TestModel(unittest.TestCase):

    def testTipoCreacion(self):
        prueba = Jugador("Ejemplo","Alberto","Soriano Martinez",150,["juego1","juego2","juego3"],True)
        self.assertIsInstance(prueba,Jugador,"Tipo de objeto jugador incorrecto.")

    def testUnicidad(self):
        prueba = Jugador("Ejemplo", "Alberto", "Soriano Martinez", 150, ["juego1", "juego2", "juego3"], True)
        prueba2 = Jugador("Ejemplo", "Alberto", "Soriano Martinez", 150, ["juego1", "juego2", "juego3"], True)
        self.assertIs(prueba,prueba2,"Dos objetos con los mismos atributos no pueden ser el mismo.")

    def testCambioNick(self):
        prueba = Jugador("Ejemplo", "Alberto", "Soriano Martinez", 150, ["juego1", "juego2", "juego3"], True)
        prueba.setNick("nuevoNick")
        self.assertIsInstance(prueba.nick,str,"El tipo del campo nick no es correcto al cambiarlo")
        self.assertEqual(prueba.nick,"nuevoNick","El atrubuto Nick no se ha modificado correctamente.")

    def testInsertar(self):
        prueba = Jugador("Ejemplo", "Alberto", "Soriano Martinez", 150, ["juego1", "juego2", "juego3"], True)
        prueba.aniadirVideojuego("Nuevo Juego")
        self.assertIn("Nuevo Juego",prueba.videojuegos,"No se ha agregado un videojuego al jugador correctamente.")

    def testEliminar(self):
        prueba = Jugador("Ejemplo", "Alberto", "Soriano Martinez", 150, ["juego1", "juego2", "juego3"], True)
        self.assertEqual(len(prueba.videojuegos),3,"No se ha creado el vector de videojuegos del jugador correctamente.")
        prueba.eliminarVideojuego("Juego que no tiene el jugador")
        self.assertEqual(len(prueba.videojuegos), 3, "Se eliminan juegos que no existen??")
        prueba.eliminarVideojuego("juego2")
        self.assertNotIn("juego2",prueba.videojuegos,"Los videojuegos especificados no se eliminan bien del jugador.")

