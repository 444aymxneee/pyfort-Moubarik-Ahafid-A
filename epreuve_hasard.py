import random
import string
from fonctions_utiles import *

def epreuve_hasard():
    print("Vous avez choisi une épreuve de hasard!")
    choix = random.choice(['A', 'B', 'C'])
    print("Devinez sous quel gobelet (A, B ou C) se cache la clé.")
    for tentative in range(2):
        reponse = input(f"Tentative {tentative + 1}: ").upper()
        if reponse == choix:
            print("Bravo! Vous avez trouvé la clé.")
            return True
    print(f"Dommage! La clé était sous le gobelet {choix}.")
    return False

