from typing import List
from fastapi import FastAPI
from schema import text_sch
from conexio_db import conection
from crud import idioma,paraula,partida,jugador,text


app = FastAPI()

conn = conection.conexio()

# CRUDS

# PARTIDA
@app.get(path="/penjat/partida/{id}")
async def read_Partida(id: int):
    return ({"text":"{id}"})

@app.post("/penjat/partida/post")
async def create_Partida():
    id=5
    intents=0
    partida.createPartida(id,intents,conn)
    return {"message": f"Partida creada"}


@app.put("/penjat/partida/put")
async def update_Partida():
        partida.updatePartida(conn)
        return {"message": f"Partida actualitzada"}


@app.delete("/penjat/partida/delete")
async def delete_Partida():
    partida.deletePartida( conn)
    return {"message": f"Partida esborrada"}


# TEXT
@app.get(path="/penjat/texts/data")
async def read_Text():
    return(text_sch.text_schema(text.readText(conn)))


@app.post("/penjat/texts/post")
async def create_Text():
    id_html="imatge"
    text_content="hola"
    text.createText(id_html,text_content,conn)
    return {"message": f"Text creat"}


@app.put("/penjat/texts/put")
async def update_Text():
        text.updateText(conn)
        return {"message": f"Text actualizat"}


@app.delete("/penjat/text/delete")
async def delete_Text():
    text.deleteText(conn)
    return {"message": f"Text esborrat"}

# PARAULES

@app.get("/penjat/paraules")
async def read_Paraules():
    return(text_sch.paraules_schema(text_sch.paraula_schema(paraula.readParaules)))

@app.post("/penjat/paraules/post")
async def create_paraules():
    paraules="hola"
    tematica="presentacio"
    paraula.createParaules(paraules,tematica,conn)
    return {"message": f"Paraula creada"}


@app.put("/penjat/paraules/put")
async def update_paraules():
        paraula.updateParaules(conn)
        return {"message": f"Paraula actualizada"}


@app.delete("/penjat/paraules/delete")
async def delete_text():
    paraula.deleteParaules(conn)
    return {"message": f"Paraula esborrada"}



    
# IDIOMA
@app.get(path="/penjat/idiomes/{lang}")
async def read_Abecedari(lang: str):
    return (text_sch.text_schema(idioma.readIdioma(lang,conn)))

@app.post("/penjat/idiomes/post")
async def create_Abecedari():
    lang="corea"
    text="가나다라마바사아자차카타파하"
    idioma.createIdioma(lang,text,conn)
    return {"message": f"Idioma creat"}


@app.put("/penjat/idiomes/put")
async def update_Abecedari():
        idioma.updateIdioma(conn)
        return {"message": f"Idioma actualitzat"}


@app.delete("/penjat/idiomes/delete")
async def delete_Abecedari(lang: str):
    idioma.deleteIdioma(conn)
    return {"message": f"Idioma esborrat"}




# JUGADOR
@app.get(path="/penjat/jugadors/{id}")
async def read_Jugadors(id: str):
    return (text_sch.text_schema(idioma.readIdioma(id,conn)))

@app.post("/penjat/jugadors/post")
async def create_Jugador():
    id=45
    puntsActuals=30
    totalPartides=3
    partidesGuanyades=10
    millorPuntuacio=150
    jugador.createJugador(id,puntsActuals,totalPartides,partidesGuanyades,millorPuntuacio,conn)
    return {"message": f"Jugador creat"}


@app.put("/penjat/jugadors/put")
async def update_Jugador(lang: str, data: dict):
        idioma.createIdioma(lang, text, conn)
        return {"message": f"Idioma actualitzat"}


@app.delete("/penjat/jugadors/delete")
async def delete_Jugador():
    idioma.deleteIdioma(conn)
    return {"message": f"Idioma esborrat"}