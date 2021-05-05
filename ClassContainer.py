import libs

LARGE_FONT = ("Verdana", 12)


class Classcontainer(libs.Tk):

    def __init__(self, *args, **kwargs):
        libs.Tk.__init__(self, *args, **kwargs)
        container = libs.Frame(self)

        container.pack(side="left", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (libs.StartPageClass.StartPage, libs.AddProductClass.AddProd, libs.CreateDishClass.CreateDish,libs.CreateDietClass.CreateDiet):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(libs.StartPageClass.StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()