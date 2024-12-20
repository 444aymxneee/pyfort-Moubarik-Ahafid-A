import random
import string
from fonctions_utiles import *

def epreuve_factorielle():
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

def epreuve_equation_lineaire():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x = -b/a
    response = float(input(f"Résoudre l'équation linèaire {a}x + {b} = 0 ? "))
    if response == x:
        print("Bonne réponse!")
        return True
    else:
        print(f"Mauvaise réponse! La réponse correcte était {x}.")
        return False

def epreuve_math():
    print("Vous avez choisi une épreuve de mathématiques!")
