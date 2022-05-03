from tkinter import *
from joueurs_kniks2 import Joueurs_knicks2

class Knicks(Tk):
    def __init__(self, Interface=None):
        super(Knicks, self).__init__()
        self.title("PlayerBasket")
        self.config(background='#008DDC')
        self.iconbitmap("assets/logo.ico")
        self.geometry("1000x542")
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="Equipe des lakers", bg="#000000", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=420, y=30)

        img1 = PhotoImage(file="assets/Knicks/4395625.png").subsample(4)
        img1_user = Label(self, image=img1, bg="#008DDC")
        img1_user.place(x=80, y=100)

        text1_user = Label(self, text="R. J. Barrett", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text1_user.place(x=100, y=220)

        img2 = PhotoImage(file="assets/Knicks/images.png").subsample(2)
        img2_user = Label(self, image=img2, bg="#008DDC")
        img2_user.place(x=290, y=125)

        text2_user = Label(self, text="Derrick Rose", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text2_user.place(x=300, y=230)

        img3 = PhotoImage(file="assets/Knicks/6500.png").subsample(2)
        img3_user = Label(self, image=img3, bg="#008DDC")
        img3_user.place(x=460, y=110)

        text3_user = Label(self, text="Kemba Walker", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text3_user.place(x=480, y=240)

        img4 = PhotoImage(file="assets/Knicks/1629656.png").subsample(6)
        img4_user = Label(self, image=img4, bg="#008DDC")
        img4_user.place(x=650, y=130)

        text4_user = Label(self, text="Quentin Grimes", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text4_user.place(x=660, y=240)

        img5 = PhotoImage(file="assets/Knicks/i.png").subsample(4)
        img5_user = Label(self, image=img5, bg="#008DDC")
        img5_user.place(x=830, y=130)

        text5_user = Label(self, text="Ryan Arcidiacono", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text5_user.place(x=830, y=240)

        img6 = PhotoImage(file="assets/Knicks/13533.png").subsample(2)
        img6_user = Label(self, image=img6, bg="#008DDC")
        img6_user.place(x=50, y=300)

        text6_user = Label(self, text="Obi Toppin", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text6_user.place(x=75, y=440)

        img7 = PhotoImage(file="assets/Knicks/1629629.png").subsample(6)
        img7_user = Label(self, image=img7, bg="#008DDC")
        img7_user.place(x=250, y=320)

        text7_user = Label(self, text="Cam Reddish", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text7_user.place(x=275, y=460)

        img8 = PhotoImage(file="assets/Knicks/203944.png").subsample(7)
        img8_user = Label(self, image=img8, bg="#008DDC")
        img8_user.place(x=470, y=340)

        text8_user = Label(self, text="Julius Randle", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text8_user.place(x=485, y=450)

        img9 = PhotoImage(file="assets/Knicks/3371.png").subsample(2)
        img9_user = Label(self, image=img9, bg="#008DDC")
        img9_user.place(x=650, y=320)

        text9_user = Label(self, text="Evan Fournier", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text9_user.place(x=670, y=450)

        img10 = PhotoImage(file="assets/Knicks/6417.png").subsample(6)
        img10_user = Label(self, image=img10, bg="#008DDC")
        img10_user.place(x=830, y=325)

        text10_user = Label(self, text="Immanuel Quickley", bg="#008DDC", fg="#FFFFFF", font=('Roboto', 15))
        text10_user.place(x=830, y=440)

        boutton_page2 = Button(self, text="Pages suivantes", bg="#3190C5", fg="white", relief=FLAT,
                               font=('arial', 12), width=20, activebackground="#008DDC", activeforeground="White",
                               command=lambda: Joueurs_knicks2(self.destroy()))
        boutton_page2.place(x=400, y=500)

        droit = Label(self, text="© 2022 Playerbasket", bg="#008DDC", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=590, y=510)

        self.mainloop()