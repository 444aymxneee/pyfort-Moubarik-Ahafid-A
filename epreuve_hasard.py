import random
import string
from fonctions_utiles import *

def jeu_lance_des():
    print("Vous allez jouer au jeu de lance de dès")
    for tentative in range(3):
        print(f"Tentative {tentative + 1}: ")
        print("Tour du joueur")
        input("Appuyez sur Entrée pour lancer les dès")
        des_joueur = (random.randint(0, 6), random.randint(0, 6))
        print(f"Dès obtenue par le joueur : {des_joueur}")
        if des_joueur[0] == 6 or des_joueur[1] ==6:
            return True
        print("Aucune dès de 6 obtenue. On passe au prochain essai")
        print("Tour du maître du jeu")
        des_maitre = (random.randint(0, 6), random.randint(0, 6))
        print(f"Dès obtenue par le maître du jeu : {des_joueur}")
        if des_maitre[0] == 6 or des_maitre[1] ==6:
            return False
        if tentative != 2:
            print("Aucune dès de 6 obtenue. On passe au prochain essai")
    print("Après trois essais, aucun des joueurs n'a gagné")
    return False


def bonneteau():
    choix = random.choice(['A', 'B', 'C'])
    print("Devinez sous quel gobelet (A, B ou C) se cache la clé.")
    for tentative in range(2):
        reponse = input(f"Tentative {tentative + 1}: ").upper()
        if reponse == choix:
            print("Bravo! Vous avez trouvé la clé.")
            return True
    print(f"Dommage! La clé était sous le gobelet {choix}.")
    return False

def epreuve_hasard():
    print("Vous avez choisi une épreuve de hasard!")
    rng = random.randint(1, 2)
    if rng == 1:
        jeu_lance_des()
    elif rng == 2:
        bonneteau()

