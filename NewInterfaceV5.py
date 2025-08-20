# In this version, I begin to play around with the welcome screen, making it look good


import customtkinter
from LoginV1 import User

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")

        # Configure the rows and columns of the root window
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Create the root frame (the frame that holds all the other frames)
        root_frame = customtkinter.CTkFrame(self)
        # Place the root frame into the root window
        root_frame.grid(row=0, column=0, sticky="nesw")

        # Configure the rows and columns of the root frame
        root_frame.rowconfigure(0, weight=1)
        root_frame.columnconfigure(0, weight=1)

        self.frames = {}
        for f in (WelcomeScreen, Frame2):
            frame = f(root_frame, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.display_frame(WelcomeScreen)

    def display_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class WelcomeScreen(customtkinter.CTkFrame):
    def __init__(self, root_frame, root):
        super().__init__(root_frame)

        for i in range(25):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

        def get_new_details():
            new_username = new_username_entry.get()
            new_password = new_password_entry.get()
            check = User.validate_new_username_and_password(new_username, new_password)
            if check is True:
                root.display_frame(Frame2)
            else:
                error_message = customtkinter.CTkLabel(self, height=50, width=200, text="", font=("Coolvetica", 22))
                error_message.grid(row=30, column=2, sticky="nw")

        def get_existing_details():
            existing_username = existing_username_entry.get()
            existing_password = existing_password_entry.get()
            check = User.validate_existing_username_and_password(existing_username, existing_password)
            if check is True:
                root.display_frame(Frame2)
            else:
                error_message = customtkinter.CTkLabel(self, height=50, width=200, text="", font=("Coolvetica", 22))
                error_message.grid(row=30, column=2, sticky="nw")

        left_border_frame = customtkinter.CTkFrame(self, fg_color="#90D5FF")
        left_border_frame.grid(row=0, column=0, rowspan=25, sticky="nesw")

        new_username_entry = customtkinter.CTkEntry(self, height=50, width=200, placeholder_text="Enter Username", font=("Coolvetica", 22))
        new_username_entry.grid(row=10, column=2, sticky="nw")

        new_password_entry = customtkinter.CTkEntry(self, height=50, width=200, placeholder_text="Enter Password", font=("Coolvetica", 22))
        new_password_entry.grid(row=20, column=2, sticky="nw")

        create_account__button = customtkinter.CTkButton(self, height=50, width=200, text="Proceed", font=("Coolvetica", 22), command=get_new_details)
        create_account__button.grid(row=30, column=2, sticky="nw")

        existing_username_entry = customtkinter.CTkEntry(self, height=50, width=200, placeholder_text="Enter Username", font=("Coolvetica", 22))
        existing_username_entry.grid(row=10, column=2, sticky="nw")

        existing_password_entry = customtkinter.CTkEntry(self, height=50, width=200, placeholder_text="Enter Password", font=("Coolvetica", 22))
        existing_password_entry.grid(row=20, column=2, sticky="nw")

        login_button = customtkinter.CTkButton(self, height=50, width=200, text="Proceed", font=("Coolvetica", 22), command=get_existing_details)
        login_button.grid(row=30, column=2, sticky="nw")

        go_to_frame2 = customtkinter.CTkButton(self, text="Go To Frame 2",
                                               command=lambda : root.display_frame(Frame2))
        go_to_frame2.grid(row=0, column=0, sticky="nesw")


class Frame2(customtkinter.CTkFrame):
    def __init__(self, root_frame, root):
        super().__init__(root_frame)

        for i in range(25):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)


        go_to_frame1 = customtkinter.CTkButton(self, text="Go To Frame 1",
                                               command=lambda : root.display_frame(WelcomeScreen))
        go_to_frame1.grid(row=0, column=0, sticky="nesw")


