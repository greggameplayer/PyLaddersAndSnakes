from PyLaddersAndSnakes.playermenu import (
    PLAYERMENU,
    find_data_file,
    tkfont,
    tkmessage,
    Tk,
    TclError,
    Label,
    Button,
    time,
    pypresenceEnabled,
)


class MAINMENU:
    def __init__(self, pypresence):
        """
        fonction permettant d'initialiser un objet de la classe MAINMENU représentant
        le menu principal
        :param pypresence:
        """
        self.pypresenceRPC = pypresence
        self.menu = Tk()
        self.menu.title("PyLadders&Snakes")
        self.menu.geometry("600x600")
        try:
            self.menu.iconbitmap(find_data_file("images/snakes-and-ladders.ico"))
        except TclError:
            tkmessage.showwarning("Attention", "Vous avez supprimé le logo !")
            pass
        self.menu.resizable(False, False)
        gameTitle = Label(
            self.menu,
            text="Snakes & Ladders",
            font=tkfont.Font(family="Helvetica", size=36, weight="bold"),
        )
        gameTitle.pack(anchor="n")
        onePlayer = Button(
            self.menu,
            text="1 Joueur",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=35,
        )
        onePlayer.pack(anchor="n", pady=10)
        twoPlayers = Button(
            self.menu,
            text="2 Joueurs",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=35,
        )
        twoPlayers.pack(anchor="n", pady=10)
        threePlayers = Button(
            self.menu,
            text="3 Joueurs",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=35,
        )
        threePlayers.pack(anchor="n", pady=10)
        fourPlayers = Button(
            self.menu,
            text="4 Joueurs",
            font=tkfont.Font(family="Helvetica", size=12, weight="normal"),
            width=35,
        )
        fourPlayers.pack(anchor="n", pady=10)
        onePlayer.bind("<Button-1>", self.onBtClick)
        twoPlayers.bind("<Button-1>", self.onBtClick)
        threePlayers.bind("<Button-1>", self.onBtClick)
        fourPlayers.bind("<Button-1>", self.onBtClick)
        if pypresenceEnabled and self.pypresenceRPC is not None:
            self.pypresenceRPC.update(
                state="Dans les menus !",
                large_image="snakes-and-ladders",
                start=time.time(),
                large_text="PyLadders&Snakes",
            )
        self.menu.mainloop()

    def quit(self):
        """
        fonction permettant de quitter la fenêtre du menu principal
        :return:
        """
        self.menu.destroy()

    def onBtClick(self, event):
        """
        fonction executé lors de l'appuie sur l'un des boutons pour rediriger vers
        le mode avec le nombre de joueur(s) approprié(s)
        :param event:
        :return:
        """
        if str(event.widget) == ".!button":
            self.quit()
            PLAYERMENU(1, self.pypresenceRPC)
        elif str(event.widget) == ".!button2":
            self.quit()
            PLAYERMENU(2, self.pypresenceRPC)
        elif str(event.widget) == ".!button3":
            self.quit()
            PLAYERMENU(3, self.pypresenceRPC)
        elif str(event.widget) == ".!button4":
            self.quit()
            PLAYERMENU(4, self.pypresenceRPC)
