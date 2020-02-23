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
    'differentladders': 0,
    'differentsnakes': 0,
    'simtab': [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
}


def genLevel():
    while objects['differentsnakes'] == 0 and objects['differentladders'] == 0:
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
                if np.array_equal(np.isin(np.array(objects['ladders']), np.array(elem)), np.array([True, True])):
                    objects['differentladders'] = 0
                else:
                    print(np.array_equal(np.isin(np.array(objects['ladders']), np.sum([elem, [1, 1]], axis=0)),
                                         np.array([True, True])))
                    print(np.array_equal(np.isin(np.array(objects['ladders']), np.sum([elem, [0, 1]], axis=0)),
                                         np.array([True, True])))
                    print(np.array_equal(np.isin(np.array(objects['ladders']), np.sum([elem, [1, 0]], axis=0)),
                                         np.array([True, True])))
                    print(np.array_equal(np.isin(np.array(objects['ladders']), np.sum([elem, [-1, -1]], axis=0)),
                                         np.array([True, True])))
                    print(np.array_equal(np.isin(np.array(objects['ladders']), np.sum([elem, [0, -1]], axis=0)),
                                         np.array([True, True])))
                    print(np.array_equal(np.isin(np.array(objects['ladders']), np.sum([elem, [-1, 0]], axis=0)),
                                         np.array([True, True])))
                    if np.array(objects['ladders'])[
                        np.isin(np.array(objects['ladders']), np.sum([[1,  - objects['simtab'][elem[1]] + 1], [1,  - objects['simtab'][elem[0]] + 1]], axis=0))].size == 0 and \
                            np.array(objects['ladders'])[
                                np.isin(np.array(objects['ladders']), np.sum([[1,  - objects['simtab'][elem[1]]], [1,  - objects['simtab'][elem[0]] + 1]], axis=0))].size == 0 and \
                            np.array(objects['ladders'])[
                                np.isin(np.array(objects['ladders']), np.sum([[1,  - objects['simtab'][elem[1]] + 1], [1,  - objects['simtab'][elem[0]]]], axis=0))].size == 0 \
                            and np.array(objects['ladders'])[
                            np.isin(np.array(objects['ladders']), np.sum([[1, - objects['simtab'][elem[1]] - 1], [1, - objects['simtab'][elem[0]] - 1]], axis=0))].size == 0 and \
                                    np.array(objects['ladders'])[
                            np.isin(np.array(objects['ladders']), np.sum([[1, - objects['simtab'][elem[1]]], [1, - objects['simtab'][elem[0]] - 1]], axis=0))].size == 0 and \
                                    np.array(objects['ladders'])[
                            np.isin(np.array(objects['ladders']), np.sum([[1, - objects['simtab'][elem[1]] - 1], [1, - objects['simtab'][elem[0]]]], axis=0))].size == 0 \
                            and np.array(objects['ladders'])[
                        np.isin(np.array(objects['ladders']), np.sum([elem, [0, 1]], axis=0))].size == 0 and \
                            np.array(objects['ladders'])[
                                np.isin(np.array(objects['ladders']), np.sum([elem, [1, 0]], axis=0))].size == 0 and \
                            np.array(objects['ladders'])[
                                np.isin(np.array(objects['ladders']), np.sum([elem, [1, 1]], axis=0))].size == 0:
                        objects['differentladders'] = 1

        for elems in objects['snakes']:
            for elem in elems:
                if objects['differentsnakes'] != 1:
                    if np.array_equal(np.isin(np.array(objects['snakes']), np.array(elem)), np.array([True, True])):
                        objects['differentsnakes'] = 0
                    else:
                        if np.array(objects['snakes'])[
                                np.isin(np.array(objects['snakes']), np.sum([elem, [1, 1]], axis=0))].size == 0 and \
                                np.array(objects['snakes'])[
                                    np.isin(np.array(objects['snakes']), np.sum([elem, [0, 1]], axis=0))].size == 0 and \
                                np.array(objects['snakes'])[
                                    np.isin(np.array(objects['snakes']), np.sum([elem, [1, 0]], axis=0))].size == 0 \
                                and np.array(elems)[
                                np.isin(np.array(elems), np.sum([elem, [1, 1]], axis=0))].size != 0 and np.array(elems)[
                                np.isin(np.array(elems), np.sum([elem, [0, 1]], axis=0))].size != 0 and np.array(elems)[
                                np.isin(np.array(elems), np.sum([elem, [1, 0]], axis=0))].size != 0 \
                                and np.array(objects['snakes'])[
                                np.isin(np.array(objects['snakes']), np.sum([elem, [2, 2]], axis=0))].size == 0 and \
                                np.array(objects['snakes'])[
                                    np.isin(np.array(objects['snakes']), np.sum([elem, [2, 0]], axis=0))].size == 0 and \
                                np.array(objects['snakes'])[
                                    np.isin(np.array(objects['snakes']), np.sum([elem, [0, 2]], axis=0))].size == 0 \
                                and np.array(elems)[
                                np.isin(np.array(elems), np.sum([elem, [2, 2]], axis=0))].size != 0 and np.array(elems)[
                                np.isin(np.array(elems), np.sum([elem, [0, 2]], axis=0))].size != 0 and np.array(elems)[
                                np.isin(np.array(elems), np.sum([elem, [2, 0]], axis=0))].size != 0 \
                                and np.array(objects['snakes'])[
                                np.isin(np.array(objects['snakes']), np.sum([elem, [1, 2]], axis=0))].size == 0 and \
                                np.array(objects['snakes'])[
                                    np.isin(np.array(objects['snakes']), np.sum([elem, [2, 1]], axis=0))].size == 0 \
                                and np.array(elems)[
                                np.isin(np.array(elems), np.sum([elem, [1, 2]], axis=0))].size != 0 and np.array(elems)[
                                np.isin(np.array(elems), np.sum([elem, [2, 1]], axis=0))].size != 0:
                            objects['differentladders'] = 1


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
fenetre.geometry("600x600")
Terrain = Canvas(fenetre, height=600, width=600)
Terrain.pack()
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
fenetre.mainloop()
