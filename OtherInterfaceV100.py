import customtkinter

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.root_frame = customtkinter.CTkFrame(self)
        self.root_frame.pack()

        self.frame1 = WelcomeScreen(self.root_frame)
        self.frame2 = Dashboard(self.root_frame)
        self.frame3 = InitialiseNewItem(self.root_frame)

        self.display_welcome_screen()

    def display_frame(self, frame):
        frame.tkraise()

    def display_welcome_screen(self):
        self.display_frame(self.frame1)

    def display_dashboard(self):
        self.display_frame(self.frame2)

    def display_init_new_item(self):
        self.display_frame(self.frame3)



class WelcomeScreen(customtkinter.CTkFrame):
    def __init__(self, root):
        super().__init__(root)


class Dashboard(customtkinter.CTkFrame):
    def __init__(self, root):
        super().__init__(root)

class InitialiseNewItem(customtkinter.CTkFrame):
    def __init__(self, root):
        super().__init__(root)


main = Root()
main.mainloop()