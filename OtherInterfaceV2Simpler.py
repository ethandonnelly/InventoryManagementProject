import customtkinter

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")

        self.root_frame = customtkinter.CTkFrame(self)
        self.root_frame.pack()

        self.frame1 = Frame1(self.root_frame)
        self.frame2 = Frame2(self.root_frame)

        for frame in (self.frame1, self.frame2):
            frame.grid(row=0, column=0, sticky="nsew")

        self.display_frame1()

    def display_frame(self, frame):
            frame.tkraise()

    def display_frame1(self):
        self.display_frame(self.frame1)

    def display_frame2(self):
        self.display_frame(self.frame2)

class Frame1(customtkinter.CTkFrame):
    def __init__(self, root_frame, root):
        super().__init__(root_frame)
        self.root = root

        go_to_frame2 = customtkinter.CTkButton(self, text="Go To Frame 2",
                                               command=self.root.display_frame1)
        go_to_frame2.pack()


class Frame2(customtkinter.CTkFrame):
    def __init__(self, root_frame, root):
        super().__init__(root_frame)
        self.root = root

        go_to_frame1 = customtkinter.CTkButton(self, text="Go To Frame 2",
                                               command=self.root.display_frame2)
        go_to_frame1.pack()