# Agafa un usuari i tranforma les dades en json
def word_schema(paraula) -> dict:
    return {
        "Option": paraula
    }
    

# Donada una llista d'usuaris transforma cadascun en json amb el metode anterior
def categoria_schema(llistaTemes) -> dict:
    
    return [word_schema(paraula) for paraula in llistaTemes]

