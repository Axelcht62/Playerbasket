from tkinter import *



class Joueurs_knicks2(Tk):
    def __init__(self, Interface=None):
        super(Joueurs_knicks2, self).__init__()
        self.title("PlayerBasket")
        self.config(background='#008DDC')
        self.iconbitmap("assets/logo.ico")
        self.geometry("1000x542")
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="Equipe des lakers", bg="#000000", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=420, y=30)

        img1 = PhotoImage(file="assets/Knicks/13759.png").subsample(2)
        img1_user = Label(self, image=img1, bg="#008DDC")
        img1_user.place(x=80, y=100)

        text1_user = Label(self, text="Miles McBride", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text1_user.place(x=100, y=220)

        img2 = PhotoImage(file="assets/Knicks/9598.png").subsample(2)
        img2_user = Label(self, image=img2, bg="#008DDC")
        img2_user.place(x=270, y=105)

        text2_user = Label(self, text="Nerlens Noel", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text2_user.place(x=300, y=240)

        img3 = PhotoImage(file="assets/Knicks/1629011.png").subsample(6)
        img3_user = Label(self, image=img3, bg="#008DDC")
        img3_user.place(x=460, y=110)

        text3_user = Label(self, text="Mitchell Robinson", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text3_user.place(x=480, y=240)

        img4 = PhotoImage(file="assets/Knicks/1629656.png").subsample(6)
        img4_user = Label(self, image=img4, bg="#008DDC")
        img4_user.place(x=650, y=130)

        text4_user = Label(self, text="Quentin Grimes", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text4_user.place(x=660, y=240)

        img5 = PhotoImage(file="assets/Knicks/6495.png").subsample(2)
        img5_user = Label(self, image=img5, bg="#008DDC")
        img5_user.place(x=830, y=130)

        text5_user = Label(self, text="Alec Burks", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text5_user.place(x=860, y=260)



        droit = Label(self, text="© 2022 Playerbasket", bg="#008DDC", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=460, y=510)


        self.mainloop()