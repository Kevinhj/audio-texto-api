import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MSI-GF63-THIN;'
                      'Database=ANALISIS;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("SELECT * FROM ANALISIS.dbo.Carrera")

for row in cursor:
    print(row)