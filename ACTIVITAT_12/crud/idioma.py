from conexio_db import conection

conn = conection.conexio()

def readIdioma(conn):
    cursor = conn.cursor()

    cursor.execute('''select * from idioma;''')
    resultatConsulta = cursor.fetchall()

    return resultatConsulta


def createIdioma(conn):
    cursor = conn.cursor()
    cursor.execute("insert into idioma values (%s, %s)", (lang, text))
    conn.commit()


def updateIdioma(conn):
    cursor = conn.cursor()
    cursor.execute('''update idioma set lang = 'es' where lang = 'castellano';''')
    conn.commit()

def deleteIdioma(conn):
    cursor = conn.cursor()
    cursor.execute("delete from idioma where lang = (%s)", (lang))
    conn.commit()

