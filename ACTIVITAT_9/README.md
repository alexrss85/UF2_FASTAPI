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

2 - BODY NESTED:
    Gràcies a la biblioteca de pydantic tenim altres funcionalitats:
        - VALIDACIONS:
                Podem controlar que un paràmetre del BaseModel sigui d'un tipus determinat, com ara una llista.
                    ![alt text](/ACTIVITAT_9/provaBodyNested/llistaOK.png)  
                També podem controlar el tipus de dada que conté aquesta llista. En aquest exemple estem validan que es tracten de strings, en cas  contrari dona error:
                    ![alt text](/ACTIVITAT_9/provaBodyNested/tipusDada.png)
                Es pot fer que l'atribut sigui de tipus "set" per a que no hi hagi repetits.

        - SUBMODELS:
                Pydantic permet crear objectes amb el nom que volguem i poder utilitzar-los després com atribut d'altres models:
                    ![alt text](/ACTIVITAT_9/provaBodyNested/imageObject.png)
                En aquesta foto estem creant el model Image, que després estem utilitzan com paràmetre per l'atribut image del model Item.
                A l'hora de fer la sol·licitud espera un json:
                    ![alt text](provaBodyNested/tipusDada.png)
                Permet l'ús de tipus de dades especials. Per exemple per l'url es pot utilitzar HttpUrl per valiar que la url es correcte.
                Aquests submodels especials també es poden pasar com subtipus de llistes,sets,etc. Fer la validació que, per exemple, la llista sigui d'elements tipus Image.

            Es pot posar tipus de dada diccionari i controlar el tipus tant de la clau com el valor.:
                En el segon metode POST de prova.py ens demana un diccionari amb claus tipus int i valor tipus float, en cas contrari:
                    ![alt text](/ACTIVITAT_9/provaBodyNested/dict.png)
                    Si ho fem correctament amb int i float:
                    
                    ![alt text](image.png)


8 - Documentaió

    1-L'arxiu connection.py s'encarrega d'establir la conexió amb la base de dades. Aquí tenim la taula users:
        ![alt text](/ACTIVITAT_9/img/pgadmin.png)
    2- L'arxiu crud_users conté el metode readUsers() que envia una consulta sql a la base de dades que retorna el llistat d'usuaris dins la taula users.
    3- L'arxiu users_sch.py conté dos mètodes amb les següents funcions:
        user_schema:  Agafa un usuari i tranforma les dades en json.
        users_schema:  Agafa la llista d'usuaris que retorna el readUsers, tranformant cadascun a json mitjançant el mètode anterior. Aquest metode retorna una llista de diccionaris(json) amb tots el usuaris.
    4 - En el main.py tenim la fastapi on amb el mètode get amb endpoint /users que crida els metodes de users_sch.py i retorna la llista json d'usuaris:
        ![alt text](/ACTIVITAT_9/img/getPostman.png)