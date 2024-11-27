
import sys
import os
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Users/Alex/Documents/DAW2/ENTORN_SERVIDOR/UF2/FASTAPI/UF2_FASTAPI')))

from ACTIVITAT_10.conexio_db import conection

conn = conection.conexio()

def readTematica(conn):
    cursor = conn.cursor()

    cursor.execute('''select tematica from paraules_db;''')
    resultatConsulta = cursor.fetchall()

    llistaTemes = []
    for x in resultatConsulta:
        if x not in llistaTemes:
            llistaTemes.append(x)

    llistaTemes = [t[0] for t in llistaTemes]

    return llistaTemes

def readParaula(conn,tematica):
    cursor = conn.cursor()
    cursor.execute('''select paraula from paraules_db where tematica=%s;''',(tematica,))
    resultatConsulta = cursor.fetchall()

    paraules = [t[0] for t in resultatConsulta]
    numAleatori= random.randint(0, len(paraules)-1)
    res=paraules[numAleatori]

    return res






