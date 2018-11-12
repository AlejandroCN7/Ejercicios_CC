class Jugador:
    def __init__(self,nick,nombre,apellidos,edad,videojuegos,competitivo):
        self.nick=nick
        self.nombre=nombre
        self.apellidos=apellidos
        self.edad=edad
        self.videojuegos=videojuegos
        self.competitivo=competitivo

    def __dict__(self):
        d = {
            "Nick": self.nick,
            "Nombre": self.nombre,
            "Apellidos": self.apellidos,
            "edad": self.edad,
            "Videojuegos": self.videojuegos,
            "Competitivo": self.competitivo
        }

        return d

    def set(self,nick):
        self.nick=nick

    def aniadirVideojuego(self,juego):
        videojuegos.add(juego)

    def eliminarVideojuego(self,juego):
        if(juego in self.videojuegos):
            videojuegos.remove(juego)

prueba = Jugador("Ejemplo","Alberto","Soriano Martinez",150,["juego1","juego2","juego3"],True)

print(type(prueba))

