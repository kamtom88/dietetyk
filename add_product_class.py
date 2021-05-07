import libs


class AddProd(libs.Frame):

    def __init__(self, parent, controller):
        libs.Frame.__init__(self, parent)
        render = libs.PIL.ImageTk.PhotoImage(libs.PIL.Image.open("D:\Python\Projekty\Projektb\Dietetyk\Images\mainpageb.jpg"))
        img = libs.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        self.create_widgets(controller)
        self.dbinstance = libs.database_class.Db()

    def create_widgets(self,controller):
        self.photo = libs.PhotoImage(file="D:\Python\Projekty\Projektb\Dietetyk\Images\strzalka.gif")
        self.button1 = libs.Button(self, text="Back", bg='white', image = self.photo,
                                   command=lambda: controller.show_frame(libs.start_page_class.StartPage)).place(x=10, y=10)
        # utwórz etykietęty
        self.myFont = libs.font.Font(family='Helvetica', size=10)
        t1 = ["Nazwa Produktu","kcal","Białko","Węglowodany","Tłuszcze"]
        t2 = ["self.name","self.kcal","self.bial","self.wegl","self.tl"]
        counter=0
        for i in range(len(t1)):
            t2[i] = libs.Label(self, font=self.myFont, text=t1[i]).place(x=700,y=100+counter)
            counter += 40
        # # utwórz widżety Entry do przyjęcia dan(x=10,y=10)ych do bazy
        self.name_ent = libs.Entry(self)
        self.name_ent.place(x=810,y=100)
        self.kcal_ent = libs.Entry(self)
        self.kcal_ent.place(x=810,y=140)
        self.bial_ent = libs.Entry(self)
        self.bial_ent.place(x=810,y=180)
        self.wegl_ent = libs.Entry(self)
        self.wegl_ent.place(x=810,y=220)
        self.tl_ent = libs.Entry(self)
        self.tl_ent.place(x=810,y=260)

        # utwórz przycisk 'Akceptuj'
        self.submit_bttn = libs.Button(self, text="Dodaj", command=self.click_button).place(x=900,y=300)
        # self.submit_bttn.grid(row=5, column=4, sticky=E)
    def click_button(self):

        self.dbinstance.insert("insert into Produkty (NazwaProduktu,kcal,bialko,weglowodany,tluszcze)\
             values('{}',{},{},{},{})".format(self.name_ent.get(), self.kcal_ent.get(), self.bial_ent.get(),
                                              self.wegl_ent.get(), self.tl_ent.get()))



