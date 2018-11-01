# Ejercios sobre Desarrollo Basado en Pruebas

---

### Ejericio 1: Instalar alguno de los entornos virtuales de node.js (o de cualquier otro lenguaje con el que se esté familiarizado) y, con ellos, instalar la última versión existente, la versión minor más actual de la 4.x y lo mismo para la 0.11 o alguna impar (de desarrollo).

Hecho. He decido instalar virtualenv para Python. De esta forma tengo la posibilidad de crear entornos aislados para Python, de tal forma que puedo instalar ciertos paquetes y una versión concreta del motor de Python sin interferir en otros entornos que pueden tener otros paquetes y otra versiones del motor.

---

### Ejercicio 2: Ejecutar un programa básico que trabaje con una base de datos en diferentes versiones del lenguaje. ¿Funciona en todas ellas?

Voy a crear en entorno con virtualenv que utilice la base de datos MongoDB. El primer paso, obviamente, es instalar el entorno virtual, especificando como ruta el directorio de este repositorio localmente en mi computador:

`> virtualenv ./entorno_python/env`

Queremos que ejecute una versión concreta de Python. Esto lo podemos especificar de la siguiente forma:

`> virtualenv -p /usr/bin/python3.6 ./env`

Una vez tenemos creado nuestro entorno, es importante activarlo y podemos hacerlo a traves de un script que se genera automáticamente en el propio entorno:

`> source ./env/bin/activate`

Podemos comprobar que nos encontramos dentro del entorno porque en el prompt de shell, en el lado izquierdo aparece el nombre del entorno que habíamos asignado (env), tal y como se aprecia en la imagen:

 ![Captura de le terminal.](figuras/figura1.png)

 A partir de ahora cualquier comando o script de python se ejecutara en ese entorno virtual. Si queremos desactivar el entorno virtual, simplemente debemos poner:

 `> deactivate`

 Podemos encontrar más información sobre este proceso en el [siguiente enlace](https://osl.ugr.es/2016/10/17/entornos-virtuales-en-python-con-virtualenv/).

 Se ha realizado la instalación de [MongoDb en Ubuntu 18.04 LTS](https://www.digitalocean.com/community/tutorials/como-instalar-mongodb-en-ubuntu-16-04-es). Podemos comprobar que el proceso se ha realizado con éxito en la siguiente imagen:

 ![figura4](figuras/figura4.png)

 El siguiente paso es conectar Python con MongoDb, para ello hacemos uso de [pymongo](https://api.mongodb.com/python/current/):

 `(env) > pip install pymongo`

 En este punto, probé a crearme otro entorno virtual a ver si contenía los mismos paquetes o no, obteniendo el siguiente resultado:

 ![figura2](figuras/figura2.png)

 Como se puede apreciar, en el segundo entorno que hemos creado no contiene paquetes instalados, mientras que en el primer entorno tenemos todos los paquetes que necesitamos.

 Una vez instalado y teniendo disponible este servicio he probado un ejemplo sacado de [este tutorial](https://jarroba.com/python-mongodb-driver-pymongo-con-ejemplos/). He modificado el código para que resulte más vistoso y he entendido como funciona MongoDb con Python, lo cual considero un objetivo muy valioso. Podemos ver parte de la ejecución de todo lo que he probado en el código de [prueba.py](https://github.com/AlejandroCN7/Ejercicios_CC/tree/master/Desarrollo_Basado_en_Pruebas/prueba.py) en la siguiente imagen:

 ![figura3](figuras/figura3.png)
