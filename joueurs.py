from tkinter import *
from joueur2 import Joueur2


class Joueurs(Tk):
    def __init__(self, Interface=None):
        super(Joueurs, self).__init__()
        self.title("PlayerBasket")
        self.config(background='#6700A6')
        self.iconbitmap("assets/logo.ico")
        self.geometry("1000x542")
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="Equipe des lakers", bg="#000000", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=420, y=20)

        img1 = PhotoImage(file="assets/OIP.png").subsample(3)
        img1_user=Label(self, image=img1, bg="#6700A6")
        img1_user.place(x=50,y=100)

        text1_user = Label(self, text="Carmelo Antoine", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text1_user.place(x=55, y=220)

        img2 = PhotoImage(file="assets/r8.png").subsample(4)
        img2_user=Label(self, image=img2, bg="#6700A6")
        img2_user.place(x=250,y=105)

        text2_user = Label(self, text="Trevor Ariza", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text2_user.place(x=280, y=220)

        img3 = PhotoImage(file="assets/R9.png").subsample(5)
        img3_user=Label(self, image=img3, bg="#6700A6")
        img3_user.place(x=450,y=110)

        text3_user = Label(self, text="Kent Bazemore", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text3_user.place(x=450, y=220)

        img4 = PhotoImage(file="assets/a2.png").subsample(12)
        img4_user=Label(self, image=img4, bg="#6700A6")
        img4_user.place(x=630,y=110)

        text4_user = Label(self, text="Avery Bradley", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text4_user.place(x=645, y=220)

        img5 = PhotoImage(file="assets/a22.png").subsample(10)
        img5_user=Label(self, image=img5, bg="#6700A6")
        img5_user.place(x=820,y=110)

        text5_user = Label(self, text="Antoine Davis", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text5_user.place(x=835, y=220)

        img6 = PhotoImage(file="assets/l65.png").subsample(3)
        img6_user=Label(self, image=img6, bg="#6700A6")
        img6_user.place(x=50,y=280)

        text6_user = Label(self, text="Wayne Ellington", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text6_user.place(x=60, y=450)

        img7 = PhotoImage(file="assets/a45.png").subsample(6)
        img7_user=Label(self, image=img7, bg="#6700A6")
        img7_user.place(x=250,y=310)

        text7_user = Label(self, text="Talen Horton-Tucker", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text7_user.place(x=245, y=420)

        img8 = PhotoImage(file="assets/jj.png").subsample(11)
        img8_user=Label(self, image=img8, bg="#6700A6")
        img8_user.place(x=450,y=310)

        text8_user = Label(self, text="Dwight Howard", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text8_user.place(x=465, y=440)

        img9 = PhotoImage(file="assets/cc.png").subsample(3)
        img9_user=Label(self, image=img9, bg="#6700A6")
        img9_user.place(x=650,y=310)

        text9_user = Label(self, text="LeBron James", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text9_user.place(x=665, y=440)

        img10 = PhotoImage(file="assets/cv.png").subsample(3)
        img10_user=Label(self, image=img10, bg="#6700A6")
        img10_user.place(x=830,y=325)

        text10_user = Label(self, text=" DeAndre Jordan", bg="#6700A6", fg="#FFFFFF", font=('Roboto', 15))
        text10_user.place(x=830, y=430)

        boutton_page2 = Button(self, text="Pages suivantes", bg="#9E00FF", fg="white", relief=FLAT,
                                    font=('arial', 12), width=20, activebackground="#6700A6", activeforeground="White",
                                   command=lambda: Joueur2(self.destroy()))
        boutton_page2.place(x=400, y=500)

        droit = Label(self, text="© 2022 Playerbasket", bg="#282828", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=460, y=510)





        self.mainloop()
