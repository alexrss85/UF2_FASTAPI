from typing import List
from fastapi import FastAPI
from text_sch import text_schema,user_schema


from conection import conexio
from read import readTitol,readBoto,readImatge,readAbc,readUser,readIntents

app = FastAPI()

conn = conexio()

# GET de les tematiques que retorna llista de jsons
@app.get(path="/penjat/texts/boto")
async def read_Boto():
    return(text_schema(readBoto(conn)))

@app.get(path="/penjat/texts/titol")
async def read_Titol():
    return(text_schema(readTitol(conn)))

@app.get(path="/penjat/texts/imatge")
async def read_Imatge():
    return(text_schema(readImatge(conn)))
    


@app.get(path="/penjat/idiomes/{lang}")
async def read_Abecedari(lang: str):
    return (text_schema(readAbc(conn,lang)))


@app.get(path="/penjat/user/{id}")
async def read_User(id: str):
    return (user_schema(readUser(conn,id)))
