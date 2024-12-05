# Agafa un text i tranforma les dades en json
def text_schema(text) -> dict:
    return {
        "Text": text[0]
    }

def user_schema(user) -> dict:
    return {
        "id_jugador": user[0],
        "punts_actuals": user[1],
        "total_partides": user[2],
        "partide_guanyages": user[3],
        "millor_puntuacio": user[4]
    }