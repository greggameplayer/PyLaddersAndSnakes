import os
try:
    from PyLaddersAndSnakes.functions import CreatePyPresenceConnection
    from PyLaddersAndSnakes.mainmenu import MAINMENU
except ImportError:
    os.system('py -m pip install pypresence cx_Freeze simpleaudio')
    from PyLaddersAndSnakes.functions import CreatePyPresenceConnection
    from PyLaddersAndSnakes.mainmenu import MAINMENU

pypresence = CreatePyPresenceConnection()
MAINMENU(pypresence)
