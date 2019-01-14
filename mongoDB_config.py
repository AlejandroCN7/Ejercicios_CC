from model import Jugador
from mongoDB import BaseDatos

if(__name__ == "__main__"):
    direccion = "mongodb://alejandro:passMONGO@40.89.155.202:27017/MiBaseDatos"
    mongo = BaseDatos(direccion)

    j1 = Jugador("Hapneck", "Alejandro", "Campoy Nieves", 22, ["Fortnite", "Hollow Knight", "The Witcher"], True)
    j2 = Jugador("Malcaide", "Alfonso", "Barragan Lara", 22, ["Counter Strike"], True)
    j3 = Jugador("Rekkles", "Juan", "Martinez Casado", 22, ["Fortnite", "League of Legends", "Counter Strike"], False)

    mongo.insertJugador(j1)
    mongo.insertJugador(j2)
    mongo.insertJugador(j3)
