import os
import sys

import pypresence

from PyLaddersAndSnakes.objects import *

pypresenceEnabled = True


def find_data_file(filename):
    """
    utilisé pour trouver le chemin du dossier resources
    :param filename:
    :return:
    """
    if getattr(sys, "frozen", False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
        return os.path.join(datadir, "resources/" + filename)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)
        return os.path.join(datadir, "../resources/" + filename)


def isEquals(elem1, elem2):
    """
    utilisé pour tester si un élément est égal à un autre élément de tableau
    (un élément est composé comme ceci : [x, y])
    :param elem1:
    :param elem2:
    :return:
    """
    if elem1[0] == elem2[0] and elem1[1] == elem2[1]:
        return True
    else:
        return False


def tabExists(elems, elem, x, y, reverse):
    """
    utilisé pour tester si un élément de tableau avec plus ou moins de hauteur
    et/ou de longueur, inversé ou pas se trouve dans elems
    (un élément est composé comme ceci : [x, y])
    :param elems:
    :param elem:
    :param x:
    :param y:
    :param reverse:
    :return:
    """
    if reverse:
        tabtemp = [objects["simtab"][elem[0]] + x, elem[1] + y]
    else:
        tabtemp = [elem[0] + x, elem[1] + y]
    if elems == objects["ladders"] or elems == objects["snakes"]:
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


def CreatePyPresenceConnection():
    """
    utilisé pour créer une connexion discord rich presence si votre application
    discord est ouverte
    :return:
    """
    client_id = "686550339578495046"
    try:
        RPC = pypresence.Presence(client_id)
        RPC.connect()
        pypresenceEnabled = True
        return RPC
    except pypresence.exceptions.InvalidPipe:
        pypresenceEnabled = False
