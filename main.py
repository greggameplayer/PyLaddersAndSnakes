from tkinter import *
import tkinter.font as tkfont
import random
import math
import numpy as np
import time
import os
try:
    import pypresence
except ImportError:
    os.system("pip3 install -r requirements.txt")
client_id = "686550339578495046"
RPC = pypresence.Presence(client_id)
RPC.connect()


objects = {
    'snakes': [],
    'ladders': [],
    'startLadders': [],
    'endLadders': [],
    'startSnakes': [],
    'endSnakes': [],
    'graphicalLadders': [],
    'simtab': [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    'playerline': [0, 0, 0, 0]
}


def isEquals(elem1, elem2):
    if elem1[0] == elem2[0] and elem1[1] == elem2[1]:
        return True
    else:
        return False


def tabExists(elems, elem, x, y, reverse):
    if reverse:
        tabtemp = [objects['simtab'][elem[0]] + x, elem[1] + y]
    else:
        tabtemp = [elem[0] + x, elem[1] + y]
    if elems == objects['ladders'] or elems == objects['snakes']:
        for elen in elems:
            for el in elen:
                if el[0] == tabtemp[0] and el[1] == tabtemp[1]:
                    return True
        return False
    else:
        for el in elems:
            if el[0] == tabtemp[0] and el[1] == tabtemp[1]:
                return True
        return False


class MAINGAME():
    def __init__(self, PlayerNumber):
        self.playerNumber = PlayerNumber
        self.fenetre = Tk()
        self.fenetre.title("Snakes & Ladders")
        self.fenetre.geometry("800x600")
        self.Terrain = Canvas(self.fenetre, height=600, width=800)
        self.Terrain.pack(anchor='nw')
        self.carreau = [[self.Terrain.create_rectangle(i * 60, j * 60, (i + 1) * 60, (j + 1) * 60, fill="#FFFFFF")
                    for i in range(10)] for j in range(10)]
        self.labels = [[self.Terrain.create_text(i * 60 + 50, j * 60 + 10) for i in range(10)] for j in range(10)]
        self.labels.reverse()
        self.carreau.reverse()
        for i in range(1, 10, 2):
            self.labels[i].reverse()
            self.carreau[i].reverse()
        for i in range(10):
            for j in range(10):
                self.Terrain.itemconfigure(self.labels[i][j], text=(j + 1) + (i * 10))
        self.genLevel()
        self.placeObjects()
        if self.playerNumber == 1:
            self.player = [self.Terrain.create_oval(10, 550, 50, 590, fill="blue", outline='grey')]
        elif self.playerNumber == 2:
            self.player = [self.Terrain.create_oval(4, 560, 24, 580, fill="blue", outline='grey'),
                           self.Terrain.create_oval(36, 560, 56, 580, fill="red", outline='grey')]
        elif self.playerNumber == 3:
            self.player = [self.Terrain.create_oval(14, 560, 24, 570, fill="blue", outline='grey'),
                           self.Terrain.create_oval(36, 560, 46, 570, fill="red", outline='grey'),
                           self.Terrain.create_oval(24, 580, 34, 590, fill="green", outline='grey')]
        else:
            self.player = [self.Terrain.create_oval(14, 560, 24, 570, fill="blue", outline='grey'),
                           self.Terrain.create_oval(36, 560, 46, 570, fill="red", outline='grey'),
                           self.Terrain.create_oval(14, 580, 24, 590, fill="green", outline='grey'),
                           self.Terrain.create_oval(36, 580, 46, 590, fill="yellow", outline='grey')]
        self.playerPositionGap = [[50], [56, 24], [46, 24, 36], [46, 24, 46, 24]]
        self.playerPositionGapY = [[50], [40, 40], [40, 40, 20], [40, 40, 20, 20]]
        self.playerPositionY = [[[550, 590]],
                                [[544, 564],[576, 596]],
                                [[554, 564],[576, 586], [564, 574]],
                                [[554, 564], [576, 586], [554, 564], [576, 586]]]
        self.playerPositionX = [[[10, 50]],
                                [[4, 24], [36, 56]],
                                [[14, 24], [36, 46], [24, 34]],
                                [[14, 24], [36, 46], [14, 24], [36, 46]]]
        self.dice = self.Terrain.create_rectangle(655, 25, 750, 120, fill="white", tags="dice")
        self.dice_face = self.Terrain.create_text(702.5, 72.5, fill="black", font=tkfont.Font(family='Helvetica', size=36, weight='bold'),
                                        tags="dice_face")
        self.playerturnlabel = self.Terrain.create_text(702.5, 130, text="Au tour du joueur 1")
        self.playerturn = 0
        self.Terrain.tag_bind("dice_face", '<Button-1>', self.onDiceClick)
        self.Terrain.tag_bind("dice", "<Button-1>", self.onDiceClick)
        self.fenetre.mainloop()

    def genLevel(self):
        objects['snakes'] = []
        objects['ladders'] = []
        for i in range(random.randint(1, 4)):
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            taille = random.randint(2, 4)
            objects['snakes'].append([[abs(x), y + j] for j in range(taille)])
            for j in range(len(objects['snakes'][i])):
                if j % 2 == 1 and j != 0:
                    objects['snakes'][i][j][0] = objects['simtab'][objects['snakes'][i][j][0]]
        for i in range(random.randint(1, 4)):
            x = random.randint(0, 5)
            y = random.randint(0, 5)
            taille = random.randint(2, 4)
            objects['ladders'].append([[abs(x), y + j] for j in range(taille)])
            for j in range(len(objects['ladders'][i])):
                if j % 2 == 1 and j != 0:
                    objects['ladders'][i][j][0] = objects['simtab'][objects['ladders'][i][j][0]]
        print(objects)
        for elems in objects['ladders']:
            for elem in elems:
                if objects['ladders'].count(elem) > 1:
                    self.genLevel()
                    return
                else:
                    if (tabExists(objects['ladders'], elem, 0, 1, False) and not tabExists(elems, elem, 0, 1, False)) or \
                            (tabExists(objects['ladders'], elem, 1, 0, False) and not tabExists(elems, elem, 1, 0,
                                                                                                False)) or \
                            (tabExists(objects['ladders'], elem, 1, 1, False) and not tabExists(elems, elem, 1, 1,
                                                                                                False)) or \
                            (tabExists(objects['ladders'], elem, 0, -1, False) and not tabExists(elems, elem, 0, -1,
                                                                                                 False)) or \
                            (tabExists(objects['ladders'], elem, -1, 1, False) and not tabExists(elems, elem, -1, 1,
                                                                                                 False)) or \
                            (tabExists(objects['ladders'], elem, 1, -1, False) and not tabExists(elems, elem, 1, -1,
                                                                                                 False)) or \
                            (tabExists(objects['ladders'], elem, -1, 0, False) and not tabExists(elems, elem, -1, 0,
                                                                                                 False)) or \
                            (tabExists(objects['ladders'], elem, -1, -1, False) and not tabExists(elems, elem, -1, -1,
                                                                                                  False)) or \
                            (tabExists(objects['ladders'], elem, 0, 1, True) and not tabExists(elems, elem, 0, 1,
                                                                                               True)) or \
                            (tabExists(objects['ladders'], elem, 1, 0, True) and not tabExists(elems, elem, 1, 0,
                                                                                               True)) or \
                            (tabExists(objects['ladders'], elem, 1, 1, True) and not tabExists(elems, elem, 1, 1,
                                                                                               True)) or \
                            (tabExists(objects['ladders'], elem, 0, -1, True) and not tabExists(elems, elem, 0, -1,
                                                                                                True)) or \
                            (tabExists(objects['ladders'], elem, -1, 1, True) and not tabExists(elems, elem, -1, 1,
                                                                                                True)) or \
                            (tabExists(objects['ladders'], elem, 1, -1, True) and not tabExists(elems, elem, 1, -1,
                                                                                                True)) or \
                            (tabExists(objects['ladders'], elem, -1, 0, True) and not tabExists(elems, elem, -1, 0,
                                                                                                True)) or \
                            (tabExists(objects['ladders'], elem, -1, -1, True) and not tabExists(elems, elem, -1, -1,
                                                                                                 True)):
                        self.genLevel()
                        return

        for elems in objects['snakes']:
            for elem in elems:
                if objects['snakes'].count(elem) > 1:
                    self.genLevel()
                    return
                else:
                    if (tabExists(objects['snakes'], elem, 0, 1, False) and not tabExists(elems, elem, 0, 1, False)) or \
                            (tabExists(objects['snakes'], elem, 1, 0, False) and not tabExists(elems, elem, 1, 0,
                                                                                               False)) or \
                            (tabExists(objects['snakes'], elem, 1, 1, False) and not tabExists(elems, elem, 1, 1,
                                                                                               False)) or \
                            (tabExists(objects['snakes'], elem, 0, -1, False) and not tabExists(elems, elem, 0, -1,
                                                                                                False)) or \
                            (tabExists(objects['snakes'], elem, -1, 1, False) and not tabExists(elems, elem, -1, 1,
                                                                                                False)) or \
                            (tabExists(objects['snakes'], elem, 1, -1, False) and not tabExists(elems, elem, 1, -1,
                                                                                                False)) or \
                            (tabExists(objects['snakes'], elem, -1, 0, False) and not tabExists(elems, elem, -1, 0,
                                                                                                False)) or \
                            (tabExists(objects['snakes'], elem, -1, -1, False) and not tabExists(elems, elem, -1, -1,
                                                                                                 False)) or \
                            (tabExists(objects['snakes'], elem, 0, 1, True) and not tabExists(elems, elem, 0, 1,
                                                                                              True)) or \
                            (tabExists(objects['snakes'], elem, 1, 0, True) and not tabExists(elems, elem, 1, 0,
                                                                                              True)) or \
                            (tabExists(objects['snakes'], elem, 1, 1, True) and not tabExists(elems, elem, 1, 1,
                                                                                              True)) or \
                            (tabExists(objects['snakes'], elem, 0, -1, True) and not tabExists(elems, elem, 0, -1,
                                                                                               True)) or \
                            (tabExists(objects['snakes'], elem, -1, 1, True) and not tabExists(elems, elem, -1, 1,
                                                                                               True)) or \
                            (tabExists(objects['snakes'], elem, 1, -1, True) and not tabExists(elems, elem, 1, -1,
                                                                                               True)) or \
                            (tabExists(objects['snakes'], elem, -1, 0, True) and not tabExists(elems, elem, -1, 0,
                                                                                               True)) or \
                            (tabExists(objects['snakes'], elem, -1, -1, True) and not tabExists(elems, elem, -1, -1,
                                                                                                True)):
                        self.genLevel()
                        return
            for elems in objects['ladders']:
                for elem in elems:
                    for elems2 in objects['snakes']:
                        for elem2 in elems2:
                            if isEquals(elem, elem2):
                                objects['different'] = 1
                                self.genLevel()
                                return

    def placeObjects(self):
        for i in range(len(objects['ladders'])):
            if objects['ladders'][i][0][1] % 2 == 0:
                objects['startLadders'].append(
                    [objects['simtab'][objects['ladders'][i][0][0]], objects['ladders'][i][0][1]])
            else:
                objects['startLadders'].append(objects['ladders'][i][0])
            if objects['ladders'][i][len(objects['ladders'][i]) - 1][1] % 2 == 0:
                objects['endLadders'].append(
                    [objects['simtab'][objects['ladders'][i][len(objects['ladders'][i]) - 1][0]],
                     objects['ladders'][i][len(objects['ladders'][i]) - 1][1]])
            else:
                objects['endLadders'].append(objects['ladders'][i][len(objects['ladders'][i]) - 1])
            for j in range(len(objects['ladders'][i])):
                print(objects['ladders'][i][j][0], objects['ladders'][i][j][1])
                self.Terrain.itemconfigure(self.carreau[objects['ladders'][i][j][1]][objects['ladders'][i][j][0]], fill="green")
        print(objects['startLadders'])
        print(objects['endLadders'])

        for i in range(len(objects['snakes'])):
            if objects['snakes'][i][0][1] % 2 == 0:
                objects['startSnakes'].append(
                    [objects['simtab'][objects['snakes'][i][0][0]], objects['snakes'][i][0][1]])
            else:
                objects['startSnakes'].append(objects['snakes'][i][0])
            if objects['snakes'][i][len(objects['snakes'][i]) - 1][1] % 2 == 0:
                objects['endSnakes'].append([objects['simtab'][objects['snakes'][i][len(objects['snakes'][i]) - 1][0]],
                                             objects['snakes'][i][len(objects['snakes'][i]) - 1][1]])
            else:
                objects['endSnakes'].append(objects['snakes'][i][len(objects['snakes'][i]) - 1])
            for j in range(len(objects['snakes'][i])):
                print(objects['snakes'][i][j][0], objects['snakes'][i][j][1])
                self.Terrain.itemconfigure(self.carreau[objects['snakes'][i][j][1]][objects['snakes'][i][j][0]], fill="red")


    def onDiceClick(self, event):
        rd_dice_face = random.randint(1, 6)
        self.Terrain.itemconfigure(self.dice_face, text=rd_dice_face)
        self.Terrain.tag_unbind("dice_face", '<Button-1>')
        self.Terrain.tag_unbind("dice", "<Button-1>")
        self.moveplayer(rd_dice_face, self.detectPlayerNumbersOnCase())
        time.sleep(0.100)
        self.detectCollision(self.detectPlayerNumbersOnCase())
        if self.playerturn == (len(self.player) - 1):
            self.playerturn = 0
            self.Terrain.itemconfigure(self.playerturnlabel, text="Au tour du joueur 1")
        else:
            self.playerturn += 1
            self.Terrain.itemconfigure(self.playerturnlabel, text=("Au tour du joueur " + str(self.playerturn + 1)))

    def moveplayer(self, rd, playernumbers):
            playerturn = self.playerturn
            cases = 0
            unbind_final = 0
            print(self.Terrain.coords(self.player[playerturn]))
            if objects['playerline'][playerturn] % 2 == 0:
                if self.Terrain.coords(self.player[playerturn])[0] + rd * 60 <= self.playerPositionY[self.playerNumber - 1][playerturn][0] and self.Terrain.coords(self.player[playerturn])[2] + rd * 60 <= self.playerPositionY[self.playerNumber - 1][playerturn][1]:
                    self.Terrain.move(self.player[playerturn], rd * 60, 0)
                else:
                    while self.Terrain.coords(self.player[playerturn])[0] < self.playerPositionY[self.playerNumber - 1][playerturn][0]:
                        self.Terrain.move(self.player[playerturn], 60, 0)
                        cases += 1
                    self.Terrain.move(self.player[playerturn], -(abs(((rd - cases) - 1) * 60)), -60)
                    objects['playerline'][playerturn] += 1
            else:
                if self.Terrain.coords(self.player[playerturn])[1] == self.playerPositionX[self.playerNumber - 1][playerturn][0]:
                    if self.Terrain.coords(self.player[playerturn])[0] - rd * 60 < self.playerPositionX[self.playerNumber - 1][playerturn][0] and self.Terrain.coords(self.player[playerturn])[2] - rd * 60 < self.playerPositionX[self.playerNumber - 1][playerturn][1]:
                        while self.Terrain.coords(self.player[playerturn])[0] > self.playerPositionX[self.playerNumber - 1][playerturn][0]:
                            self.Terrain.move(self.player[playerturn], -60, 0)
                            unbind_final = 1
                    elif self.Terrain.coords(self.player[playerturn])[0] - rd * 60 == self.playerPositionX[self.playerNumber - 1][playerturn][0] and self.Terrain.coords(self.player[playerturn])[2] - rd * 60 == self.playerPositionX[self.playerNumber - 1][playerturn][1]:
                        self.Terrain.move(self.player[playerturn], -(rd * 60), 0)
                        unbind_final = 1
                    else:
                        self.Terrain.move(self.player[playerturn], -(rd * 60), 0)
                else:
                    if self.Terrain.coords(self.player[playerturn])[0] - rd * 60 >= self.playerPositionX[self.playerNumber - 1][playerturn][0] and self.Terrain.coords(self.player[playerturn])[2] - rd * 60 >= self.playerPositionX[self.playerNumber - 1][playerturn][1]:
                        self.Terrain.move(self.player[playerturn], -(rd * 60), 0)
                    else:
                        while self.Terrain.coords(self.player[playerturn])[0] > self.playerPositionX[self.playerNumber - 1][playerturn][0]:
                            self.Terrain.move(self.player[playerturn], -60, 0)
                            cases += 1
                        self.Terrain.move(self.player[playerturn], abs(((rd - cases) - 1) * 60), -60)
                        objects['playerline'][playerturn] += 1
            if unbind_final == 0:
                self.Terrain.tag_bind("dice_face", '<Button-1>', self.onDiceClick)
                self.Terrain.tag_bind("dice", "<Button-1>", self.onDiceClick)

    def detectCollision(self, playernumbers):
            playerturn = self.playerturn
            for i in range(len(objects['endSnakes'])):
                print("----------")
                print(self.Terrain.coords(self.player[playerturn])[0])
                print(600 - ((objects['endSnakes'][i][0] * 60) + self.playerPositionGap[self.playerNumber - 1][playerturn]))
                print("----------------------")
                if int(self.Terrain.coords(self.player[playerturn])[0]) == 600 - ((objects['endSnakes'][i][0] * 60) + self.playerPositionGap[self.playerNumber - 1][playerturn]):
                    if int(self.Terrain.coords(self.player[playerturn])[1]) == 600 - ((objects['endSnakes'][i][1] * 60) + self.playerPositionGapY[self.playerNumber - 1][playerturn]):
                        self.Terrain.move(self.player[playerturn], 0, (600 - ((objects['startSnakes'][i][1] * 60) + self.playerPositionGapY[self.playerNumber - 1][playerturn])) - int(
                            self.Terrain.coords(self.player[playerturn])[1]))
                        objects['playerline'][playerturn] = (int(self.Terrain.coords(self.player[playerturn])[1]) + self.playerPositionGapY[self.playerNumber - 1][playerturn]) / 60
            for i in range(len(objects['startLadders'])):
                print(objects['startLadders'][i])
                print(self.Terrain.coords(self.player[playerturn]))
                if int(self.Terrain.coords(self.player[playerturn])[0]) == 600 - ((objects['startLadders'][i][0] * 60) + self.playerPositionGap[self.playerNumber - 1][playerturn]):
                    if int(self.Terrain.coords(self.player[playerturn])[1]) == 600 - ((objects['startLadders'][i][1] * 60) + self.playerPositionGapY[self.playerNumber - 1][playerturn]):
                        self.Terrain.move(self.player[playerturn], 0, (600 - ((objects['endLadders'][i][1] * 60) + self.playerPositionGapY[self.playerNumber - 1][playerturn])) - int(
                            self.Terrain.coords(self.player[playerturn])[1]))
                        objects['playerline'][playerturn] = (int(self.Terrain.coords(self.player[playerturn])[1]) + self.playerPositionGapY[self.playerNumber - 1][playerturn]) / 60

    def detectPlayerNumbersOnCase(self):
        return "test"


class MAINMENU():
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Snakes & Ladders")
        self.menu.geometry("600x600")
        gameTitle = Label(self.menu, text="Snakes & Ladders", font=tkfont.Font(family='Helvetica', size=36, weight='bold'))
        gameTitle.pack(anchor='n')
        onePlayer = Button(self.menu, text='1 Joueur', font=tkfont.Font(family='Helvetica', size=12, weight='normal'), width=35)
        onePlayer.pack(anchor='n', pady=10)
        twoPlayers = Button(self.menu, text='2 Joueurs', font=tkfont.Font(family='Helvetica', size=12, weight='normal'), width=35)
        twoPlayers.pack(anchor='n', pady=10)
        threePlayers = Button(self.menu, text='3 Joueurs', font=tkfont.Font(family='Helvetica', size=12, weight='normal'), width=35)
        threePlayers.pack(anchor='n', pady=10)
        fourPlayers = Button(self.menu, text='4 Joueurs', font=tkfont.Font(family='Helvetica', size=12, weight='normal'), width=35)
        fourPlayers.pack(anchor='n', pady=10)
        onePlayer.bind('<Button-1>', self.onBtClick)
        twoPlayers.bind('<Button-1>', self.onBtClick)
        threePlayers.bind('<Button-1>', self.onBtClick)
        fourPlayers.bind('<Button-1>', self.onBtClick)
        RPC.update(state="Dans les menus !", large_image="snakes-and-ladders", start=time.time())
        self.menu.mainloop()

    def quit(self):
        self.menu.destroy()

    def onBtClick(self, event):
        if str(event.widget) == '.!button':
            self.quit()
            print(1)
            game = MAINGAME(1)
        elif str(event.widget) == '.!button2':
            self.quit()
            print(2)
            game = MAINGAME(2)
        elif str(event.widget) == '.!button3':
            self.quit()
            print(3)
            game = MAINGAME(3)
        elif str(event.widget) == '.!button4':
            self.quit()
            print(4)
            game = MAINGAME(4)

menu = MAINMENU()