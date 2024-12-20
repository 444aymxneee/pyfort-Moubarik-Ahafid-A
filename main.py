import random
import string
from enigme_pere_fouras import enigme_pere_fouras
from epreuve_hasard import epreuve_hasard
from epreuve_logique import epreuve_logique
from epreuve_math import epreuve_math
from fonctions_utiles import *

def main():
    print("Bienvenue dans le Fort Boyard Simulator!")

    equipe = composer_equipe()
    cles_gagnees = 0

    while cles_gagnees < 3:
        print("\n--- Nouvelle épreuve ---")
        type_epreuve = menu_epreuves()
        joueur = choisir_joueur(equipe)

        if type_epreuve == 1:
            reussi = epreuve_math()
        elif type_epreuve == 2:
            reussi = epreuve_logique()
        elif type_epreuve == 3:
            reussi = epreuve_hasard()
        elif type_epreuve == 4:
            reussi = enigme_pere_fouras()
        else:
            print("Choix invalide. Passez à une autre épreuve.")
            continue

        if reussi:
            print(f"Bravo {joueur['nom']}! Vous avez gagné une clé!")
            joueur['cles_gagnees'] += 1
            cles_gagnees += 1
        else:
            print(f"Dommage {joueur['nom']}. Essayez une prochaine fois!")



if __name__ == "__main__":
    main()



