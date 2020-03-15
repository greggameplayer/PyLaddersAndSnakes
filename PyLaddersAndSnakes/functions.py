import os
import sys

import pypresence

from PyLaddersAndSnakes.objects import *

pypresenceEnabled = True


def find_data_file(filename):
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
    if elem1[0] == elem2[0] and elem1[1] == elem2[1]:
        return True
    else:
        return False


def tabExists(elems, elem, x, y, reverse):
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
    client_id = "686550339578495046"
    try:
        RPC = pypresence.Presence(client_id)
        RPC.connect()
        pypresenceEnabled = True
        return RPC
    except pypresence.exceptions.InvalidPipe:
        pypresenceEnabled = False
