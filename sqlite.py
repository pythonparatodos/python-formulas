"""
Este formula no requiere ninguna instalación previa, pues sqlite está incluido dentro de la librería estándar de Python
desde Python 2.5

Para mas ayuda visite la [documentacion oficial](https://docs.python.org/3/library/sqlite3.html)

Como SQLite almacena la información en archivos locales, no es necesaria ninguna instancia de ejecución adicional
"""
# Importar el paquete
import sqlite3

# Realizar la conexión con la bases de datos, en caso de que el archivo no exista, Python lo creará, tambiéen puede enviar
# como parámetro ':memory:', el cual creará una base de datos en memoria
connection = sqlite3.connect('blog.db')

# Cree un cursor para realizar transacciones SQL
cursor = connection.cursor()

# Ejecute SQL
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS post(
        id number PRIMARY KEY , 
        title text, 
        body text, 
        pub_date text
        )
    """
)

# Genere una transacción
cursor.execute(
    """
      INSERT INTO post VALUES (1, "Hello world", "lorem ipsum", "");
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
