import threading
import time
import tkinter.font as tkfont
import tkinter.messagebox as tkmessage
from tkinter import *

from PyLaddersAndSnakes.anim import *


class MAINGAME:
    def __init__(self, PlayerNumber, PlayerNames, PlayerColors, pypresence):
        """
        fonction permettant d'initialiser un objet de la classe MAINGAME représentant
        le jeu principal
        :param PlayerNumber:
        :param PlayerNames:
        :param PlayerColors:
        :param pypresence:
        """
        self.pypresenceRPC = pypresence
        self.playerNumber = PlayerNumber
        self.fenetre = Tk()
        self.fenetre.title("Snakes & Ladders")
        self.fenetre.geometry("800x600")
        try:
            self.fenetre.iconbitmap(
                find_data_file("images/snakes-and-ladders.ico"))
        except TclError:
            tkmessage.showwarning("Attention", "Vous avez supprimé le logo !")
            pass
        self.fenetre.resizable(False, False)
        self.PlayerNames = PlayerNames
        self.win = False
        self.Terrain = Canvas(self.fenetre, height=600, width=800)
        self.Terrain.pack(anchor="nw")
        self.carreau = [[
            self.Terrain.create_rectangle(i * 60,
                                          j * 60, (i + 1) * 60, (j + 1) * 60,
                                          fill="#FFFFFF") for i in range(10)
        ] for j in range(10)]
        self.labels = [[
            self.Terrain.create_text(i * 60 + 50, j * 60 + 10)
            for i in range(10)
        ] for j in range(10)]
        self.labels.reverse()
        self.carreau.reverse()
        for i in range(1, 10, 2):
            self.labels[i].reverse()
            self.carreau[i].reverse()
        for i in range(10):
            for j in range(10):
                self.Terrain.itemconfigure(self.labels[i][j],
                                           text=(j + 1) + (i * 10))
        self.genLevel()
        self.placeObjects()
        if self.playerNumber == 1:
            self.player = [
                self.Terrain.create_oval(10,
                                         550,
                                         50,
                                         590,
                                         fill=PlayerColors[0],
                                         outline="grey")
            ]
            if pypresenceEnabled and self.pypresenceRPC is not None:
                self.pypresenceRPC.update(
                    state="En jeu !",
                    large_image="snakes-and-ladders",
                    start=time.time(),
                    large_text="PyLadders&Snakes",
                    small_image="oneplayer",
                    small_text="Mode 1 joueur !",
                )
        elif self.playerNumber == 2:
            self.player = [
                self.Terrain.create_oval(4,
                                         560,
                                         24,
                                         580,
                                         fill=PlayerColors[0],
                                         outline="grey"),
                self.Terrain.create_oval(36,
                                         560,
                                         56,
                                         580,
                                         fill=PlayerColors[1],
                                         outline="grey"),
            ]
            if pypresenceEnabled and self.pypresenceRPC is not None:
                self.pypresenceRPC.update(
                    state="En jeu !",
                    large_image="snakes-and-ladders",
                    start=time.time(),
                    large_text="PyLadders&Snakes",
                    small_image="twoplayers",
                    small_text="Mode 2 joueurs !",
                )
        elif self.playerNumber == 3:
            self.player = [
                self.Terrain.create_oval(14,
                                         560,
                                         24,
                                         570,
                                         fill=PlayerColors[0],
                                         outline="grey"),
                self.Terrain.create_oval(36,
                                         560,
                                         46,
                                         570,
                                         fill=PlayerColors[1],
                                         outline="grey"),
                self.Terrain.create_oval(24,
                                         580,
                                         34,
                                         590,
                                         fill=PlayerColors[2],
                                         outline="grey"),
            ]
            if pypresenceEnabled and self.pypresenceRPC is not None:
                self.pypresenceRPC.update(
                    state="En jeu !",
                    large_image="snakes-and-ladders",
                    start=time.time(),
                    large_text="PyLadders&Snakes",
                    small_image="threeplayers",
                    small_text="Mode 3 joueurs !",
                )
        else:
            self.player = [
                self.Terrain.create_oval(14,
                                         560,
                                         24,
                                         570,
                                         fill=PlayerColors[0],
                                         outline="grey"),
                self.Terrain.create_oval(36,
                                         560,
                                         46,
                                         570,
                                         fill=PlayerColors[1],
                                         outline="grey"),
                self.Terrain.create_oval(14,
                                         580,
                                         24,
                                         590,
                                         fill=PlayerColors[2],
                                         outline="grey"),
                self.Terrain.create_oval(36,
                                         580,
                                         46,
                                         590,
                                         fill=PlayerColors[3],
                                         outline="grey"),
            ]
            if pypresenceEnabled and self.pypresenceRPC is not None:
                self.pypresenceRPC.update(
                    state="En jeu !",
                    large_image="snakes-and-ladders",
                    start=time.time(),
                    large_text="PyLadders&Snakes",
                    small_image="fourplayers",
                    small_text="Mode 4 joueurs !",
                )
        self.playerPositionGap = [
            [50],
            [56, 24],
            [46, 24,
             36],  # gap entre la position de la case et celle du joueur
            [46, 24, 46, 24],
        ]  # sur l'axe x
        self.playerPositionGapY = [
            [50],
            [40, 40],
            [40, 40,
             20],  # gap entre la position de la case et celle du joueur
            [40, 40, 20, 20],
        ]  # sur l'axe y
        self.playerPositionY = [  # position minimum du joueur sur l'axe Y
            [[550, 590]],  # ou peut aussi être sur le max de l'axe X
            [[544, 564], [576, 596]],
            [[554, 564], [576, 586], [564, 574]],
            [[554, 564], [576, 586], [554, 564], [576, 586]],
        ]
        self.playerPositionX = [  # position minimum du joueur sur l'axe X
            [[10, 50]],  # ou peut aussi être position minimum sur l'axe Y
            [[4, 24], [36, 56]],
            [[14, 24], [36, 46], [24, 34]],
            [[14, 24], [36, 46], [14, 24], [36, 46]],
        ]
        self.playerPositionYMax = [  # position du joueur maximum sur l'axe Y
            [[10, 50]],
            [[20, 40], [20, 40]],
            [[20, 30], [20, 30], [40, 50]],
            [[20, 30], [20, 30], [40, 50], [40, 50]],
        ]
        self.dice = self.Terrain.create_rectangle(655,
                                                  25,
                                                  750,
                                                  120,
                                                  fill="white",
                                                  tags="dice")
        self.dice_face = self.Terrain.create_text(
            702.5,
            72.5,
            fill="black",
            font=tkfont.Font(family="Helvetica", size=36, weight="bold"),
            tags="dice_face",
        )
        self.playerturnlabel = self.Terrain.create_text(
            702.5, 130, text="Au tour de " + str(self.PlayerNames[0]))
        self.playerturn = 0
        self.Terrain.tag_bind("dice_face", "<Button-1>", self.onDiceClick)
        self.Terrain.tag_bind("dice", "<Button-1>", self.onDiceClick)
        self.fenetre.mainloop()

    def genLevel(self):
        """
        fonction permettant de générer le niveau, tous les obstacles dessus
        (échelles et serpents) et de les stocker dans des tableaux
        :return:
        """
        objects["snakes"] = []
        objects["ladders"] = []
        for i in range(random.randint(
                2, 3)):  # génération d'entre 2 et 3 serpents
            x = random.randint(0, 9)
            y = random.randint(0, 5)
            while y == 0 and x == 0 or x == 1:
                x = random.randint(0, 9)
            taille = random.randint(2, 4)
            while y + taille == 9 and x == 0 or x == 1:
                x = random.randint(0, 9)
            objects["snakes"].append([[abs(x), y + j] for j in range(taille)])
            for j in range(len(objects["snakes"][i])):
                if j % 2 == 1 and j != 0:
                    objects["snakes"][i][j][0] = objects["simtab"][
                        objects["snakes"][i][j][0]]
        for i in range(random.randint(
                2, 3)):  # génération d'entre 2 et 3 échelles
            x = random.randint(0, 9)
            y = random.randint(0, 5)
            while y == 0 and x == 0 or x == 1:
                x = random.randint(0, 9)
            taille = random.randint(2, 4)
            while y + taille == 9 and x == 0 or x == 1:
                x = random.randint(0, 9)
            objects["ladders"].append([[abs(x), y + j] for j in range(taille)])
            for j in range(len(objects["ladders"][i])):
                if j % 2 == 1 and j != 0:
                    objects["ladders"][i][j][0] = objects["simtab"][
                        objects["ladders"][i][j][0]]
        # vérification permettant d'interdire
        for elemsLadders in objects["ladders"]:
            for elem in elemsLadders:  # les échelles en direct contact
                if objects["ladders"].count(elem) > 1:  # avec celle testée
                    self.genLevel()
                    return
                else:
                    if ((tabExists(objects["ladders"], elem, 0, 1, False)
                         and not tabExists(elemsLadders, elem, 0, 1, False)) or
                        (tabExists(objects["ladders"], elem, 1, 0, False)
                         and not tabExists(elemsLadders, elem, 1, 0, False)) or
                        (tabExists(objects["ladders"], elem, 1, 1, False)
                         and not tabExists(elemsLadders, elem, 1, 1, False)) or
                        (tabExists(objects["ladders"], elem, 0, -1, False)
                         and not tabExists(elemsLadders, elem, 0, -1, False))
                            or
                        (tabExists(objects["ladders"], elem, -1, 1, False)
                         and not tabExists(elemsLadders, elem, -1, 1, False))
                            or
                        (tabExists(objects["ladders"], elem, 1, -1, False)
                         and not tabExists(elemsLadders, elem, 1, -1, False))
                            or
                        (tabExists(objects["ladders"], elem, -1, 0, False)
                         and not tabExists(elemsLadders, elem, -1, 0, False))
                            or
                        (tabExists(objects["ladders"], elem, -1, -1, False)
                         and not tabExists(elemsLadders, elem, -1, -1, False))
                            or
                        (tabExists(objects["ladders"], elem, 0, 1, True)
                         and not tabExists(elemsLadders, elem, 0, 1, True)) or
                        (tabExists(objects["ladders"], elem, 1, 1, True)
                         and not tabExists(elemsLadders, elem, 1, 1, True)) or
                        (tabExists(objects["ladders"], elem, 0, -1, True)
                         and not tabExists(elemsLadders, elem, 0, -1, True)) or
                        (tabExists(objects["ladders"], elem, -1, 1, True)
                         and not tabExists(elemsLadders, elem, -1, 1, True)) or
                        (tabExists(objects["ladders"], elem, 1, -1, True)
                         and not tabExists(elemsLadders, elem, 1, -1, True)) or
                        (tabExists(objects["ladders"], elem, -1, -1, True)
                         and not tabExists(elemsLadders, elem, -1, -1, True))):
                        self.genLevel()
                        return

        # vérification permettant d'interdire
        for elemsSnakes in objects["snakes"]:
            for elem in elemsSnakes:  # les serpents en direct contact
                if objects["snakes"].count(elem) > 1:  # avec celui testé
                    self.genLevel()
                    return
                else:
                    if ((tabExists(objects["snakes"], elem, 0, 1, False)
                         and not tabExists(elemsSnakes, elem, 0, 1, False)) or
                        (tabExists(objects["snakes"], elem, 1, 0, False)
                         and not tabExists(elemsSnakes, elem, 1, 0, False)) or
                        (tabExists(objects["snakes"], elem, 1, 1, False)
                         and not tabExists(elemsSnakes, elem, 1, 1, False)) or
                        (tabExists(objects["snakes"], elem, 0, -1, False)
                         and not tabExists(elemsSnakes, elem, 0, -1, False)) or
                        (tabExists(objects["snakes"], elem, -1, 1, False)
                         and not tabExists(elemsSnakes, elem, -1, 1, False)) or
                        (tabExists(objects["snakes"], elem, 1, -1, False)
                         and not tabExists(elemsSnakes, elem, 1, -1, False)) or
                        (tabExists(objects["snakes"], elem, -1, 0, False)
                         and not tabExists(elemsSnakes, elem, -1, 0, False)) or
                        (tabExists(objects["snakes"], elem, -1, -1, False)
                         and not tabExists(elemsSnakes, elem, -1, -1, False))
                            or
                        (tabExists(objects["snakes"], elem, 0, 1, True)
                         and not tabExists(elemsSnakes, elem, 0, 1, True)) or
                        (tabExists(objects["snakes"], elem, 1, 1, True)
                         and not tabExists(elemsSnakes, elem, 1, 1, True)) or
                        (tabExists(objects["snakes"], elem, 0, -1, True)
                         and not tabExists(elemsSnakes, elem, 0, -1, True)) or
                        (tabExists(objects["snakes"], elem, -1, 1, True)
                         and not tabExists(elemsSnakes, elem, -1, 1, True)) or
                        (tabExists(objects["snakes"], elem, 1, -1, True)
                         and not tabExists(elemsSnakes, elem, 1, -1, True)) or
                        (tabExists(objects["snakes"], elem, -1, -1, True)
                         and not tabExists(elemsSnakes, elem, -1, -1, True))):
                        self.genLevel()
                        return
            for elems in objects[
                    "ladders"]:  # vérification permettant d'interdire
                for elem in elems:  # le positionnement d'une échelle sur un serpent
                    for elems2 in objects["snakes"]:
                        for elem2 in elems2:
                            if isEquals(elem, elem2):
                                objects["different"] = 1
                                self.genLevel()
                                return

    def placeObjects(self):
        """
        fonction permettant de placer graphiquement les échelles et les serpents
        contenu dans les tableaux placés dans le dictionnaire objects
        :return:
        """
        for i in range(len(objects["ladders"])):  # placement des échelles
            if objects["ladders"][i][0][1] % 2 == 0:
                objects["startLadders"].append([
                    objects["simtab"][objects["ladders"][i][0][0]],
                    objects["ladders"][i][0][1],
                ])
            else:
                objects["startLadders"].append(objects["ladders"][i][0])
            if objects["ladders"][i][len(objects["ladders"][i]) -
                                     1][1] % 2 == 0:
                objects["endLadders"].append([
                    objects["simtab"][objects["ladders"][i][
                        len(objects["ladders"][i]) - 1][0]],
                    objects["ladders"][i][len(objects["ladders"][i]) - 1][1],
                ])
            else:
                objects["endLadders"].append(
                    objects["ladders"][i][len(objects["ladders"][i]) - 1])
            for j in range(len(objects["ladders"][i])):
                self.Terrain.itemconfigure(
                    self.carreau[objects["ladders"][i][j][1]][
                        objects["ladders"][i][j][0]],
                    fill="green",
                )

        for i in range(len(objects["snakes"])):  # placement des serpents
            if objects["snakes"][i][0][1] % 2 == 0:
                objects["startSnakes"].append([
                    objects["simtab"][objects["snakes"][i][0][0]],
                    objects["snakes"][i][0][1],
                ])
            else:
                objects["startSnakes"].append(objects["snakes"][i][0])
            if objects["snakes"][i][len(objects["snakes"][i]) - 1][1] % 2 == 0:
                objects["endSnakes"].append([
                    objects["simtab"][objects["snakes"][i][
                        len(objects["snakes"][i]) - 1][0]],
                    objects["snakes"][i][len(objects["snakes"][i]) - 1][1],
                ])
            else:
                objects["endSnakes"].append(
                    objects["snakes"][i][len(objects["snakes"][i]) - 1])
            for j in range(len(objects["snakes"][i])):
                self.Terrain.itemconfigure(
                    self.carreau[objects["snakes"][i][j][1]][objects["snakes"]
                                                             [i][j][0]],
                    fill="red",
                )

    def onDiceClick(self, _event):
        """
        fonction executé lors de l'appuie sur le dés permettant de le faire tourner
        et donc de générer un nombre aléatoire et de lancer son animation via la
        création d'un objet de la classe ANIM dans un nouveau Thread
        :param _event:
        :return:
        """
        rd_dice_face = random.randint(1, 6)
        self.Terrain.tag_unbind("dice_face", "<Button-1>")
        self.Terrain.tag_unbind("dice", "<Button-1>")
        diceAnim = threading.Thread(target=ANIM,
                                    args=(self, self.dice_face, rd_dice_face))
        diceAnim.start()

    def moveplayer(self, rd):
        """
        fonction executé à la suite de l'animation du dés permettant
        de faire avancer le joueur sur la case en fonction du nombre désigné par le dés
        :param rd:
        :return:
        """
        playerturn = self.playerturn
        cases = 0
        if objects["playerline"][playerturn] % 2 == 0:
            if (self.Terrain.coords(self.player[playerturn])[0] + rd * 60 <=
                    self.playerPositionY[self.playerNumber - 1][playerturn][0]
                    and self.Terrain.coords(self.player[playerturn])[2] +
                    rd * 60 <= self.playerPositionY[self.playerNumber -
                                                    1][playerturn][1]):
                self.Terrain.move(self.player[playerturn], rd * 60, 0)
            else:
                while (self.Terrain.coords(self.player[playerturn])[0] <
                       self.playerPositionY[self.playerNumber -
                                            1][playerturn][0]):
                    self.Terrain.move(self.player[playerturn], 60, 0)
                    cases += 1
                self.Terrain.move(self.player[playerturn], -(abs(
                    ((rd - cases) - 1) * 60)), -60)
                objects["playerline"][playerturn] += 1
        else:
            if (self.Terrain.coords(self.player[playerturn])[1] ==
                    self.playerPositionYMax[self.playerNumber -
                                            1][playerturn][0]):
                if (self.Terrain.coords(self.player[playerturn])[0] - rd * 60 <
                        self.playerPositionYMax[self.playerNumber -
                                                1][playerturn][0]):
                    while (self.Terrain.coords(self.player[playerturn])[0] >
                           self.playerPositionYMax[self.playerNumber -
                                                   1][playerturn][1]):
                        self.Terrain.move(self.player[playerturn], -60, 0)
                        cases += 1
                    self.Terrain.move(self.player[playerturn],
                                      (rd - cases) * 60, 0)
                else:
                    self.Terrain.move(self.player[playerturn], -(rd * 60), 0)
            else:
                if (self.Terrain.coords(self.player[playerturn])[0] - rd * 60
                        >= self.playerPositionX[self.playerNumber -
                                                1][playerturn][0]
                        and self.Terrain.coords(self.player[playerturn])[2] -
                        rd * 60 >= self.playerPositionX[self.playerNumber -
                                                        1][playerturn][1]):
                    self.Terrain.move(self.player[playerturn], -(rd * 60), 0)
                else:
                    while (self.Terrain.coords(self.player[playerturn])[0] >
                           self.playerPositionX[self.playerNumber -
                                                1][playerturn][0]):
                        self.Terrain.move(self.player[playerturn], -60, 0)
                        cases += 1
                    self.Terrain.move(self.player[playerturn],
                                      abs(((rd - cases) - 1) * 60), -60)
                    objects["playerline"][playerturn] += 1
            self.Terrain.tag_bind("dice_face", "<Button-1>", self.onDiceClick)
            self.Terrain.tag_bind("dice", "<Button-1>", self.onDiceClick)

    def detectCollision(self):
        """
        fonction executé à la suite de moveplayer(self, rd) permettant de bouger
        le joueur sur la case de destination du serpent ou de l'échelle si il
        est positionné sur le début de ceux-ci
        :return:
        """
        self.Terrain.tag_unbind("dice_face", "<Button-1>")
        self.Terrain.tag_unbind("dice", "<Button-1>")
        playerturn = self.playerturn
        for i in range(len(objects["endSnakes"])):
            if int(self.Terrain.coords(self.player[playerturn])[0]) == 600 - (
                (objects["endSnakes"][i][0] * 60) +
                    self.playerPositionGap[self.playerNumber - 1][playerturn]):
                if int(self.Terrain.coords(
                        self.player[playerturn])[1]) == 600 - (
                            (objects["endSnakes"][i][1] * 60) +
                            self.playerPositionGapY[self.playerNumber -
                                                    1][playerturn]):
                    wave_obj = sa.WaveObject.from_wave_file(
                        find_data_file("sounds/go_low.wav"))
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
                    self.Terrain.move(
                        self.player[playerturn],
                        0,
                        (600 - ((objects["startSnakes"][i][1] * 60) +
                                self.playerPositionGapY[self.playerNumber -
                                                        1][playerturn])) -
                        int(self.Terrain.coords(self.player[playerturn])[1]),
                    )
                    objects["playerline"][playerturn] = (
                        int(self.Terrain.coords(self.player[playerturn])[1]) +
                        self.playerPositionGapY[self.playerNumber -
                                                1][playerturn]) / 60
        for i in range(len(objects["startLadders"])):
            if int(self.Terrain.coords(self.player[playerturn])[0]) == 600 - (
                (objects["startLadders"][i][0] * 60) +
                    self.playerPositionGap[self.playerNumber - 1][playerturn]):
                if int(self.Terrain.coords(
                        self.player[playerturn])[1]) == 600 - (
                            (objects["startLadders"][i][1] * 60) +
                            self.playerPositionGapY[self.playerNumber -
                                                    1][playerturn]):
                    wave_obj = sa.WaveObject.from_wave_file(
                        find_data_file("sounds/go_up.wav"))
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
                    self.Terrain.move(
                        self.player[playerturn],
                        0,
                        (600 - ((objects["endLadders"][i][1] * 60) +
                                self.playerPositionGapY[self.playerNumber -
                                                        1][playerturn])) -
                        int(self.Terrain.coords(self.player[playerturn])[1]),
                    )
                    objects["playerline"][playerturn] = (
                        int(self.Terrain.coords(self.player[playerturn])[1]) +
                        self.playerPositionGapY[self.playerNumber -
                                                1][playerturn]) / 60
        self.Terrain.tag_bind("dice_face", "<Button-1>", self.onDiceClick)
        self.Terrain.tag_bind("dice", "<Button-1>", self.onDiceClick)

    def detectWin(self):
        """
        fonction executé à la suite de detectCollision(self) permettant de détecter
        si le joueur se trouve sur la dernière case et de lui retourner un message
        de victoire si c'est le cas
        :return:
        """
        if (int(self.Terrain.coords(self.player[self.playerturn])[0]) ==
                self.playerPositionX[self.playerNumber -
                                     1][self.playerturn][0]):
            if (self.Terrain.coords(self.player[self.playerturn])[1] ==
                    self.playerPositionYMax[self.playerNumber -
                                            1][self.playerturn][0]):
                self.Terrain.tag_unbind("dice_face", "<Button-1>")
                self.Terrain.tag_unbind("dice", "<Button-1>")
                self.Terrain.itemconfigure(
                    self.playerturnlabel,
                    fill="green",
                    text=str(self.PlayerNames[self.playerturn]) + " a gagné !",
                )
                self.win = True
                wave_obj_win = sa.WaveObject.from_wave_file(
                    find_data_file("sounds/win.wav"))
                play_obj_win = wave_obj_win.play()
                play_obj_win.wait_done()
