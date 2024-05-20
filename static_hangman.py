# A BUON PUNTO, DA AGGIUNGERE QUALCHE DETTAGLIO (TENTATIVI RIMASTI, LETTERE GIA' UTILIZZATE, PLAY AGAIN)
import os
import random

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

hang_count = 0

lista_parole = ["cane", "gatto", "uccello", "elefante", "leone", "cavallo"]

parola = random.choice(lista_parole)

lunghezza_parola = len(parola)
print(f"la parola ha {lunghezza_parola} lettere")

parola_rilevata = []
for lettera in parola:
    parola_rilevata.append(lettera)

parola_nascosta =[]

lettere_già_utilizzate = []

counter = []

for lettera in parola:
    parola_nascosta.append("_")

print(parola_nascosta)
count_lettera = 0
tentativi = 6
print("BENVENUTO AL GIOCO DI HANGMAN")
print("HAI 10 TENTATIVI")
input("premi invio per iniziare")
win = False
loose = False

while "_" in parola_nascosta:
    os.system('cls'if os.name == 'nt' else 'clear')
    print(parola_nascosta)
    print(HANGMAN[hang_count])
    count= 0
    lettera = str(input("Inserire una lettera: "))
    if lettera in lettere_già_utilizzate:
        print(f"Hai già utilizzato la lettera {lettera}")
    elif len(lettera)>1:
        print("ERRORE: inserire una singola lettera alla volta")
    elif lettera not in parola:
        print(f"La lettera {lettera} non è presente nella parola")
        tentativi -= 1
        hang_count += 1
    elif lettera in parola_rilevata:
        for i in range(len(parola_rilevata)):
            #print(i)
            if lettera== parola_rilevata[i]:
                counter.append(i)
        count=0
        for i in counter:
            parola_nascosta[i] = lettera
        counter.clear()
        lettere_già_utilizzate.append(lettera)
        print(f"Ne hai azzeccata una")
        print(parola_nascosta)
    print(f"Hai ancora {tentativi} tentativi")
        #print("count:",count)
        #print("counter:",counter)
    if "_" not in parola_nascosta:
        win = True
        print(f"HAI VINTO, la parola era {parola}")
        break
        
    elif tentativi == 0:
        loose = True
        print(f"HAI PERSO, la parola era {parola}")
        break
    input("Premi invio per continuare")

