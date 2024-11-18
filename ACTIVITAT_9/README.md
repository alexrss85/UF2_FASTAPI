1 - BODY FIELDS:
    De pydantic importem field.
    Això ens permet afegir validacions a les dades del BaseModel.
    A l'exemple de l'arxiu "ACTIVITAT_9\provaBodyField\field.py" trobem aquest model:
        ![alt text](/ACTIVITAT_9/provaBodyField/image.png). 
        En el camp price estem posant un field que valida que el valor ha de ser superior a 0.
    Si es compleix aquesta condició tot funciona  correctament:
        ![alt text](/ACTIVITAT_9/provaBodyField/ok.png)
    En canvi si posem un valor incorrecte per la condició de field:
        ![alt text](/ACTIVITAT_9/provaBodyField/notOk.png)
        Dona error 422 que diu que la peticio està ben formada però té errors semàntics. En el json que ens retorna en mostra el tipus d'error, on es troba i un missatge que l'explica. Diu: "msg": "Input should be greater than 0". Seguidament esta l'input -3, que és el price que hem posat a la sol·licitud de forma incorrecta.
    En description també torbem un field que controla que la longitud del string no pot ser superior a 300 caracters. En l'exeució funciona de la mateixa manera explicada anteriorment(validació de la dada introduïda).