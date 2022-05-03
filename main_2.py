from tkinter import *
from main_3 import Main3
from main_4 import Main4
from main_5 import Main5
from main_6 import Main6



class Main2(Tk):
    def __init__(self, Interface=None):
        super(Main2, self).__init__()
        self.title("PlayerBasket")
        self.config(background='#282828')
        self.iconbitmap("assets/logo.ico")
        self.geometry("1000x542")
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#575757", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="PlayerBasket", bg="#575757", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=400, y=20)

        title_second = Label(self, text="Voici les équipe que vous pouvais consulter !", bg="#282828", fg="#FFFFFF",
                             font=('Roboto', 15))
        title_second.place(x=30, y=100)

        img1 = PhotoImage(file="assets/1200px-Los_Angeles_Lakers_logo.svg.png").subsample(6)
        img1_user = Label(self, image=img1, bg="#282828")
        img1_user.place(x=50, y=160)

        boutton_lakers = Button(self, text="Lakers", bg="#575757", fg="white", relief=FLAT,
                                font=('arial', 10), width=20, activebackground="#575757", activeforeground="White",
                                command=lambda: Main3(self.destroy()))
        boutton_lakers.place(x=65, y=290)

        img2 = PhotoImage(file="assets/images.png").subsample(2)
        img2_user = Label(self, image=img2, bg="#282828")
        img2_user.place(x=350, y=165)

        boutton_chicago = Button(self, text="Chicago Bulls", bg="#575757", fg="white", relief=FLAT,
                                font=('arial', 10), width=20, activebackground="#575757", activeforeground="White",
                                command=lambda: Main4(self.destroy()))
        boutton_chicago.place(x=320, y=290)

        img3 = PhotoImage(file="assets/1200px-Miami_Heat_-_Logo.svg.png").subsample(10)
        img3_user = Label(self, image=img3, bg="#282828")
        img3_user.place(x=570, y=165)

        boutton_heat = Button(self, text="Miami Heat", bg="#575757", fg="white", relief=FLAT,
                                font=('arial', 10), width=20, activebackground="#575757", activeforeground="White",
                              command=lambda: Main5(self.destroy()))
        boutton_heat.place(x=530, y=290)

        img4 = PhotoImage(file="assets/NY_Knicks_Logo_2011.png").subsample(5)
        img4_user = Label(self, image=img4, bg="#282828")
        img4_user.place(x=770, y=165)

        boutton_kneaks = Button(self, text="Knicks", bg="#575757", fg="white", relief=FLAT,
                              font=('arial', 10), width=20, activebackground="#575757", activeforeground="White",
                                command=lambda: Main6(self.destroy()))
        boutton_kneaks.place(x=750, y=290)

        imgprincipale = PhotoImage(file="assets/2527948.png").subsample(6)
        imgprincipale_1 = Label(self, image=imgprincipale, bg="#575757")
        imgprincipale_1.place(x=10, y=0)

        imgsecond = PhotoImage(file="assets/2527948.png").subsample(6)
        imgsecond_2 = Label(self, image=imgsecond, bg="#575757")
        imgsecond_2.place(x=900, y=0)

        droit = Label(self, text="© 2022 Playerbasket", bg="#282828", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=460, y=510)



        self.mainloop()