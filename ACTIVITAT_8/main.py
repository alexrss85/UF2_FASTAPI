from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app = FastAPI()


@app.get("/contactes")
async def root():
    return {"1":"Alex","2":"Arnau","3":"Adri","4":"Sergi"}

contactes = {"1":"Alex","2":"Arnau","3":"Adri","4":"Sergi"}
@app.get("/contactes/{contacte_id}")
async def read_item(contacte_id):
    if contacte_id not in contactes:
        raise HTTPException(status_code=404, detail="Contacte inexistent amb aquesta ID")
    return {"contacte_id": contacte_id}


class Item(BaseModel):
    nom: str
    cognom: str
    edat: int
    id: int
    curs: str
    correu: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    return item