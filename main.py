from tkinter import *
import random
objects = {
    'snakes': [],
    'ladders': []
}


def genLevel():
    for i in range(random.randint(1, 6)):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        taille = random.randint(2, 4)
        objects['snakes'].append([[abs(x + random.randint(-1, 2)), y + j] for j in range(taille)])
    for i in range(random.randint(1, 6)):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        taille = random.randint(2, 4)
        objects['ladders'].append([[abs(x+random.randint(-1, 2)), y+j] for j in range(taille)])
    print(objects)


def placeObjects():
    endladder = 0


fenetre = Tk()
fenetre.title("Snakes & ladders")
fenetre.geometry("600x600")
Terrain = Canvas(fenetre, height=600, width=600)
Terrain.pack()
carreau = [[Terrain.create_rectangle(i * 60, j * 60, (i + 1) * 60, (j + 1) * 60, fill="#FFFFFF")
            for i in range(10)] for j in range(10)]
labels = [[Terrain.create_text(i * 60 + 50, j * 60 + 10) for i in range(10)] for j in range(10)]
labels.reverse()
for i in range(1, 10, 2):
    labels[i].reverse()
for i in range(10):
    for j in range(10):
        Terrain.itemconfigure(labels[i][j], text=(j + 1) + (i * 10))
genLevel()
placeObjects()
fenetre.mainloop()
