from tkinter import *


class Joueur2_chicago(Tk):
    def __init__(self, Interface = None):
        super(Joueur2_chicago, self).__init__()
        self.title("Histoires des Lakers")
        self.geometry("1000x542")
        self.iconbitmap("assets/logo.ico")
        self.config(background='#880000')
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="Equipe des lakers", bg="#000000", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=420, y=20)

        img1 = PhotoImage(file="assets/chicago/Troy_Brown_Jr_rebound__cropped_.png").subsample(12)
        img1_user=Label(self, image=img1, bg="#880000")
        img1_user.place(x=200,y=100)

        text1_user = Label(self, text="Troy Brown", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text1_user.place(x=210, y=270)

        img2 = PhotoImage(file="assets/chicago/11439.png").subsample(2)
        img2_user=Label(self, image=img2, bg="#880000")
        img2_user.place(x=400,y=110)

        text2_user = Label(self, text="Tony Bradley", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text2_user.place(x=430, y=240)

        img3 = PhotoImage(file="assets/chicago/12786.png").subsample(2)
        img3_user=Label(self, image=img3, bg="#880000")
        img3_user.place(x=640,y=110)

        text3_user = Label(self, text="Tyler Cook", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text3_user.place(x=685, y=240)


        droit = Label(self, text="© 2022 Playerbasket", bg="#880000", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=420, y=510)


        self.mainloop()