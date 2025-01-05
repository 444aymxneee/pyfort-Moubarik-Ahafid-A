import json
import random


def epreuve_finale():
    jeu_tv = {}
    with open('indicesSalle.json', 'r', encoding='utf-8') as file:
        jeu_tv = json.load(file)
    annee = random.choice(list(jeu_tv["Fort Boyard"].keys()))
    emission = random.choice(list(jeu_tv["Fort Boyard"][annee].keys()))
    indices = jeu_tv["Fort Boyard"][annee][emission]["Indices"]
    mot_code = jeu_tv["Fort Boyard"][annee][emission]["MOT-CODE"]
    essais = 3
    reponse_correcte = False
    indices_affichés = 3
    while essais > 0 and not reponse_correcte:
        print("Indices disponibles :", indices[:indices_affichés])
        reponse = input("Entrez votre réponse : ")
        if reponse == mot_code:
            reponse_correcte = True
        else:
            essais -= 1
            indices_affichés += 1
            if essais > 0:
                print(f"Il vous reste {essais} essai(s).")
            else:
                print("Indice supplémentaire : ", indices[-1])

    if reponse_correcte:
        print("Bravo, vous avez gagné !")
    else:
        print(f"Échec. Le mot-code était : {mot_code}")

