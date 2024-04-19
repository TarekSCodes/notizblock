import customtkinter as ctk
import const

class TopMenu(ctk.CTkFrame):
    def __init__(self, parent, text_multi_frame, note_frame):
        super().__init__(parent, corner_radius=0)
        self.pack(fill="x", ipady=10)

        # define top menu grid
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")

        # Eingaben aus der Hauptklasse (App)
        self.text_multi_frame = text_multi_frame
        self.note_frame = note_frame

        # place widgets
        self.create_top_menu_widgets()

    def create_top_menu_widgets(self):
        
        notesButton = ctk.CTkButton(
            master=self,
            text="Notizen",
            fg_color=const.FRAME_BACKGROUND_COLOR,
            text_color=const.TOP_MENU_BUTTON_FONT_COLOR,
            corner_radius=0,
            image=const.NOTIZEN_ICON_IMAGE,
            font=const.BUTTON_FONT,
            hover_color=const.BUTTON_COLOR_HOVER,
            command=self.menu_func_notes
            )
        notesButton.grid(column=0, row=0, padx=0, sticky="nsew")
        
        translatorButton = ctk.CTkButton(
            master=self,
            text="Übersetzer",
            fg_color=const.FRAME_BACKGROUND_COLOR,
            text_color=const.TOP_MENU_BUTTON_FONT_COLOR,
            corner_radius=0,
            image=const.TRANSLATOR_ICON_IMAGE,
            font=const.BUTTON_FONT,
            hover_color=const.BUTTON_COLOR_HOVER,
            command=self.menu_func_text_multi
            )
        translatorButton.grid(column=1, row=0, padx=0, sticky="nsew")

    def menu_func_text_multi(self):
        """versteckt das note_frame und zeigt das text_multi_frame an"""
        
        self.note_frame.pack_forget()
        self.text_multi_frame.pack(expand=True, fill="both")

    def menu_func_notes(self):
        """versteckt das text_multi_frame und zeigt das note_frame an"""
        
        self.text_multi_frame.pack_forget()
        self.note_frame.pack(expand=True, fill="both")