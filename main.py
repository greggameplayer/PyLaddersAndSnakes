from tkinter import *
import random
import math
import numpy as np

objects = {
    'snakes': [],
    'ladders': [],
    'startLadders': [],
    'endLadders': [],
    'startSnakes': [],
    'endSnakes': [],
    'graphicalLadders': [],
    'simtab': [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
}


def isEquals(elem1, elem2):
    if elem1[0] == elem2[0] and elem1[1] == elem2[1]:
        return True
    else:
        return False


def tabExists(elems, elem, x, y, reverse):
    if reverse:
        tabtemp = [objects['simtab'][elem[0]] + x, objects['simtab'][elem[1]] + y]
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
                if (tabExists(objects['ladders'], elem, 0, 1, False) and not tabExists(elems, elem, 0, 1, False)) or\
                        (tabExists(objects['ladders'], elem, 1, 0, False) and not tabExists(elems, elem, 1, 0, False)) or\
                        (tabExists(objects['ladders'], elem, 1, 1, False) and not tabExists(elems, elem, 1, 1, False)) or\
                        (tabExists(objects['ladders'], elem, 0, -1, False) and not tabExists(elems, elem, 0, -1, False)) or\
                        (tabExists(objects['ladders'], elem, -1, 1, False) and not tabExists(elems, elem, -1, 1, False)) or\
                        (tabExists(objects['ladders'], elem, 1, -1, False) and not tabExists(elems, elem, 1, -1, False)) or\
                        (tabExists(objects['ladders'], elem, -1, 0, False) and not tabExists(elems, elem, -1, 0, False)) or\
                        (tabExists(objects['ladders'], elem, -1, -1, False) and not tabExists(elems, elem, -1, -1, False)) or \
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
        objects['startLadders'].append(objects['ladders'][i][0])
        objects['endLadders'].append(objects['ladders'][i][len(objects['ladders'][i]) - 1])
        for j in range(len(objects['ladders'][i])):
            print(objects['ladders'][i][j][0], objects['ladders'][i][j][1])
            Terrain.itemconfigure(carreau[objects['ladders'][i][j][1]][objects['ladders'][i][j][0]], fill="green")
    print(objects['startLadders'])
    print(objects['endLadders'])

    for i in range(len(objects['snakes'])):
        objects['startSnakes'].append(objects['snakes'][i][0])
        objects['endSnakes'].append(objects['snakes'][i][len(objects['snakes'][i]) - 1])
        for j in range(len(objects['snakes'][i])):
            print(objects['snakes'][i][j][0], objects['snakes'][i][j][1])
            Terrain.itemconfigure(carreau[objects['snakes'][i][j][1]][objects['snakes'][i][j][0]], fill="red")


fenetre = Tk()
fenetre.title("Snakes & ladders")
fenetre.geometry("800x600")
Terrain = Canvas(fenetre, height=600, width=600)
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
fenetre.mainloop()
