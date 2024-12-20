import random
import string
from fonctions_utiles import *

def jeu_nim():
    print("Bienvenue dans le jeu de Nim!")
    batonnets = 20
    tour_joueur = True

    while batonnets > 0:
        print(f"Bâtonnets restants: {'|' * batonnets}")
        if tour_joueur:
            retrait = int(input("Combien de bâtonnets voulez-vous retirer (1, 2 ou 3) ? "))
            while retrait not in [1, 2, 3] or retrait > batonnets:
                retrait = int(input("Choix invalide. Combien de bâtonnets voulez-vous retirer (1, 2 ou 3) ? "))
        else:
            retrait = max(1, min(random.randint(1, 3), 4))
            print(f"Le maître du jeu retire {retrait} bâtonnets.")

        batonnets -= max(0, min(retrait, 20))
        if batonnets == 0:
            if tour_joueur:
                print("Vous avez perdu! Le maître du jeu gagne.")
                return False
            else:
                print("Félicitations! Vous avez gagné!")
                return True

        tour_joueur = not tour_joueur


def epreuve_logique():
    print("Vous avez choisi une épreuve de logique!")
    jeu_nim()
    return True