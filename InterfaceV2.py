import customtkinter


class WelcomeScreen(customtkinter.CTkFrame):
    def __init__(self, main_class):
        super().__init__(main_class)
        self.name_entry = customtkinter.CTkEntry(self,
                                                 height=50,
                                                 width=300,
                                                 placeholder_text="User: ",
                                                 corner_radius=20).grid(row = 0, column = 0, sticky = "nsew")

        self.pack()



class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.rowconfigure((0, 1, 2), weight=1)




main = Main()
ws = WelcomeScreen(main)
main.mainloop()