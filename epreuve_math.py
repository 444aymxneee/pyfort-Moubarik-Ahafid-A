import random
import string
from itertools import repeat

from fonctions_utiles import *

def epreuve_math_factorielle():
    n = random.randint(1, 10)
    reponse = int(input(f"Quelle est la factorielle de {n} ? "))
    facteur = 1
    for i in range(1, n + 1):
        facteur *= i
    if reponse == facteur:
        print("Bonne réponse!")
        return True
    else:
        print(f"Mauvaise réponse! La réponse correcte était {facteur}.")
        return False

def epreuve_math_equation():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x = resoudre_equation_lineaire(a, b)
    response = float(input(f"Résoudre l'équation linèaire {a}x + {b} = 0 : "))
    if response == x:
        print("Bonne réponse!")
        return True
    else:
        print(f"Mauvaise réponse! La réponse correcte était {x}.")
        return False

def epreuve_math_premier():
    n = random.randint(10, 20)
    while est_premier(n):
        n = random.randint(10, 20)
    res = premier_plus_proche(n)
    response = int(input(f"Trouver le nombre premier le plus proche de {n}."))
    if response == res:
        print("Bonne réponse!")
        return True
    else:
        print(f"Mauvaise réponse! La réponse correcte était {res}.")
        return False

def epreuve_roulette_mathematique():
    roulette = []
    for i in range(5):
        roulette.append(random.randint(1, 20))
    print("Nombres sur la roulette : ", roulette)
    operation = random.choice(["addition", "soustraction", "multiplication"])
    resultat = 0
    if operation == "addition":
        resultat = sum(roulette)
    elif operation == "soustraction":
        resultat = sustract(roulette)
    elif operation == "multiplication":
        resultat = multiply(roulette)
    print("Calculez le résultat en combinant ces nombres avec une addition")
    response = int(input("Votre réponse : "))
    if response == resultat:
        print("Bonne réponse!")
        return True
    else:
        print(f"Mauvaise réponse! La réponse correcte était {resultat}.")
        return False


def epreuve_math():
    print("Vous avez choisi une épreuve de mathématiques!")
    rng = random.randint(1, 4)
    if rng == 1:
        epreuve_math_factorielle()
    elif rng == 2:
        epreuve_math_equation()
    elif rng == 3:
        epreuve_math_premier()
    elif rng == 4:
        epreuve_roulette_mathematique()
