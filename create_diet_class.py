import libs
class CreateDiet(libs.Frame):

    def __init__(self, parent, controller):
        libs.Frame.__init__(self, parent)
        render = libs.PIL.ImageTk.PhotoImage(libs.PIL.Image.open("D:\Python\Projekty\Projektb\Dietetyk\Images\mainpageb.jpg"))
        img = libs.Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        self.create_widgets(controller)

    def create_widgets(self, controller):
        self.photo = libs.PhotoImage(file="D:\Python\Projekty\Projektb\Dietetyk\Images\strzalka.gif")
        self.button1 = libs.Button(self, text="Back", bg='white', image = self.photo,
                                   command=lambda: controller.show_frame(libs.start_page_class.StartPage)).place(x=10, y=10)