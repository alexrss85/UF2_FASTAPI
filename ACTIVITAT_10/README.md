DOCUMENTACIO

1. Amb l'arxiu script_insert.py extreiem les dades del csv i retornem una llista amb totes les paraules i temàtiques corresponents.

2. update.py s'encarrega d'agafar aquesta llista i afegir les dades a la db. ![alt text](/ACTIVITAT_10/img/taula_db.png)

3. read.py fa consultes a la db per obtenir les dades necessàries. 
    - readTematica() obte totes les tematiques
    - readParaula() obte una paraula aleatoria d'una temàtica determinada

4. word_sch.py s'encarrega d'adaptar les dades que necessitem al model adequat(json) per a que el retorn de la info sigui correcte.

    - word_schema tranforma en un objecte json amb clau "option" y valor el parametre que passem(str)
    - categoria_schema passa una llista d'str a json utilitzant el metode anterior

5. Un cop tenim les dades, en el main.py tenim la app de fastapi amb dos GET:

    - El primer get és per obtenir les temàtiques de les paraules, hi ha 5. Utilizant readTematica, s'obte la llista de les 5 tematiques i aplicant els metodes per passar al model adequat obtenim la següent resposta:
        ![alt text](/ACTIVITAT_10/img/getTematica.png)

    - El segon get /penjat/tematica/{option} és per obtenir una paraula aleatoria d'una temàtica determinada. Aqui estem passant com paràmetre un str que serà la temàtica sobre la cual volem la paraula. Utilizant readParaula() i word_schema per passar-la a json, obtenim la següent resposta:
        (Exemple) Amb temàtica NAVEGACIO ![alt text](/ACTIVITAT_10/img/getParaulaNav.png)
                               ESPORTS ![alt text](/ACTIVITAT_10/img/getParaulaEsp.png)
                               CUINA  ![alt text](/ACTIVITAT_10/img/getParaulaCui.png)
                               AVENTURA ![alt text](/ACTIVITAT_10/img/getParaulaAve.png)
                               INFORMATICA ![alt text](/ACTIVITAT_10/img/getParaulaInf.png)
