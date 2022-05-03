from tkinter import *
from joueurs_miami2 import Joueurs_miami2


class Joueurs_miami(Tk):
    def __init__(self, Interface=None):
        super(Joueurs_miami, self).__init__()
        self.title("PlayerBasket")
        self.config(background='#880000')
        self.iconbitmap("assets/logo.ico")
        self.geometry("1000x542")
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="Equipe des lakers", bg="#000000", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=420, y=30)

        img1 = PhotoImage(file="assets/Heat-miami/202693.png").subsample(7)
        img1_user=Label(self, image=img1, bg="#880000")
        img1_user.place(x=80,y=100)

        text1_user = Label(self, text="Markieff Morris", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text1_user.place(x=85, y=220)

        img2 = PhotoImage(file="assets/Heat-miami/87a0ba6d09beada1f1de641010685c90f7e15d24.png").subsample(6)
        img2_user=Label(self, image=img2, bg="#880000")
        img2_user.place(x=290, y=105)

        text2_user = Label(self, text="Jimmy Butler", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text2_user.place(x=275, y=240)

        img3 = PhotoImage(file="assets/Heat-miami/1629639.png").subsample(6)
        img3_user=Label(self, image=img3, bg="#880000")
        img3_user.place(x=450,y=110)

        text3_user = Label(self, text="Tyler Herro", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text3_user.place(x=480, y=240)

        img4 = PhotoImage(file="assets/Heat-miami/i.png").subsample(4)
        img4_user=Label(self, image=img4, bg="#880000")
        img4_user.place(x=650,y=130)

        text4_user = Label(self, text="Victor Oladipo", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text4_user.place(x=660, y=240)

        img5 = PhotoImage(file="assets/Heat-miami/1629130.png").subsample(7)
        img5_user=Label(self, image=img5, bg="#880000")
        img5_user.place(x=830,y=130)

        text5_user = Label(self, text="Duncan Robinson", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text5_user.place(x=830, y=240)

        img6 = PhotoImage(file="assets/Heat-miami/Omer_Yurtseven-4.png").subsample(2)
        img6_user=Label(self, image=img6, bg="#880000")
        img6_user.place(x=50,y=300)

        text6_user = Label(self, text="Omer Yurtseven", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text6_user.place(x=65, y=460)

        img7 = PhotoImage(file="assets/Heat-miami/i (1).png").subsample(2)
        img7_user=Label(self, image=img7, bg="#880000")
        img7_user.place(x=250,y=320)

        text7_user = Label(self, text="Dewayne Dedmon", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text7_user.place(x=250, y=460)

        img8 = PhotoImage(file="assets/Heat-miami/kyle-lowry-heat.png").subsample(5)
        img8_user=Label(self, image=img8, bg="#880000")
        img8_user.place(x=460,y=350)

        text8_user = Label(self, text="Kyle Lowry", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text8_user.place(x=485, y=450)

        img9 = PhotoImage(file="assets/Heat-miami/2-7.png").subsample(7)
        img9_user=Label(self, image=img9, bg="#880000")
        img9_user.place(x=650,y=350)

        text9_user = Label(self, text="Udonis Haslem", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text9_user.place(x=660, y=450)

        img10 = PhotoImage(file="assets/Heat-miami/1629216.png").subsample(6)
        img10_user=Label(self, image=img10, bg="#880000")
        img10_user.place(x=830,y=325)

        text10_user = Label(self, text="Gabe Vincent", bg="#880000", fg="#FFFFFF", font=('Roboto', 15))
        text10_user.place(x=850, y=460)

        boutton_page2 = Button(self, text="Pages suivantes", bg="#DC0000", fg="white", relief=FLAT,
                                    font=('arial', 12), width=20, activebackground="#880000", activeforeground="White",
                                   command=lambda: Joueurs_miami2(self.destroy()))
        boutton_page2.place(x=400, y=500)

        droit = Label(self, text="© 2022 Playerbasket", bg="#880000", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=590, y=510)





        self.mainloop()
