import libs

class CreateDish(libs.Frame):

    def __init__(self, parent, controller):
        libs.Frame.__init__(self, parent)
        render = libs.PIL.ImageTk.PhotoImage(libs.PIL.Image.open("D:\Python\Projekty\Projektb\Dietetyk\Images\mainpageb.jpg"))
        img = libs.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        self.create_widgets(controller)
        self.dbinstance2 = libs.database_class.Db()

    def create_widgets(self,controller):
        self.photo = libs.PhotoImage(file="D:\Python\Projekty\Projektb\Dietetyk\Images\strzalka.gif")
        self.button1 = libs.Button(self, text="Back", bg='white', image = self.photo,
                                   command=lambda: controller.show_frame(libs.start_page_class.StartPage)).place(x=10, y=10)
        self.framefortext=libs.Frame(self,width=285, height=160,bg="white")
        self.framefortext.place(x=680,y=30)
        self.text = libs.Text(self.framefortext, width=35, height=10)
        self.text.place(x=1,y=1)
        self.label1=libs.Label(self, text="Czego Szukasz:").place(x=680, y=200)
        self.entry=libs.Entry(self)
        self.entry.place(x=770,y=200)
        self.button2=libs.Button(self,text="szukaj",height = 1, width = 6, command = lambda: self.database_search())
        self.button2.place(x=910, y = 200)

    def database_search(self):
        product = self.entry.get()
        query = "select * from Produkty where NazwaProduktu like '%{}%'".format(product)
        self.text.delete(0.0,libs.END)
        sqloutput = self.dbinstance2.query(query)
        self.text.insert(0.0,sqloutput)


