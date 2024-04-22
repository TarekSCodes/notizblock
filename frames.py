import customtkinter as ctk
import const

# beinhaltet das Entry Feld und den hinzufügen Button
class EntryFrame(ctk.CTkFrame):
    def __init__(self, master, func, entry_string):
        super().__init__(master=master, corner_radius=0, fg_color=const.FRAME_BACKGROUND_COLOR)
        self.pack(fill="x")
        
        # Eingaben
        self.command = func
        self.entry_string = entry_string
        
        self.create_widgets()

    def create_widgets(self):
        # Entry zum Eingeben der Aufgaben
        textBoxNotizen = ctk.CTkEntry(
            master=self,
            textvariable=self.entry_string,
            corner_radius=5,
            border_width=1,
            width=300,
            height=40,
            font=const.TEXTBOX_NOTES_FONT
        )
        textBoxNotizen.pack(side="left", padx=10, pady=5)
        textBoxNotizen.bind("<Return>", self.command)
        
        # Button zum Hinzufügen der Aufgaben
        erstelleNotizButton = ctk.CTkButton(
            master=self,
            text="",
            width=20,
            height=40,
            fg_color=const.FRAME_BACKGROUND_COLOR,
            hover_color=const.BUTTON_COLOR_HOVER,
            command=self.command,
            corner_radius=5, 
            image=const.ADD_BUTTON_IMAGE
            )
        erstelleNotizButton.pack(pady=0, anchor=None, side="left")  

class Footer(ctk.CTkFrame):
    def __init__(self, parent, corner_radius, fill, height, about_func):
        super().__init__(
            master=parent,
            corner_radius=corner_radius,
            height=height,
            fg_color=const.FRAME_BACKGROUND_COLOR
        )
        self.pack(fill=fill)
        
        # grid definieren
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")
        
        # Eingaben
        self.about_func = about_func
        
        self.create_widgets()
        
    def create_widgets(self):
        aboutButton = ctk.CTkButton(
            master=self,
            text="About",
            fg_color=const.FRAME_BACKGROUND_COLOR,
            hover_color=const.FRAME_BACKGROUND_COLOR,
            text_color=const.ABOUT_BUTTON_FONT_COLOR,
            command=self.about_func,
            font=const.BUTTON_FONT_SMALL,
            width=10
            )
        aboutButton.grid(column=1, row=0, sticky="e",padx=20, pady=12)
