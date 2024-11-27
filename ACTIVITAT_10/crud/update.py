from db_connection import connection
from insertData import script_insert

conn = connection.conexio()

cursor = conn.cursor()

llista = script_insert.llistaParaules()
print(llista)
for x in range(0,len(llista),2):
    paraula = llista[x]
    tematica = llista[x+1]
    cursor.execute("insert into paraules_db values (%s, %s)", (paraula, tematica))
conn.commit()

