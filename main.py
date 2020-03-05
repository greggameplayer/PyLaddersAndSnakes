from tkinter import *
import tkinter.font as tkfont
import random
import math
import numpy as np
import time

objects = {
    'snakes': [],
    'ladders': [],
    'startLadders': [],
    'endLadders': [],
    'startSnakes': [],
    'endSnakes': [],
    'graphicalLadders': [],
    'simtab': [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    'playerline': 0
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


def genLevel():
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
                genLevel()
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
                    genLevel()
                    return

    for elems in objects['snakes']:
        for elem in elems:
            if objects['snakes'].count(elem) > 1:
                genLevel()
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
                    genLevel()
                    return
        for elems in objects['ladders']:
            for elem in elems:
                for elems2 in objects['snakes']:
                    for elem2 in elems2:
                        if isEquals(elem, elem2):
                            objects['different'] = 1
                            genLevel()
                            return


def placeObjects():
    for i in range(len(objects['ladders'])):
        if objects['ladders'][i][0][1] % 2 == 0:
            objects['startLadders'].append([objects['simtab'][objects['ladders'][i][0][0]], objects['ladders'][i][0][1]])
        else:
            objects['startLadders'].append(objects['ladders'][i][0])
        if objects['ladders'][i][len(objects['ladders'][i]) - 1][1] % 2 == 0:
            objects['endLadders'].append([objects['simtab'][objects['ladders'][i][len(objects['ladders'][i]) - 1][0]],
                                         objects['ladders'][i][len(objects['ladders'][i]) - 1][1]])
        else:
            objects['endLadders'].append(objects['ladders'][i][len(objects['ladders'][i]) - 1])
        for j in range(len(objects['ladders'][i])):
            print(objects['ladders'][i][j][0], objects['ladders'][i][j][1])
            Terrain.itemconfigure(carreau[objects['ladders'][i][j][1]][objects['ladders'][i][j][0]], fill="green")
    print(objects['startLadders'])
    print(objects['endLadders'])

    for i in range(len(objects['snakes'])):
        if objects['snakes'][i][0][1] % 2 == 0:
            objects['startSnakes'].append([objects['simtab'][objects['snakes'][i][0][0]], objects['snakes'][i][0][1]])
        else:
            objects['startSnakes'].append(objects['snakes'][i][0])
        if objects['snakes'][i][len(objects['snakes'][i]) - 1][1] % 2 == 0:
            objects['endSnakes'].append([objects['simtab'][objects['snakes'][i][len(objects['snakes'][i]) - 1][0]], objects['snakes'][i][len(objects['snakes'][i]) - 1][1]])
        else:
            objects['endSnakes'].append(objects['snakes'][i][len(objects['snakes'][i]) - 1])
        for j in range(len(objects['snakes'][i])):
            print(objects['snakes'][i][j][0], objects['snakes'][i][j][1])
            Terrain.itemconfigure(carreau[objects['snakes'][i][j][1]][objects['snakes'][i][j][0]], fill="red")


def onDiceClick(event):
    rd_dice_face = random.randint(1, 1)
    Terrain.itemconfigure(dice_face, text=rd_dice_face)
    Terrain.tag_unbind("dice_face", '<Button-1>')
    Terrain.tag_unbind("dice", "<Button-1>")
    moveplayer(rd_dice_face)
    time.sleep(0.100)
    detectCollision()


def moveplayer(rd):
    cases = 0
    unbind_final = 0
    print(Terrain.coords(player[0]))
    if objects['playerline'] % 2 == 0:
        if Terrain.coords(player[0])[0] + rd * 60 <= 550 and Terrain.coords(player[0])[2] + rd * 60 <= 590:
            Terrain.move(player[0], rd * 60, 0)
        else:
            while Terrain.coords(player[0])[0] < 550:
                Terrain.move(player[0], 60, 0)
                cases += 1
            Terrain.move(player[0], -(abs(((rd - cases) - 1) * 60)), -60)
            objects['playerline'] += 1
    else:
        if Terrain.coords(player[0])[1] == 10:
            if Terrain.coords(player[0])[0] - rd * 60 < 10 and Terrain.coords(player[0])[2] - rd * 60 < 50:
                while Terrain.coords(player[0])[0] > 10:
                    Terrain.move(player[0], -60, 0)
                    unbind_final = 1
            elif Terrain.coords(player[0])[0] - rd * 60 == 10 and Terrain.coords(player[0])[2] - rd * 60 == 50:
                Terrain.move(player[0], -(rd * 60), 0)
                unbind_final = 1
            else:
                Terrain.move(player[0], -(rd * 60), 0)
        else:
            if Terrain.coords(player[0])[0] - rd * 60 >= 10 and Terrain.coords(player[0])[2] - rd * 60 >= 50:
                Terrain.move(player[0], -(rd * 60), 0)
            else:
                while Terrain.coords(player[0])[0] > 10:
                    Terrain.move(player[0], -60, 0)
                    cases += 1
                Terrain.move(player[0], abs(((rd - cases) - 1) * 60), -60)
                objects['playerline'] += 1
    if unbind_final == 0:
        Terrain.tag_bind("dice_face", '<Button-1>', onDiceClick)
        Terrain.tag_bind("dice", "<Button-1>", onDiceClick)


def detectCollision():
    for i in range(len(objects['endSnakes'])):
        print(objects['endSnakes'])
        print(objects['endSnakes'][i])
        print(objects['startSnakes'])
        print(objects['startSnakes'][i])
        print(Terrain.coords(player[0]))
        if int(Terrain.coords(player[0])[0]) == 600 - ((objects['endSnakes'][i][0] * 60)+50):
                if int(Terrain.coords(player[0])[1]) == 600 - ((objects['endSnakes'][i][1] * 60)+50):
                    Terrain.move(player[0], 0, (600 - ((objects['startSnakes'][i][1] * 60)+50)) - int(Terrain.coords(player[0])[1]))
                    objects['playerline'] = (int(Terrain.coords(player[0])[1])+50)/60
    for i in range(len(objects['startLadders'])):
        print(objects['endLadders'])
        print(objects['endLadders'][i])
        print(objects['startLadders'])
        print(objects['startLadders'][i])
        print(Terrain.coords(player[0]))
        if int(Terrain.coords(player[0])[0]) == 600 - ((objects['startLadders'][i][0] * 60)+50):
                if int(Terrain.coords(player[0])[1]) == 600 - ((objects['startLadders'][i][1] * 60)+50):
                    Terrain.move(player[0], 0, (600 - ((objects['endLadders'][i][1] * 60)+50)) - int(Terrain.coords(player[0])[1]))
                    objects['playerline'] = (int(Terrain.coords(player[0])[1])+50)/60


fenetre = Tk()
fenetre.title("Snakes & ladders")
fenetre.geometry("800x600")
Terrain = Canvas(fenetre, height=600, width=800)
Terrain.pack(anchor='nw')
carreau = [[Terrain.create_rectangle(i * 60, j * 60, (i + 1) * 60, (j + 1) * 60, fill="#FFFFFF")
            for i in range(10)] for j in range(10)]
labels = [[Terrain.create_text(i * 60 + 50, j * 60 + 10) for i in range(10)] for j in range(10)]
labels.reverse()
carreau.reverse()
for i in range(1, 10, 2):
    labels[i].reverse()
    carreau[i].reverse()
for i in range(10):
    for j in range(10):
        Terrain.itemconfigure(labels[i][j], text=(j + 1) + (i * 10))
genLevel()
placeObjects()
player = [Terrain.create_oval(10, 550, 50, 590, fill="blue", outline='')]
dice = Terrain.create_rectangle(655, 25, 750, 120, fill="white", tags="dice")
dice_face = Terrain.create_text(702.5, 72.5, fill="black", font=tkfont.Font(family='Helvetica', size=36, weight='bold'),
                                tags="dice_face")
Terrain.tag_bind("dice_face", '<Button-1>', onDiceClick)
Terrain.tag_bind("dice", "<Button-1>", onDiceClick)
fenetre.mainloop()
