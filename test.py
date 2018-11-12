import unittest
from model import Jugador

class Test(unittest.TestCase):

    def testCreacion(self):
        prueba = Jugador("Ejemplo","Alberto","Soriano Martinez",150,["juego1","juego2","juego3"],True)

