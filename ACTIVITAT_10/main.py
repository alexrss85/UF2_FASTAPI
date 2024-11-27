from typing import List
from fastapi import FastAPI
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/Users/Alex/Documents/DAW2/ENTORN_SERVIDOR/UF2/FASTAPI/UF2_FASTAPI')))

from ACTIVITAT_10.conexio_db import conection
from crud import read
from schemas import word_sch
import pydantic

app = FastAPI()

conn = conection.conexio()

# GET de les tematiques que retorna llista de jsons
@app.get(path="/penjat/tematica/opcions", response_model=List[dict])
async def read_tematica():
    print(read.readTematica(conn))
    return word_sch.categoria_schema(read.readTematica(conn)) # Agafa la llista de temes i retorna cadascuna en json

#GET de la paraula aleatoria de una tematica
@app.get(path="/penjat/tematica/{option}")
async def read_paraula(item_id: str):
    return word_sch.word_schema(read.readParaula(conn,item_id)) # Fa la consulta de paraula aleatoria a la db segons la tematica


