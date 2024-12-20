import random
import string
from fonctions_utiles import *

def composer_equipe():
    equipe = []
    nombre_joueurs = int(input("Combien de joueurs dans l'équipe (1-3) ? "))
    for i in range(nombre_joueurs):
        nom = input(f"Entrez le nom du joueur {i+1} : ")
        profession = input(f"Quelle est la profession de {nom} ? : ")
        est_leader = input(f"{nom} est-il le leader de l'équipe ? (o/n) : ").lower() == 'o'
        joueur = {
            'nom': nom,
            'profession': profession,
            'leader': est_leader,
            'cles_gagnees': 0
        }
        equipe.append(joueur)

    if not any(j['leader'] for j in equipe):
        equipe[0]['leader'] = True
        print(f"{equipe[0]['nom']} est automatiquement désigné comme leader.")
    return equipe

def menu_epreuves():
    print("Choisissez une épreuve :")
    print("1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve du Hasard")
    print("4. Enigme du Père Fouras")
    return int(input("Votre choix : "))

def choisir_joueur(equipe):
    print("\nVoici les membres de l'équipe :")
    for i, joueur in enumerate(equipe):
        role = "Leader" if joueur['leader'] else "Membre"
        print(f"{i+1}. {joueur['nom']} ({joueur['profession']}) - {role}")
    choix = int(input("Entrez le numéro du joueur choisi : "))
    return equipe[choix - 1]



def est_premier(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        return False
    return True

def premier_plus_proche(n):
    nombresPremiers = [11, 13, 17, 23]
    for i in range(len(nombresPremiers)-1):
        if nombresPremiers[i] < n < nombresPremiers[i + 1]:
            return nombresPremiers[i+1]

def resoudre_equation_lineaire(a, b):
    return -b/a

def multiply(list):
    result = list[0]
    for i in list[1:]:
        result *= list[i]

def sustract(list):
    result = list[0]
    for i in list[1:]:
        result -= list[i]
