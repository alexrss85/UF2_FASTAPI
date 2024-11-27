import pandas as pd

def llistaParaules():

    df = pd.read_csv("ACTIVITAT_10\csv\paraules_temàtica_penjat.csv") #Generem el dataFrame amb les dades

    paraules=[]
    i=0
    #Afegim les paraules i la seva tematica a una llista
    for x in df.WORD:
        paraules.append(x)
        paraules.append(df.THEME[i])
        i+=1
    return paraules
