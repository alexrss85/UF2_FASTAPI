from typing import List
from fastapi import FastAPI
from text_sch import text_schema


from conection import conexio
from read import readTitol,readBoto,readImatge,readAbc

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
    



@app.get(path="/penjat/lang/{idioma}")
async def read_Abecedari(idioma: str):
    return (text_schema(readAbc(conn,idioma)))

