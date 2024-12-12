from typing import List
from fastapi import FastAPI
from schema import text_sch
from conexio_db import conection
from crud import read

app = FastAPI()

conn = conection.conexio()

# Boto començar partida
@app.get(path="/penjat/texts/boto")
async def read_Boto():
    return(text_sch.text_schema(read.readBoto(conn)))

# Titol començar partida
@app.get(path="/penjat/texts/titol")
async def read_Titol():
    return(text_sch.text_schema(read.readTitol(conn)))

#  Post Intents 
@app.post(path="/penjat/texts/imatge")
async def read_Imatge():
    return(text_sch.text_intents(read.updateIntents(conn)))
    
# Retorna l'idioma que volguem segons parametre(catala,castella,etc)
@app.get(path="/penjat/idiomes/{lang}")
async def read_Abecedari(lang: str):
    return (text_sch.text_schema(read.readAbc(conn,lang)))

# Retorna informacio del jugador segons ID
@app.get(path="/penjat/user/{id}")
async def read_User(id: str):
    return (text_sch.user_schema(read.readUser(conn,id)))
