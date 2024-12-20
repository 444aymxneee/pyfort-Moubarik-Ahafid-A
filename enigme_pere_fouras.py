import random
import string
from fonctions_utiles import *
import json

with open("enigmesPF.json", "r", encoding='utf-8') as f:
    enigmes = json.load(f)


def enigme_pere_fouras():
    print("Vous affrontez le Père Fouras!")
    enigme = random.choice(enigmes)
    enigmes.remove(enigme)
    print("Énigme: {}".format(enigme["question"]))
    for tentative in range(3):
        reponse = input(f"Réponse (tentative {tentative + 1}/3) : ").capitalize()
        if str.lower(reponse) == enigme["reponse"]:
            print("Bonne réponse! Vous avez gagné une clé.")
            return True
    print(f"Dommage! La réponse correcte était {enigme['reponse']}.")
    return False