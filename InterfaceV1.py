import customtkinter

class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        main_frame = customtkinter.CTkFrame(self)
        main_frame.pack()

        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        self.all_frames = []
        