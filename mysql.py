"""
Este formula asume la instalación de [mysqlclient](https://pypi.org/project/mysqlclient/)

Para mas ayuda visite la [documentacion oficial](https://mysqlclient.readthedocs.io/index.html)
"""
# Importar el paquete
import _mysql

# Realizar la conexión con la bases de datos. Esta conexión será persistente, así que considere no conectarse múltiples veces
db =_mysql.connect(
    host="127.0.0.1",
    user="root",
    passwd="my-secret-pw",
    db="blog"
)

# Ejecute SQL
db.query(
    """
        CREATE TABLE IF NOT EXISTS post(
        id serial PRIMARY KEY , 
        title VARCHAR(80), 
        body text, 
        pub_date TIMESTAMP 
        )
    """
)

# Genere una transacción
db.query(
    """
      INSERT INTO post (id, title, body, pub_date) VALUES (1, 'Hello world', 'lorem ipsum', '2018-10-12');
    """
)
# Haga efectiva la transacción
db.commit()

# Obtenga los datos de la base de datos
db.query(
    """
    SELECT * FROM post;
    """
)

# Obtenga un iterador para consumir los resultados
rows = db.store_result()

# Repita mientras existan elementos en el iterador
rows.fetch_row()
