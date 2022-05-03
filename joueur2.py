from tkinter import *


class Joueur2(Tk):
    def __init__(self, Interface = None):
        super(Joueur2, self).__init__()
        self.title("Histoires des Lakers")
        self.geometry("1000x542")
        self.iconbitmap("assets/logo.ico")
        self.config(background='#6700A6')
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="Equipe des lakers", bg="#000000", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=420, y=20)

        img1 = PhotoImage(file="assets/av.png").subsample(3)
        img1_user=Label(self, image=img1, bg="#6700A6")
        img1_user.place(x=50,y=100)

        text1_user = Label(self, text="Malik Monk", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text1_user.place(x=70, y=220)

        img2 = PhotoImage(file="assets/R50.png").subsample(4)
        img2_user=Label(self, image=img2, bg="#6700A6")
        img2_user.place(x=250,y=105)

        text2_user = Label(self, text="Kendrick Nunn", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text2_user.place(x=260, y=220)

        img3 = PhotoImage(file="assets/df.png").subsample(3)
        img3_user=Label(self, image=img3, bg="#6700A6")
        img3_user.place(x=450,y=110)

        text3_user = Label(self, text="Austin Reaves", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text3_user.place(x=465, y=230)

        img4 = PhotoImage(file="assets/qs.png").subsample(3)
        img4_user=Label(self, image=img4, bg="#6700A6")
        img4_user.place(x=630,y=110)

        text4_user = Label(self, text="Rajon Rondo", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text4_user.place(x=650, y=220)

        img5 = PhotoImage(file="assets/az.png").subsample(7)
        img5_user=Label(self, image=img5, bg="#6700A6")
        img5_user.place(x=850,y=110)

        text5_user = Label(self, text="Russell Westbrook", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text5_user.place(x=820, y=250)


        img7 = PhotoImage(file="assets/wx.png").subsample(3)
        img7_user=Label(self, image=img7, bg="#6700A6")
        img7_user.place(x=300,y=310)

        text7_user = Label(self, text="Sekou Doumbouya", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text7_user.place(x=290, y=420)

        img8 = PhotoImage(file="assets/fg.png").subsample(9)
        img8_user=Label(self, image=img8, bg="#6700A6")
        img8_user.place(x=530,y=310)

        text8_user = Label(self, text="Jay Huff", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text8_user.place(x=570, y=430)


        droit = Label(self, text="© 2022 Playerbasket", bg="#6700A6", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=420, y=510)


        self.mainloop()