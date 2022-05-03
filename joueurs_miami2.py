from tkinter import *



class Joueurs_miami2(Tk):
    def __init__(self, Interface=None):
        super(Joueurs_miami2, self).__init__()
        self.title("PlayerBasket")
        self.config(background='#880000')
        self.iconbitmap("assets/logo.ico")
        self.geometry("1000x542")
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="Equipe des lakers", bg="#000000", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=420, y=30)

        img1 = PhotoImage(file="assets/Heat-miami/12769.png").subsample(2)
        img1_user=Label(self, image=img1, bg="#880000")
        img1_user.place(x=170,y=100)

        text10_user = Label(self, text="Caleb Martin", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text10_user.place(x=210, y=230)

        img3 = PhotoImage(file="assets/Heat-miami/1628389.png").subsample(7)
        img3_user = Label(self, image=img3, bg="#880000")
        img3_user.place(x=440, y=120)

        text3_user = Label(self, text="Bam Adebayo", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text3_user.place(x=450, y=230)

        img4 = PhotoImage(file="assets/Heat-miami/960x0.png").subsample(12)
        img4_user = Label(self, image=img4, bg="#880000")
        img4_user.place(x=690, y=130)

        text4_user = Label(self, text="P.J.Tucker", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text4_user.place(x=680, y=240)

        droit = Label(self, text="© 2022 Playerbasket", bg="#880000", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=460, y=510)


        self.mainloop()