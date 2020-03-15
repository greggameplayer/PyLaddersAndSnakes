import random

import simpleaudio as sa

from PyLaddersAndSnakes.functions import *


class ANIM:
    def __init__(self, canvas, dice_face, rd):
        """
        fonction permettant d'initialiser un objet de classe ANIM représentant
        l'animation du dés et permet aussi d'effectuer toutes les fonctions
        pour bouger le joueur, détecter les obstacles et la victoire après
        celle-ci
        :param canvas:
        :param dice_face:
        :param rd:
        """
        wave_obj = sa.WaveObject.from_wave_file(
            find_data_file("sounds/dice.wav"))
        play_obj_dice = wave_obj.play()
        for i in range(random.randint(8, 15)):
            randomint = random.randint(1, 6)
            while randomint == objects["animResult"]:
                randomint = random.randint(1, 6)
            objects["animResult"] = randomint
            canvas.Terrain.after(
                100,
                canvas.Terrain.itemconfigure(dice_face,
                                             text=random.randint(1, 6),
                                             fill="black"),
            )
        objects["animResult"] = 1
        canvas.Terrain.itemconfigure(dice_face, text=rd, fill="red")
        canvas.Terrain.tag_unbind("dice_face", "<Button-1>")
        canvas.Terrain.tag_unbind("dice", "<Button-1>")
        play_obj_dice.wait_done()
        canvas.moveplayer(rd)
        canvas.detectCollision()
        canvas.detectWin()
        if canvas.playerturn == (len(canvas.player) - 1) and not canvas.win:
            canvas.playerturn = 0
            canvas.Terrain.itemconfigure(canvas.playerturnlabel,
                                         text="Au tour de " +
                                         str(canvas.PlayerNames[0]))
        elif not canvas.win:
            canvas.playerturn += 1
            canvas.Terrain.itemconfigure(
                canvas.playerturnlabel,
                text=("Au tour de " +
                      str(canvas.PlayerNames[canvas.playerturn])),
            )
