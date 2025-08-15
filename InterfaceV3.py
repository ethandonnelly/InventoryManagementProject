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
        root_frame.grid(row = 0, column = 0, sticky="nsew")

        root_frame.grid_rowconfigure(0, weight=1)
        root_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in (Page1, Page2):
            frame = f(root_frame)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky= "nsew")
        self.display_frame(Page1)

    def display_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

class Page1(customtkinter.CTkFrame):
    def __init__(self, root_class):
        super().__init__(root_class)

        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.grid_columnconfigure(j, weight=1)

        label = customtkinter.CTkLabel(self, text="Frame1", font=("Arial", 35))
        label.grid(row=2, column=1, sticky="nsew")


class Page2(customtkinter.CTkFrame):
    def __init__(self, root_class):
        super().__init__(root_class)
        label = customtkinter.CTkLabel(self, text="Frame2")
        label.pack()

root = Root()
root.mainloop()



