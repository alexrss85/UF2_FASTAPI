from conexio_db import conection

conn = conection.conexio()

def readText(conn):
    cursor = conn.cursor()

    cursor.execute('''select * from text;''')
    resultatConsulta = cursor.fetchall()

    return resultatConsulta


def createText(conn):
    cursor = conn.cursor()
    cursor.execute("insert into text values (%s, %s)", (id_html, text_content))
    conn.commit()


def updateText(conn):
    cursor = conn.cursor()
    cursor.execute('''update text set text_content = 'hola' where id_html = 'imatge';''')
    conn.commit()

def deleteText(conn):
    cursor = conn.cursor()
    cursor.execute("delete from text;")
    conn.commit()

