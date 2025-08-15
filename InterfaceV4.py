import customtkinter



class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")

        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.grid_columnconfigure(j, weight=1)

        root_frame = customtkinter.CTkFrame(self)
        root_frame.grid(row=0, column=0, sticky="nsew")

        root_frame.grid_rowconfigure(0, weight=1)
        root_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in (WelcomeScreen, Dashboard, InitialiseItem):
            frame = f(root_frame)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.display_frame(WelcomeScreen)


    def display_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class WelcomeScreen(customtkinter.CTkFrame):
    def __init__(self, root_class):
        super().__init__(root_class)

        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.grid_columnconfigure(j, weight=1)

        username_entry = customtkinter.CTkEntry(self, height=50, width=300, placeholder_text="Enter Username")
        username_entry.grid(row = 0, column = 0, sticky = "nsew")

        password_entry = customtkinter.CTkEntry(self, height=50, width=300, placeholder_text="Enter Password")
        password_entry.grid(row=2, column=2, sticky="nsew")

        if both successful
            command show dashboard


class Dashboard(customtkinter.CTkFrame):
    def __init__(self, root_class, controller):
        super().__init__(root_class)

        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.grid_columnconfigure(j, weight=1)

        go_to_init_new_item = customtkinter.CTkButton(self, text="Initialise New Item",
                                                   command = lambda : controller.display_frame(InitialiseNewItem))
        go_to_update_level = customtkinter.CTkButton(self, text="Update Current Level",
                                                   command = lambda : controller.display_frame(UpdateCurrentLevel))

class InitialiseNewItem(customtkinter.CTkFrame):
    def __init__(self, root_class, controller):
        super().__init__(root_class)

        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.grid_columnconfigure(j, weight=1)

        go_to_dashboard = customtkinter.CTkButton(self, text="Dashboard",
                                                    command=lambda: controller.display_frame(Dashboard))
