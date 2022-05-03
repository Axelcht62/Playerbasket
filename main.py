from tkinter import *
from main_2 import Main2
from histoires import histoires_lakers

class Interface(Tk):
    def __init__(self):
        super(Interface, self).__init__()
        self.title("PlayerBasket")
        self.config(background='#282828')
        self.iconbitmap("assets/logo.ico")
        self.geometry("1000x542")
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#575757", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="PlayerBasket", bg="#575757", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=400, y=20)

        text_principal = Label(self, text="""
            Bienvenue sur PlayerBasket

            Tu cherche a visionez la biographie des joueurs
            et leur photo sans te casser la tete ?

            Alors PlayerBasket est la
            pour t'aider !
            """, bg="#282828", font=('arial', 17),
                               fg='#fff')
        text_principal.place(x=-50, y=180)
        text_principal["justify"] = CENTER

        boutton_histoires = Button(self, text="Histoires des Lakers", bg="#000000", fg="white", relief=FLAT,
                                   font=('arial', 20), width=20, activebackground="#000000", activeforeground="White",
                                    command = lambda: histoires_lakers(self.destroy()))
        boutton_histoires.place(x=640, y=170)

        boutton_equipe = Button(self, text="Equipe a visualiser", bg="#000000", fg="white", relief=FLAT,
                                font=('arial', 20), width=20, activebackground="#000000", activeforeground="White",
                                command=lambda: Main2(self.destroy()))
        boutton_equipe.place(x=640, y=280)

        boutton_Biographie = Button(self, text="Biographie des joueurs", bg="#000000", fg="white", relief=FLAT,
                                    font=('arial', 20), width=20, activebackground="#000000", activeforeground="White")
        boutton_Biographie.place(x=640, y=390)

        imgprincipale = PhotoImage(file="assets/2527948.png").subsample(6)
        imgprincipale_1 = Label(self, image=imgprincipale, bg="#575757")
        imgprincipale_1.place(x=10, y=0)

        imgsecond = PhotoImage(file="assets/2527948.png").subsample(6)
        imgsecond_2 = Label(self, image=imgsecond, bg="#575757")
        imgsecond_2.place(x=900, y=0)

        droit = Label(self, text="© 2022 Playerbasket", bg="#282828", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=460, y=510)

        self.mainloop()
Interface()