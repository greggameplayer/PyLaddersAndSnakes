from PyLaddersAndSnakes.maingame import *
import tkinter.colorchooser as tkcolor


class PLAYERMENU():
    def __init__(self, playerNumber, pypresence):
        self.pypresenceRPC = pypresence
        self.menu = Tk()
        self.menu.title("Snakes & Ladders")
        self.menu.geometry("600x600")
        try:
            self.menu.iconbitmap(find_data_file(
                "images/snakes-and-ladders.ico"))
        except TclError:
            tkmessage.showwarning("Attention", "Vous avez supprimé le logo !")
            pass
        self.menu.configure(background="lightblue")
        self.menu.resizable(False, False)
        self.playerNumber = playerNumber
        self.varColor1 = "blue"
        self.varColor2 = "red"
        self.varColor3 = "green"
        self.varColor4 = "yellow"
        self.varInput = StringVar()
        self.varInput2 = StringVar()
        self.varInput3 = StringVar()
        self.varInput4 = StringVar()

        if self.playerNumber == 1:
            self.label1 = Label(
                self.menu, text="Joueur 1 : ", background="lightblue")
            self.label1.grid(row=0, column=3, pady=20)
            self.entree1 = Entry(
                self.menu, textvariable=self.varInput, width=30)
            self.entree1.grid(row=0, column=4)
            self.color1 = Button(self.menu, background="blue",
                                 width=5, activebackground="blue")
            self.color1.grid(row=0, column=5)
            self.color1.bind('<Button-1>', self.onClickColor)
        elif self.playerNumber == 2:
            self.label1 = Label(
                self.menu, text="Joueur 1 : ", background="lightblue")
            self.label1.grid(row=0, column=3, pady=20)
            self.entree1 = Entry(
                self.menu, textvariable=self.varInput, width=30)
            self.entree1.grid(row=0, column=4)
            self.color1 = Button(self.menu, background="blue",
                                 width=5, activebackground="blue")
            self.color1.grid(row=0, column=5)
            self.label2 = Label(
                self.menu, text="Joueur 2 : ", background="lightblue")
            self.label2.grid(row=1, column=3)
            self.entree2 = Entry(
                self.menu, textvariable=self.varInput2, width=30)
            self.entree2.grid(row=1, column=4, pady=20)
            self.color2 = Button(self.menu, background="red",
                                 width=5, activebackground="red")
            self.color2.grid(row=1, column=5)
            self.color1.bind('<Button-1>', self.onClickColor)
            self.color2.bind('<Button-1>', self.onClickColor)
        elif self.playerNumber == 3:
            self.label1 = Label(
                self.menu, text="Joueur 1 : ", background="lightblue")
            self.label1.grid(row=0, column=3, pady=20)
            self.entree1 = Entry(
                self.menu, textvariable=self.varInput, width=30)
            self.entree1.grid(row=0, column=4, pady=20)
            self.color1 = Button(self.menu, background="blue",
                                 width=5, activebackground="blue")
            self.color1.grid(row=0, column=5)
            self.label2 = Label(
                self.menu, text="Joueur 2 : ", background="lightblue")
            self.label2.grid(row=1, column=3, pady=20)
            self.entree2 = Entry(
                self.menu, textvariable=self.varInput2, width=30)
            self.entree2.grid(row=1, column=4)
            self.color2 = Button(self.menu, background="red",
                                 width=5, activebackground="red")
            self.color2.grid(row=1, column=5)
            self.label3 = Label(
                self.menu, text="Joueur 3 : ", background="lightblue")
            self.label3.grid(row=2, column=3, pady=20)
            self.entree3 = Entry(
                self.menu, textvariable=self.varInput3, width=30)
            self.entree3.grid(row=2, column=4)
            self.color3 = Button(self.menu, background="green",
                                 width=5, activebackground="green")
            self.color3.grid(row=2, column=5)
            self.color1.bind('<Button-1>', self.onClickColor)
            self.color2.bind('<Button-1>', self.onClickColor)
            self.color3.bind('<Button-1>', self.onClickColor)
        else:
            self.label1 = Label(
                self.menu, text="Joueur 1 : ", background="lightblue")
            self.label1.grid(row=0, column=3, pady=20)
            self.entree1 = Entry(
                self.menu, textvariable=self.varInput, width=30)
            self.entree1.grid(row=0, column=4, pady=20)
            self.color1 = Button(self.menu, background="blue",
                                 width=5, activebackground="blue")
            self.color1.grid(row=0, column=5)
            self.label2 = Label(
                self.menu, text="Joueur 2 : ", background="lightblue")
            self.label2.grid(row=1, column=3, pady=20)
            self.entree2 = Entry(
                self.menu, textvariable=self.varInput2, width=30)
            self.entree2.grid(row=1, column=4)
            self.color2 = Button(self.menu, background="red",
                                 width=5, activebackground="red")
            self.color2.grid(row=1, column=5)
            self.label3 = Label(
                self.menu, text="Joueur 3 : ", background="lightblue")
            self.label3.grid(row=2, column=3, pady=20)
            self.entree3 = Entry(
                self.menu, textvariable=self.varInput3, width=30)
            self.entree3.grid(row=2, column=4)
            self.color3 = Button(self.menu, background="green",
                                 width=5, activebackground="green")
            self.color3.grid(row=2, column=5)
            self.label4 = Label(
                self.menu, text="Joueur 4 : ", background="lightblue")
            self.label4.grid(row=3, column=3, pady=20)
            self.entree4 = Entry(
                self.menu, textvariable=self.varInput4, width=30)
            self.entree4.grid(row=3, column=4)
            self.color4 = Button(self.menu, background="yellow",
                                 width=5, activebackground="yellow")
            self.color4.grid(row=3, column=5)
            self.color1.bind('<Button-1>', self.onClickColor)
            self.color2.bind('<Button-1>', self.onClickColor)
            self.color3.bind('<Button-1>', self.onClickColor)
            self.color4.bind('<Button-1>', self.onClickColor)
        self.submit = Button(self.menu, text='Valider', font=tkfont.Font(family='Helvetica', size=12, weight='normal'),
                             width=66, background="lightblue")
        self.submit.bind('<Button-1>', self.onBtClick)
        self.submit.bind("<Enter>", self.onEnter)
        self.submit.bind("<Leave>", self.onLeave)
        self.submit.grid(columnspan=7, row=11, pady=20)
        self.menu.mainloop()

    def quit(self):
        self.menu.destroy()

    def onBtClick(self, event):
        if self.playerNumber == 1 or\
                self.playerNumber == 2 and self.varInput.get() != self.varInput2.get() or\
                self.playerNumber == 3 and self.varInput.get() != self.varInput2.get() and self.varInput.get() != self.varInput3.get() and self.varInput2.get() != self.varInput3.get() or\
                self.playerNumber == 4 and self.varInput.get() != self.varInput2.get() and self.varInput.get() != self.varInput3.get() and self.varInput2.get() != self.varInput3.get() and\
                self.varInput.get() != self.varInput4.get() and self.varInput2.get() != self.varInput4.get() and self.varInput4.get() != self.varInput3.get():

            if self.playerNumber == 1 and "".join(self.varInput.get().split(" ")) != "" or\
                    self.playerNumber == 2 and "".join(self.varInput.get().split(" ")) != "" and "".join(self.varInput2.get().split(" ")) != "" or\
                    self.playerNumber == 3 and "".join(self.varInput.get().split(" ")) != "" and "".join(self.varInput2.get().split(" ")) != "" and "".join(self.varInput3.get().split(" ")) != "" or\
                    self.playerNumber == 4 and "".join(self.varInput.get().split(" ")) != "" and "".join(self.varInput2.get().split(" ")) != "" and "".join(self.varInput3.get().split(" ")) != "" and "".join(self.varInput4.get().split(" ")) != "":

                if self.playerNumber == 1 or\
                        self.playerNumber == 2 and self.color1['background'] != self.color2['background'] or\
                        self.playerNumber == 3 and self.color1['background'] != self.color2['background'] and self.color3['background'] != self.color2['background'] and self.color1['background'] != self.color3['background'] or\
                        self.playerNumber == 4 and self.color1['background'] != self.color2['background'] and self.color3['background'] != self.color2['background'] and self.color1['background'] != self.color3['background'] and\
                        self.color1['background'] != self.color4['background'] and self.color2['background'] != self.color4['background'] and self.color3['background'] != self.color4['background']:

                    self.quit()
                    PlayerNames = [self.varInput.get(), self.varInput2.get(
                    ), self.varInput3.get(), self.varInput4.get()]
                    PlayerColors = [self.varColor1, self.varColor2,
                                    self.varColor3, self.varColor4]
                    game = MAINGAME(self.playerNumber, PlayerNames,
                                    PlayerColors, self.pypresenceRPC)
                else:
                    tkmessage.showerror("Erreur de couleur de joueur",
                                        "Veuillez choisir des couleurs de joueurs différentes !")
            else:
                tkmessage.showerror("Erreur de nom de joueur",
                                    "Veuillez choisir des noms de joueurs !")
        else:
            tkmessage.showerror(
                "Erreur de nom de joueur", "Veuillez choisir des noms de joueurs différents !")

    def onEnter(self, event):
        self.submit['background'] = "cyan"
        self.submit['activebackground'] = "cyan"

    def onLeave(self, event):
        self.submit['background'] = "lightblue"
        self.submit['activebackground'] = "lightblue"

    def onClickColor(self, event):
        if str(event.widget) == '.!button':
            colorchoosen = tkcolor.askcolor()[1]
            self.varColor1 = colorchoosen
            self.color1.configure(background=colorchoosen,
                                  activebackground=colorchoosen)
        elif str(event.widget) == '.!button2':
            colorchoosen = tkcolor.askcolor()[1]
            self.varColor2 = colorchoosen
            self.color2.configure(background=colorchoosen,
                                  activebackground=colorchoosen)
        elif str(event.widget) == '.!button3':
            colorchoosen = tkcolor.askcolor()[1]
            self.varColor3 = colorchoosen
            self.color3.configure(background=colorchoosen,
                                  activebackground=colorchoosen)
        elif str(event.widget) == '.!button4':
            colorchoosen = tkcolor.askcolor()[1]
            self.varColor4 = colorchoosen
            self.color4.configure(background=colorchoosen,
                                  activebackground=colorchoosen)
