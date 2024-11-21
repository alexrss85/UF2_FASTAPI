# Agafa un usuari i tranforma les dades en json
def user_schema(user) -> dict:
    return {
        "Id": user[0],
        "Nom": user[1],
        "Cognom": user[2],
        "Correu":user[3]
    }

# Donada una llista d'usuaris transforma cadascun en json amb el metode anterior
def users_schema(users) -> dict:
    return [user_schema(user) for user in users]