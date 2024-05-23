# RICONTROLLA LA LOGICA DELLA FUNZIONE "aggiungi_lettera()", DA FINIRE

from flask import Flask, app, render_template

import random

lista_parole = [
{"id": 1,
"class" : "animals",
"words" : ["cane","gatto"]},
{"id" : 2,
"class" : "cities",
"words" : ["misano","morciano"]}
]

counter = []

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

def scegli_categoria(lista_parole):
    print("Inserire l'id di una delle seguenti categorie: ")
    for i in range(len(lista_parole)):
        print(lista_parole[i]["id"],"-",lista_parole[i]["class"])
    scelta = int(input("id:"))
    return scelta


def scegli_parola(scelta: int):
    parola = random.choice(lista_parole[scelta-1]["words"])
    return parola

def scomponi_parola(parola):
    parola_rivelata = []
    parola_nascosta = []
    for lettera in parola:
        parola_rivelata.append(lettera)
        parola_nascosta.append("_")
    return parola_rivelata, parola_nascosta


def gioca(parola:str,parola_rivelata: list, parola_nascosta: list, counter: list, lista_utilizzate: list):
    tentativi = 6
    lettera = str(input("Inserire una lettera: "))
    if len(lettera) > 1:
        if lettera == parola:
            return lettera, "win"
        else:
            print("ERRORE: inserire una singola lettera alla volta")
            return lettera, None
    elif lettera in lista_utilizzate:
        return lettera, "hai già utilizzato questa lettera"
    elif lettera not in parola_rivelata:
        print(f"La lettera '{lettera}' non è presente nella parola")
        tentativi -= 1
        return lettera,"errore"
    elif lettera in parola_rivelata:
        if lettera in lista_utilizzate:
            return lettera, "hai già utilizzato questa lettera"
        else:
            print("Ne hai azzeccata una")
            for i in range(len(parola_rivelata)):
                if lettera== parola_rivelata[i]:
                    counter.append(i)
            for i in counter:
                parola_nascosta[i] = lettera
            counter.clear()
            return lettera, parola_nascosta
    if "_" not in parola_nascosta:
        return lettera, "win"
    elif tentativi == 0:
        return lettera, "lose"

def avanzamento_impiccato(hang_count):
    return HANGMAN[hang_count]
    

    
#def main():
#    counter = []
#    hang_count = 0
#    parola_rivelata, parola_nascosta = scomponi_parola(scegli_parola(scegli_categoria(lista_parole)))
#    parola = scegli_parola(scegli_categoria(lista_parole))
#    condition = gioca(parola, parola_rivelata, parola_nascosta, counter)
#    while condition != "win" or condition != "loose":
#        condition = gioca(parola, parola_rivelata, parola_nascosta, counter)
#        if condition == "errore":
#            hang_count += 1
#        print(avanzamento_impiccato(hang_count))

#categoria= scegli_categoria(lista_parole) #OK
#
#parola = scegli_parola(categoria)  #OK
#
#scomponi = scomponi_parola(parola) #OK
#
#lista_utilizzate = []
#
#counter = []
#
#hang_count = 0
#
#x = True
#
#while x is True:
#    play = gioca(parola, scomponi[0], scomponi[1], counter, lista_utilizzate)
#    print(play)
#    if play[1] == "win":
#        print("Hai vinto")
#        x = False
#    elif play[1] == "lose":
#        print("Hai perso")
#        x = False
#    elif play == "errore":
#        lista_utilizzate.append(play[0])
#        hang_count += 1
#        print(avanzamento_impiccato(hang_count))
#    lista_utilizzate.append(play[0])
#    print(lista_utilizzate)

app = Flask(__name__)        

@app.route("/")
def home():
    return render_template("index.html", lista_parole = lista_parole)


if __name__ == "__main__":
    app.run(debug=True, port=5057)

    

    