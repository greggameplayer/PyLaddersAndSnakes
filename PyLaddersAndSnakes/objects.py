"""
dictionnaire contenant :
- les serpents
- les échelles
- le début des échelles
- le début des serpents
- la fin des échelles
- la fin des serpents
- une simulation d'un tableau de symétrie
- un tableau contenant la ligne sur laquelle les joueurs sont positionnées
- le nombre sur lequel l'animation du dés est tombé
"""
objects = {
    "snakes": [],
    "ladders": [],
    "startLadders": [],
    "endLadders": [],
    "startSnakes": [],
    "endSnakes": [],
    "simtab": [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    "playerline": [0, 0, 0, 0],
    "animResult": 1,
}
