# ***** GIOCO DEL LOTTO *****
# 1. Generazione di 5 numeri random compresi tra 1 e 90 inclusi
import random
import termcolor
import re


cinquina_lista = []
while True:
    numero_generato = random.randint(1, 90)
    if numero_generato not in cinquina_lista:
        cinquina_lista.append(numero_generato)
    if len(cinquina_lista) == 5:
        break
print(cinquina_lista)

# 2. Chiedere all'utente i numeri che vuole giocare
regex_numero = "^\d+$"
cinquina_utente = []
while True:
     numero_giocato = input(f"{len(cinquina_utente) +1}° numero: ")
     if re.search(regex_numero, numero_giocato):
        if (int(numero_giocato) not in cinquina_utente and
            int(numero_giocato) >= 1 and
            int(numero_giocato) <= 90):
            cinquina_utente.append(int(numero_giocato))
     if len(cinquina_utente) == 5:
         break
     
# 3. Controllare quanti numeri della cinquina_utente sono presenti nella cinquina_lista
indovinati = 0
for numero in cinquina_utente:
    if numero in cinquina_lista:
        indovinati += 1    # indovinati = indovinati +1
       
if indovinati == 2:
    print("Complimenti, hai fatto AMBO!")
elif indovinati == 3:
    print("Complimenti, hai fatto TERNO!")
elif indovinati == 4:
    print("Complimenti, non è da tutti fare QUATERNA!")
elif indovinati == 5:
    print(termcolor.colored("Sei molto bravo, HAI VINTO!!!", "green"))
else:
    print(termcolor.colored("Sei sfortunato/a, HAI PERSO!", "red"))
    
print(cinquina_lista)
print(cinquina_utente)