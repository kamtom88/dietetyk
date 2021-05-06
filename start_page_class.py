import libs
class StartPage(libs.Frame):

    def __init__(self, parent, controller):
        libs.Frame.__init__(self, parent)
        label = libs.Label(self, text="Start Page", font=libs.class_container.LARGE_FONT)
        label.pack(pady=10, padx=10)
        render = libs.PIL.ImageTk.PhotoImage(libs.PIL.Image.open("D:\Python\Projekty\Projektb\Dietetyk\Images\mainpageA.jpg"))
        img = libs.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        self.create_widgets(controller)


    def create_widgets(self,controller):

        self.add_product = libs.Button(self, text="Dodaj Produkt", command=lambda: controller.show_frame(libs.add_produc_class.AddProd), height = 2, width = 12).place(x=850, y=100)
        self.create_dish = libs.Button(self, text="Stworz Danie", command=lambda: controller.show_frame(libs.create_dish_class.CreateDish), height = 2, width = 12).place(x=850, y=200)
        self.create_diet = libs.Button(self, text="Stworz Diete", command=lambda: controller.show_frame(libs.create_diet_class.CreateDiet), height = 2, width = 12).place(x=850, y=300)


