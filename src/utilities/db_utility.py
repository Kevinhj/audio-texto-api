import pyodbc
from src.configs import config


def create_connection():
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          f'Server={config.SERVER}'
                          f'Database={config.DATABASE_NAME}'
                          'Trusted_Connection=yes;',
                          autocommit=True)

    return conn


def select_carreras():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM RegistroInteracciones.dbo.tbCarreras")

    for row in cursor:
        print(row)

    conn.close()


def insert_interacciones(dni_cliente, dni_operador, categoria_interaccion, medio_interaccion, fecha, conversasion):
    conn = create_connection()
    cursor = conn.cursor()

    store_proc = "{call agregarInteraccion (?, ?, ?, ?, ?, ?, ?)}"
    params = (dni_cliente, dni_operador, categoria_interaccion, medio_interaccion, fecha, conversasion, 0)

    cursor.execute(store_proc, params)
    id_interaccion = cursor.fetchval()
    cursor.close()
    del cursor
    conn.close()

    return id_interaccion

def insert_sentimiento_interaccion(id_interaccion, valor_negativo, valor_neutral, valor_positivo, valor_compuesto, resultado):
    conn = create_connection()
    cursor = conn.cursor()

    store_proc = "{call agregarSentimientoInteraccion (?, ?, ?, ?, ?, ?)}"
    params = (id_interaccion, valor_negativo, valor_neutral, valor_positivo, valor_compuesto, resultado)

    cursor.execute(store_proc, params)

    cursor.close()
    del cursor
    conn.close()
