from tkinter import *
import json
from pathlib import Path
from tkinter import *
import wget
from PIL import ImageTk
from PIL import Image
import os
from joueurs_miami import Joueurs_miami


class Main5(Tk):
    def __init__(self,  Interface=None):
        super(Main5, self).__init__()
        self.title("PlayerBasket")
        self.config(background='#FF3951')
        self.iconbitmap("assets/logo.ico")
        self.geometry("1000x542")
        self.resizable(False, False)

        Barre1 = Canvas(self, width=1000, height=90, bg="#000000", highlightthickness=0)
        Barre1.place(x=0, y=0)

        title_bar = Label(self, text="PlayerBasket", bg="#000000", fg="#FFFFFF", font=('Roboto', 22))
        title_bar.place(x=400, y=20)

        title_second = Label(self, text="Veuiller rentrer le nom et le prénom du joueur :", bg="#FF3951", fg="#FFFFFF",
                             font=('Roboto', 15))
        title_second.place(x=30, y=100)

        self.entry = Entry(self, bd=0, bg="#8A8A8A")
        self.entry.place(x=360, y=150, height=30, width=350)
        self.entry['justify'] = 'center'

        self.add_btn = Button(self, text="Rechercher", bg="#FF1C37", fg="white", relief=FLAT,
                              font=('Arial', 12, 'bold'), bd=1, activebackground="#FF1C37",
                              activeforeground="white", command=self.search_data)
        self.add_btn.place(x=480, y=200)

        look_btn = Button(self, text="Voir l'équipe", bg="#FF1C37", fg="white", relief=FLAT,
                          font=('arial', 12), width=20, activebackground="#FF1C37", activeforeground="White",
                          command=lambda: Joueurs_miami(self.destroy()))
        look_btn.place(x=800, y=500)

        droit = Label(self, text="© 2022 Playerbasket", bg="#FF3951", font=('arial', 8, 'bold'), fg='#fff')
        droit.place(x=460, y=510)

        self.mainloop()

    def search_data(self):
        with open("donées/Donnée_heat.json", "r+") as files:
            data = json.load(files)
            for i in range(len(data["data"])):
                if self.entry.get() in data['data'][i]["full_name"]:
                    full_name = data["data"][i]["full_name"]
                    height = data["data"][i]["height"]
                    position = data["data"][i]["position"]
                    date_of_birth = data["data"][i]["date_of_birth"]
                    Years_pro = data["data"][i]["Years_pro"]
                    weight = data["data"][i]["weight"]
                    Years_player = data["data"][i]["Years_player"]
                    From = data["data"][i]["From"]
                    text = Label(self,
                                 text=f"{full_name}, \n{height}, \n{position}, \n{date_of_birth}, \n{Years_pro}, \n{weight}, \n{Years_player}, \n{From}",
                                 bg='#FF3951', font=('Arial', 17))
                    text.place(x=50, y=240)
                    value = data["data"][i]["img"]
                    name_of_picture = wget.detect_filename(value)
                    path_img = Path(f"images\{name_of_picture}")
                    if path_img.exists():
                        os.remove(f"images\{name_of_picture}")
                    wget.download(value, "./images/Miami")
                    path = os.getcwd()
                    img = Image.open(f"{path}/images/Miami/{name_of_picture}")
                    Images = img.resize((300, 200), Image.ANTIALIAS)
                    pictures = ImageTk.PhotoImage(Images)
                    photo_value = Label(self, image=pictures)
                    photo_value.photo = pictures
                    photo_value.place(x=670, y=240)

                    break