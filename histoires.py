from tkinter import *

class histoires_lakers(Tk):
    def __init__(self, Interface=None):
        super(histoires_lakers, self).__init__()
        self.title("PlayerBasket")
        self.config(background='#282828')
        self.iconbitmap("assets/logo.ico")
        self.geometry("1000x542")
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title = Label(self, text="Histoires des Lakers", font=("times new roman", 25), bg='#000000', fg='white',
                      anchor='w')
        title.place(x=350, y=20)

        title = Label(self, text="Nous allons vous raconter la petit histoires des Lakers-Los Angeles :",
                      font=("times new roman", 15), bg='#282828', fg='white', anchor='w')
        title.place(x=15, y=120)

        title = Label(self,
                      text="Tout commence en 1946 par la création de la NBL, qui deviendra en 1949 la NBA.  La franchise Détroit Gems voit le jour ",
                      font=("times new roman", 15), bg='#282828', fg='white', anchor='w')
        title.place(x=15, y=180)

        title = Label(self, text="et connait une première saison catastrophique ponctuée de 40 défaites en 44 matches.",
                      font=("times new roman", 15), bg='#282828', fg='white', anchor='w')
        title.place(x=15, y=200)

        title = Label(self,
                      text="En 1947, elle est rachetée et délocalisée à Minneapolis sous le nom de « Lakers » (les habitants du Lac) en référence à la",
                      font=("times new roman", 15), bg='#282828', fg='white', anchor='w')
        title.place(x=15, y=260)

        title = Label(self, text="région des « Grands Lacs » dont est proche la ville.",
                      font=("times new roman", 15), bg='#282828', fg='white', anchor='w')
        title.place(x=15, y=280)

        title = Label(self,
                      text="Elle restera en place jusqu’en 1960 avant de rejoindre Los Angeles pour ses plus belles heures de gloire.",
                      font=("times new roman", 15), bg='#282828', fg='white', anchor='w')
        title.place(x=15, y=320)

        imgprincipale = PhotoImage(file="assets/2527948.png").subsample(6)
        imgprincipale_1 = Label(self, image=imgprincipale, bg="#000000")
        imgprincipale_1.place(x=10, y=0)

        imgsecond = PhotoImage(file="assets/2527948.png").subsample(6)
        imgsecond_2 = Label(self, image=imgsecond, bg="#000000")
        imgsecond_2.place(x=900, y=0)

        droit = Label(self, text="© 2022 Playerbasket", bg="#282828", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=460, y=510)

        self.mainloop()