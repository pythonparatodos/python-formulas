"""
Este formula asume la instalación de [pymongo](https://pypi.org/project/pymongo/)

Para mas ayuda visite la [documentacion oficial](https://api.mongodb.com/python/current/)

Recuerde tener una instancia ejecutandose localmente, o en un equipo remoto (si este es el caso, verifique que los puertos
correspondientes se encuentren abiertos que Postgres este oyendo en la interfaz de red a la que usted está accediendo)
Para probar con Docker

```bash
docker run \
    --name mongo \
    -v ${PWD}/data:/data/db \
    -p 27017:27017 \
    -d mongo
```
En este caso ${PWD} hace referencia a su directorio actual,  pero puede reemplazar esto por una ruta absoluta
"""
# Importar el paquete
from pymongo import MongoClient

# Cree un cliente
client = MongoClient('mongodb://localhost:27017/')

# Seleccione la base de datos
db = client.test_database

# Obtenga una referencia a la tabla
posts = db.posts

import datetime

# Cree un diccionario
p1 = dict()
p1["title"] = "Hello world"
p1["body"] = "lorem ipsum"
p1["pub_date"] = datetime.datetime.utcnow()

# Inserte el diccionario en la tabla
inserted_post = posts.insert_one(p1)

# Encuentre un registro en mongo
post1 = posts.find_one({"title": "Hello world"})
