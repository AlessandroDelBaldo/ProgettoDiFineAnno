# RICONTROLLA LA LOGICA DELLA FUNZIONE "aggiungi_lettera()", DA FINIRE

import random
import json
from flask import render_template

lista_parole = [
{"id": 1,
"class" : "animals",
"words" : ["cane","gatto"]},
{"id" : 2,
"class" : "cities",
"words" : ["misano","morciano"]}
]

HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

def scegli_categoria() -> int:
    print("Inserire l'id di una delle seguenti categorie: ")
    for i in range(len(lista_parole)):
        print(lista_parole[i]["id"],"-",lista_parole[i]["class"])
    scelta = int(input("id:"))
    return scelta


def scegli_parola(scelta: int) -> str | list:
    parola = random.choice(lista_parole[scelta-1]["words"])
    return parola
def nascondi_paola(parola):
    parola_rivelata = []
    parola_nascosta = []
    for lettera in parola:
        parola_rivelata.append(lettera)
        parola_nascosta.append("_")
    print(parola)
    return parola_rivelata, parola_nascosta

def chiedi_lettera() -> str:
    lettera = input("Inserire una lettera: ")
    return lettera

def controlla_lettera(lettera, parola) -> str | None:
    if len(lettera) > 1:
        print("ERRORE: inserire una singola lettera alla volta")
        return None
    elif lettera != str:
        print("ERRORE: inserire una lettere dell'alfabeto")
        return None
    elif lettera not in parola:
        print(f"La lettera '{lettera}' non è presente nella parola")
        return "errore"
    elif lettera in parola:
        print("Ne hai azzeccata una")
        return "ok"

def aggiungi_lettera(controllo: str | None, parola_nascosta: list, parola_rivelata: list, lettera) -> None:
    counter = []
    tentativi = 6
    if controllo == None:
        return None
    elif controllo == "ok":
        for i in range(len(parola_rivelata)):
            if lettera == parola_rivelata[i]:
                counter.append(i)
        for index in counter:
            parola_nascosta[index] = lettera
        counter.clear()
        return parola_nascosta
    elif controllo == "errore":
        tentativi -= 1
        return tentativi
    

def avanzamento_impiccato(controllo: str | None):
    pass

scegli_parola(scegli_categoria())