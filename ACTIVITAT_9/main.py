from typing import List
from fastapi import FastAPI
from db_connect import connection
from crud import crud_users
from schemas import user_sch
import pydantic

app = FastAPI()

conn = connection.conexio()

# GET /users que retorna una Llista d'elements diccionaris(json dels usuaris)
@app.get(path="/users", response_model=List[dict])
async def read_users():
    return user_sch.users_schema(crud_users.readUsers(conn)) # Agafa la llista d'usuaris que retorna el readUsers i la passa a llista de jsons


