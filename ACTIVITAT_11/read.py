from conection import conexio

conn = conexio()

def readBoto(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT text_content FROM text WHERE id_html='boto';''')
    res=cursor.fetchone()
    return res

def readTitol(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT text_content FROM text WHERE id_html='titol';''')
    res=cursor.fetchone()
    return res

def readImatge(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT text_content FROM text WHERE id_html='imatge';''')
    res=cursor.fetchone()
    return res

def readIntents(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT intents FROM partida;''')
    intents=cursor.fetchone()
    return intents



def readAbc(conn,idioma):
    cursor = conn.cursor()
    cursor.execute('''select text from idioma where lang=%s;''',(idioma,))
    abc = cursor.fetchone()
    return abc

def readUser(conn,id):
    cursor = conn.cursor()
    cursor.execute('''select * from infoUser where id_jugador=%s;''',(id,))
    user = cursor.fetchone()
    print(user)
    return user









