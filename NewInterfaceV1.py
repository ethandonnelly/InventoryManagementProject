# I began with trying to get the switching between frames functional
# I didn't focus on any other functionalities at this point

import customtkinter

class Root(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")

        # Configure the rows and columns of the root window
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Create the root frame (the frame that holds all the other frames)
        self.root_frame = customtkinter.CTkFrame(self)
        # Place the root frame into the root window
        self.root_frame.grid(row=0, column=0, sticky="nesw")

        # Configure the rows and columns of the root frame
        self.root_frame.rowconfigure(0, weight=1)
        self.root_frame.columnconfigure(0, weight=1)

        self.frame1 = Frame1
        self.frame2 = Frame2

        def display_frame1():
            self.frame1.pack(self.root_frame)

        def display_frame2():
            self.frame2.pack(self.root_frame)

        display_frame1()

class Frame1(customtkinter.CTkFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)

        for i in range(10):
            self.grid_rowconfigure(i, weight=1)
        for j in range(10):
            self.grid_columnconfigure(j, weight=1)

        go_to_frame2 = customtkinter.CTkButton(self, text="Go To Frame 2", command=display_frame2())
        go_to_frame2.grid(row=0, column=0)

class Frame2(customtkinter.CTkFrame):
    def __init__(self, root_frame):
        super().__init__(root_frame)

        for i in range(10):
            self.grid_rowconfigure(i, weight=1)
        for j in range(10):
            self.grid_columnconfigure(j, weight=1)

        go_to_frame1 = customtkinter.CTkButton(self, text="Go To Frame 2", command=display_frame1())
        go_to_frame1.grid(row=0, column=0)


main = Root()
main.mainloop()

# It is clear that my method of trying to switch between frames doesn't work because of the display_frame being an unresolved reference
# It still didn't work when I did Root.display_frame

