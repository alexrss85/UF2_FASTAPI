from conexio_db import conection

conn = conection.conexio()

# Retorna el text del boto
def readBoto(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT text_content FROM text WHERE id_html='boto';''')
    res=cursor.fetchone()
    return res

# Retorna el text del titol
def readTitol(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT text_content FROM text WHERE id_html='titol';''')
    res=cursor.fetchone()
    return res

# Actualitza i mostra els intents
def updateIntents(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT intents FROM partida where id=1;''')
    intents=cursor.fetchone()
    intentsAct=int(intents[0])
    intentsAct+=1
    cursor.execute('UPDATE partida SET intents = %s where id=1;', (intentsAct,))
    conn.commit()
    return intentsAct


# Retorna l'string de l'idioma segons el que escollim
def readAbc(conn,idioma):
    cursor = conn.cursor()
    cursor.execute('''select text from idioma where lang=%s;''',(idioma,))
    abc = cursor.fetchone()
    return abc

# Retorna l'info de l'usuari que escollim
def readUser(conn,id):
    cursor = conn.cursor()
    cursor.execute('''select * from infoUser where id_jugador=%s;''',(id,))
    user = cursor.fetchone()
    print(user)
    return user









