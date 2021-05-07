import libs

LARGE_FONT = ("Verdana", 12)


class ClassContainer(libs.Tk):

    def __init__(self, *args, **kwargs):
        libs.Tk.__init__(self, *args, **kwargs)
        container = libs.Frame(self)

        container.pack(side="left", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (libs.start_page_class.StartPage, libs.add_product_class.AddProd, libs.create_dish_class.CreateDish, libs.create_diet_class.CreateDiet):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(libs.start_page_class.StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()