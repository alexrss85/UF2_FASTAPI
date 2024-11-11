from fastapi import FastAPI

app = FastAPI()


@app.get("/contactes")
async def root():
    return {"1": "Alex","2":"Adri","3":"Arnau","4":"Sergi"}