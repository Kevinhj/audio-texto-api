import pyodbc
from src.configs import config


def create_connection():
    conn = pyodbc.connect('Driver={SQL Server};'
                          f'Server={config.SERVER}'
                          f'Database={config.DATABASE_NAME}'
                          'Trusted_Connection=yes;')

    return conn


def select_carreras():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM RegistroInteracciones.dbo.tbCarreras")

    for row in cursor:
        print(row)

    conn.close()

select_carreras()