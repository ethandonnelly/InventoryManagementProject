# Here I started to tighten up some of the placements and learn more about grid

import customtkinter

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
        for f in (Frame1, Frame2):
            frame = f(root_frame, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.display_frame(Frame1)

    def display_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class Frame1(customtkinter.CTkFrame):
    def __init__(self, root_frame, root):
        super().__init__(root_frame)

        for i in range(25):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)

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
                                               command=lambda : root.display_frame(Frame1))
        go_to_frame1.grid(row=0, column=0, sticky="nesw")


main = Root()
main.mainloop()

