
"""
Este formula asume la instalación de [psycopg2](https://pypi.org/project/psycopg2/)

Para mas ayuda visite la [documentacion oficial](https://www.psycopg.org/docs/)

Recuerde tener una instancia ejecutandose localmente, o en un equipo remoto (si este es el caso, verifique que los puertos
correspondientes se encuentren abiertos que Postgres este oyendo en la interfaz de red a la que usted está accediendo)

Para probar con Docker

```bash
docker run \
    --name postgres \
    -e POSTGRES_PASSWORD=your_secret_password \
    -v ${PWD}/pgdata:/var/lib/postgresql/data \
    -p 5432:5432 \
    -d postgres:9.6.8-alpine
```
En este caso ${PWD} hace referencia a su directorio actual,  pero puede reemplazar esto por una ruta absoluta
"""
# Importar el paquete
import psycopg2

# Realizar la conexión con la bases de datos. Esta conexión será persistente, así que considere no conectarse múltiples veces
connection = psycopg2.connect("dbname=blog user=postgres password=your_secret_password host=localhost")

# Obtenga un cursos para realizar las operaciones
cursor = connection.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS post(
        id serial PRIMARY KEY , 
        title VARCHAR(80), 
        body text, 
        pub_date TIMESTAMP 
        )
    """
)

# Ejecute SQL
cursor.execute(
    """
      INSERT INTO post (id, title, body, pub_date) VALUES (1, 'Hello world', 'lorem ipsum', '2018-10-12');
    """
)

# Haga efectiva la transacción
connection.commit()

# Obtenga los datos de la base de datos
cursor.execute(
    """
    SELECT * FROM post;
    """
)

# Obtenga todos los resultados
rows = cursor.fetchall()

