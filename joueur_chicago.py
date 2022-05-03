from tkinter import *
from joueur_chicago2 import Joueur2_chicago


class Joueurs_chiaco(Tk):
    def __init__(self, Interface=None):
        super(Joueurs_chiaco, self).__init__()
        self.title("PlayerBasket")
        self.config(background='#880000')
        self.iconbitmap("assets/logo.ico")
        self.geometry("1000x542")
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="Equipe des lakers", bg="#000000", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=420, y=20)

        img1 = PhotoImage(file="assets/chicago/Matt_Thomas.png").subsample(14)
        img1_user=Label(self, image=img1, bg="#880000")
        img1_user.place(x=80,y=100)

        text1_user = Label(self, text="Matt Thomas", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text1_user.place(x=70, y=220)

        img2 = PhotoImage(file="assets/chicago/11024.png").subsample(2)
        img2_user=Label(self, image=img2, bg="#880000")
        img2_user.place(x=250,y=105)

        text2_user = Label(self, text="Derrick Jones Jr.", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text2_user.place(x=260, y=220)

        img3 = PhotoImage(file="assets/chicago/lonzo.png").subsample(5)
        img3_user=Label(self, image=img3, bg="#880000")
        img3_user.place(x=450,y=110)

        text3_user = Label(self, text="Lonzo Ball", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text3_user.place(x=480, y=230)

        img4 = PhotoImage(file="assets/chicago/202696.png").subsample(7)
        img4_user=Label(self, image=img4, bg="#880000")
        img4_user.place(x=640,y=110)

        text4_user = Label(self, text="Nikola Vucevic", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text4_user.place(x=645, y=220)

        img5 = PhotoImage(file="assets/chicago/11383.png").subsample(2)
        img5_user=Label(self, image=img5, bg="#880000")
        img5_user.place(x=820,y=105)

        text5_user = Label(self, text="Alex Caruso", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text5_user.place(x=850, y=240)

        img6 = PhotoImage(file="assets/chicago/13535.png").subsample(2)
        img6_user=Label(self, image=img6, bg="#880000")
        img6_user.place(x=50,y=300)

        text6_user = Label(self, text="Patrick Williams", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text6_user.place(x=60, y=430)

        img7 = PhotoImage(file="assets/chicago/203897.png").subsample(6)
        img7_user=Label(self, image=img7, bg="#880000")
        img7_user.place(x=250,y=310)

        text7_user = Label(self, text="Zach LaVine", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text7_user.place(x=285, y=440)

        img8 = PhotoImage(file="assets/chicago/201942.png").subsample(6)
        img8_user=Label(self, image=img8, bg="#880000")
        img8_user.place(x=450,y=310)

        text8_user = Label(self, text="DeMar DeRozan", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text8_user.place(x=465, y=440)

        img9 = PhotoImage(file="assets/chicago/12262.png").subsample(2)
        img9_user=Label(self, image=img9, bg="#880000")
        img9_user.place(x=650,y=310)

        text9_user = Label(self, text="Javonte Green", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text9_user.place(x=665, y=440)

        img10 = PhotoImage(file="assets/chicago/1629632.png").subsample(6)
        img10_user=Label(self, image=img10, bg="#880000")
        img10_user.place(x=830,y=325)

        text10_user = Label(self, text="Coby White", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text10_user.place(x=860, y=460)

        boutton_page2 = Button(self, text="Pages suivantes", bg="#DC0000", fg="white", relief=FLAT,
                                    font=('arial', 12), width=20, activebackground="#880000", activeforeground="White",
                                   command=lambda: Joueur2_chicago(self.destroy()))
        boutton_page2.place(x=400, y=500)

        droit = Label(self, text="© 2022 Playerbasket", bg="#282828", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=460, y=510)





        self.mainloop()
