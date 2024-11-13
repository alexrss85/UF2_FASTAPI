from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app = FastAPI()

#get de tots els contactes
@app.get("/contactes")
async def root():
    return {"1":"Alex","2":"Arnau","3":"Adri","4":"Sergi"}

#get de contacte especific segons id
contactes = {"1":"Alex","2":"Arnau","3":"Adri","4":"Sergi"}
@app.get("/contactes/{contacte_id}")
async def read_item(contacte_id):
    #Si no existeix llançar excepció
    if contacte_id not in contactes:
        raise HTTPException(status_code=404, detail="Contacte inexistent amb aquesta ID")
    return {"contacte_id": contacte_id}

#estrucutra del baseModel
class Item(BaseModel):
    nom: str
    cognom: str
    edat: int
    id: int
    curs: str
    correu: float | None = None

#metode post
@app.post("/items/")
async def create_item(item: Item):
    return item