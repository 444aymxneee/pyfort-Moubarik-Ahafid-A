import random
import string
from fonctions_utiles import *

def enigme_pere_fouras():
    print("Vous affrontez le Père Fouras!")
    enigmes = [
        {"question": "Je suis une lettre. Si vous me mettez à l'envers, je reste la même. Qui suis-je ?", "reponse": ["h", "i", "x"]},
        {"question": "Je peux être longue ou courte. Je suis une unité de temps. Qui suis-je ?", "reponse": ["seconde"]},
        {"question": "Je suis une clé qui n'ouvre aucune porte. Qui suis-je ?", "reponse": ["clé de sol"]},
        {"question": "Je suis toujours devant toi, mais tu ne peux jamais m’atteindre. Qui suis-je ?", "reponse": ["futur"]},
        {"question": "Plus je suis grand, moins on me voit. Qui suis-je ?", "reponse": ["obscurité", "nuit"]},
        {"question": "Je commence la nuit et termine le matin. Qui suis-je ?", "reponse": ["n"]},
        {"question": "Je traverse les villes et les champs, mais je ne bouge jamais. Qui suis-je ?", "reponse": ["route", "chemin"]},
        {"question": "Je peux voler sans ailes, pleurer sans yeux. Qui suis-je ?", "reponse": ["nuage"]},
        {"question": "Je suis une question à laquelle on ne peut jamais répondre par 'oui'. Qui suis-je ?", "reponse": ["es-tu endormi ?"]},
        {"question": "Je peux te transporter partout, mais je ne bouge jamais. Qui suis-je ?", "reponse": ["carte", "plan"]},
        {"question": "Je suis une maison sans porte ni fenêtre. Qui suis-je ?", "reponse": ["igloo", "escargot"]},
        {"question": "Je suis prisé par les marins, mais je les rends parfois malades. Qui suis-je ?", "reponse": ["mer"]},
        {"question": "Je suis léger comme une plume, mais même l'homme le plus fort ne peut me tenir très longtemps. Qui suis-je ?", "reponse": ["souffle"]},
        {"question": "Je commence par 'e', je termine par 'e', mais je ne contiens qu'une seule lettre. Qui suis-je ?", "reponse": ["enveloppe"]},
        {"question": "Plus j’ai d’yeux, moins je vois. Qui suis-je ?", "reponse": ["dés"]},
        {"question": "On me trouve au milieu de Paris. Qui suis-je ?", "reponse": ["r"]},
        {"question": "Je suis plein de trous, mais je retiens l’eau. Qui suis-je ?", "reponse": ["éponge"]},
        {"question": "Je ne peux pas parler, mais je réponds quand on m'appelle. Qui suis-je ?", "reponse": ["écho"]},
        {"question": "Je suis un mot de quatre lettres, mais je deviens plus court si vous m’ajoutez deux lettres. Qui suis-je ?", "reponse": ["court"]},
        {"question": "Je suis un chiffre qui, multiplié par lui-même, donne lui-même. Qui suis-je ?", "reponse": ["0", "1"]},
        {"question": "Je suis là où se rencontrent le ciel et la mer, mais je ne suis jamais vraiment là. Qui suis-je ?", "reponse": ["horizon"]},
        {"question": "Je suis un animal qui marche à quatre pattes le matin, à deux le midi, et à trois le soir. Qui suis-je ?", "reponse": ["homme"]},
        {"question": "Je peux être cassée sans être touchée. Qui suis-je ?", "reponse": ["promesse"]},
        {"question": "Je rétrécis à chaque fois que je prends un bain. Qui suis-je ?", "reponse": ["savon"]},
        {"question": "Je suis plus grand que la tour eiffel, mais je ne pèse rien. Qui suis-je ?", "reponse": ["ombre"]},
        {"question": "J’ai une tête, une queue, mais pas de corps. Qui suis-je ?", "reponse": ["pièce", "monnaie"]},
        {"question": "Je passe mon temps à courir, mais je ne vais nulle part. Qui suis-je ?", "reponse": ["horloge", "temps"]},
        {"question": "Plus je suis chaude, plus je suis petite. Qui suis-je ?", "reponse": ["bougie"]},
        {"question": "Je suis invisible, mais tout le monde peut me sentir. Qui suis-je ?", "reponse": ["vent"]},
        {"question": "Je suis partout, mais on ne peut jamais me voir. Qui suis-je ?", "reponse": ["air"]},
        {"question": "Je n’ai pas de vie, mais je peux mourir. Qui suis-je ?", "reponse": ["batterie"]},
        {"question": "Plus on en retire, plus je deviens grand. Qui suis-je ?", "reponse": ["trou"]},
        {"question": "Je suis une chose que plus on en a, plus on en cherche. Qui suis-je ?", "reponse": ["argent"]},
        {"question": "Je suis un aliment que l’on jette quand on en a besoin, mais que l’on ramasse quand on n’en a plus. Qui suis-je ?", "reponse": ["ancre"]},
        {"question": "Je n’ai ni ailes ni moteur, mais je peux voler. Qui suis-je ?", "reponse": ["cerf-volant"]},
        {"question": "Je n’ai qu’une seule couleur, mais je peux absorber toute la lumière. Qui suis-je ?", "reponse": ["noir"]},
        {"question": "Je n’ai pas de poids, mais je peux te faire tomber. Qui suis-je ?", "reponse": ["fatigue"]},
        {"question": "Je suis doux, mais je peux tuer. Qui suis-je ?", "reponse": ["silence"]},
        {"question": "Je suis un endroit où hier suit aujourd'hui et demain précède aujourd'hui. Qui suis-je ?", "reponse": ["dictionnaire"]},
        {"question": "Je suis là où commence la vie, mais je ne bouge jamais. Qui suis-je ?", "reponse": ["origine"]},
        {"question": "Je suis une question sans réponse. Qui suis-je ?", "reponse": ["mystère"]},
        {"question": "Je peux remplir une pièce sans y entrer. Qui suis-je ?", "reponse": ["lumière"]},
        {"question": "Je grandis quand on me nourrit, mais je meurs quand on me donne à boire. Qui suis-je ?", "reponse": ["feu"]},
        {"question": "Je suis aussi vieille que le monde, mais je n'ai qu'un mois. Qui suis-je ?", "reponse": ["lune"]},
        {"question": "Je me brise sans bruit, mais je ne peux pas être réparée. Qui suis-je ?", "reponse": ["cœur"]},
        {"question": "Je suis un outil qui n’est utile que lorsqu’il est brisé. Qui suis-je ?", "reponse": ["œuf"]},
        {"question": "Je suis une rivière sans eau. Qui suis-je ?", "reponse": ["carte"]},
        {"question": "Je suis une lumière, mais je ne brille que dans l'obscurité. Qui suis-je ?", "reponse": ["étoile"]},
        {"question": "Je suis quelque chose qui peut être cassé avant même d’être utilisé. Qui suis-je ?", "reponse": ["œuf"]},
        {"question": "Je suis un chiffre qui disparaît quand on le divise par lui-même. Qui suis-je ?", "reponse": ["0"]},
        {"question": "Je suis un mois qui a 28 jours. Qui suis-je ?", "reponse": ["tous"]},
        {"question": "Je suis une salle dans laquelle il n’y a jamais de meubles. Qui suis-je ?", "reponse": ["salle de bain"]},
        {"question": "Je suis un animal sans os ni sang, mais qui est toujours vivant. Qui suis-je ?", "reponse": ["corail"]},
        {"question": "Je ne parle jamais, mais je te réponds toujours. Qui suis-je ?", "reponse": ["écho"]},
        {"question": "Je suis un transport sans roue ni moteur, mais je vais dans les airs. Qui suis-je ?", "reponse": ["montgolfière"]},
        {"question": "Je suis quelque chose que tu vois le plus tôt dans la journée, mais jamais la nuit. Qui suis-je ?", "reponse": ["soleil"]},
        {"question": "Je suis là quand tu pleures, mais je ne peux pas parler. Qui suis-je ?", "reponse": ["larme"]},
        {"question": "Je ne tombe jamais, mais je coule chaque jour. Qui suis-je ?", "reponse": ["temps"]},
        {"question": "Je suis une prison où il n’y a ni barreaux ni gardiens. Qui suis-je ?", "reponse": ["esprit"]},
        {"question": "Je peux être fait de bois, de métal ou de verre. Mais je ne bouge jamais. Qui suis-je ?", "reponse": ["table"]}
    ]

    enigme = random.choice(enigmes)
    enigmes.remove(enigme)
    print(f"Énigme: {enigme['question']}")
    for tentative in range(3):
        reponse = input(f"Réponse (tentative {tentative + 1}/3) : ").capitalize()
        if str.lower(reponse) in enigme['reponse']:
            print("Bonne réponse! Vous avez gagné une clé.")
            return True
    print(f"Dommage! La réponse correcte était {enigme['reponse']}.")
    return False