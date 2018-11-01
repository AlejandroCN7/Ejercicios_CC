from pymongo import MongoClient

class Futbolista:

    def __init__(self, nombre, apellidos, edad, demarcacion, internacional):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.demarcacion = demarcacion
        self.internacional = internacional

    def toDBCollection (self):
        return {
            "nombre":self.nombre,
            "apellidos":self.apellidos,
            "edad": self.edad,
            "demarcacion":self.demarcacion,
            "internacional":self.internacional
        }

    def __str__(self):
        return "Nombre: %s - Apellidos: %s - Edad: %i - Demarcación: %s - Internacional: %r" \
               %(self.nombre, self.apellidos, self.edad, self.demarcacion, self.internacional)


futbolistas= [
    Futbolista('Iker','Casillas',33,['Portero'],True),
    Futbolista('Carles','Puyol',36,['Central', 'Lateral'],True),
    Futbolista('Sergio','Ramos',28,['Lateral','Central'],True),
    Futbolista('Andrés','Iniesta',30,['Centrocampista','Delantero'],True),
    Futbolista('Fernando','Torres',30,['Delantero'],True),
    Futbolista('Leo','Baptistao',22,['Delantero'],False)
]

def mostrarTabla(collection):
    cursor = collection.find()
    for fut in cursor:
        print(fut['nombre'],' - ',fut['apellidos'],' - ',fut['edad'], ' - ',fut['demarcacion'], ' - ', fut['internacional'])


mongoClient = MongoClient('localhost',27017)

baseDatos = mongoClient.Futbol

collection = baseDatos.Futbolistas

for futbolista in futbolistas:
    collection.insert(futbolista.toDBCollection())

print("------------------------------------------------------------------------------------")
print("\n\n LA BASE DE DATOS HA SIDO MONTADA EN LOCALHOST (MONGODB)\n")
print(baseDatos)
print(collection)

#Vamos a realizar una consulta de todas las entradas de la tabla
mostrarTabla(collection)

#Podemos hacer consultas a la tabla más especificas en función de lo que estemos buscando:
print("------------------------------------------------------------------------------------")
print("\n\n BÚSQUEDA DE LOS FUTBOLISTAS QUE SEAN DELANTEROS\n")
cursor = collection.find({"demarcacion":{"$in":["Delantero"]}})
for fut in cursor:
    print(fut['nombre'],' - ',fut['apellidos'],' - ',fut['edad'], ' - ',fut['demarcacion'], ' - ', fut['internacional'])

# $In al parecer es un operador que ayuda a buscar dentro de los futbolistas en siguiendo el formato BSON (JSON binario)

# Actualizar la base de datos: Buscamos entre todos los futbolistas aquellos que tengan más de 30 años (primer argumento).
# Incrementamos su edad en 100 (segundo argumento)
# Si este campo está vacío lo crea (Tercer argumento)
# Modifica todas las entradas del collection que cumpla la condición (Cuarto argumento)
print("------------------------------------------------------------------------------------")
print("\n\n MODIFICACIÓN DE EDADES (SUMA 100 A MAYORES DE 30)\n")
collection.update({"edad":{"$gt":30}},{"$inc":{"edad":100}}, upsert = False, multi = True)
mostrarTabla(collection)

# Para borrar entradas del collection el procedimiento es similar, indicando solo la condicion de consulta que queramos
print("-----------------------------------------------------------------------------------")
print("\n\n ELIMINAMOS A AQUELLOS QUE NO SEAN INTERNACIONALES\n")
collection.remove({"internacional":False})
mostrarTabla(collection)
