import customtkinter as ctk

class TopMenu(ctk.CTkFrame):
    def __init__(self, parent, button_font, button_color_hover,
                 button_font_small,textbox_notes_font, text_multi_frame, note_frame, frame_bg_color, notizen_icon, translator_icon):
        super().__init__(parent, fg_color=frame_bg_color, corner_radius=0)
        self.pack(fill="x", ipady=10)

        # define top menu grid
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")

        # Eingaben aus der Hauptklasse (App)
        self.button_font = button_font
        self.button_font_small = button_font_small
        self.textbox_notes_font = textbox_notes_font
        self.button_color_hover = button_color_hover
        self.frame_bg_color = frame_bg_color
        self.text_multi_frame = text_multi_frame
        self.note_frame = note_frame
        self.notizen_icon = notizen_icon
        self.translator_icon = translator_icon

        # place widgets
        self.create_top_menu_widgets()

    def create_top_menu_widgets(self):
        
        notesButton = ctk.CTkButton(
            master=self,
            text="Notizen",
            fg_color=("#f3f3f3", "#191919"),
            text_color=("black", "#5d5d5d"),
            corner_radius=0,
            image=self.notizen_icon,
            font=self.button_font,
            hover_color=self.button_color_hover,
            command=self.menu_func_notes
            ).grid(column=0, row=0, padx=0, sticky="nsew")
        
        translatorButton = ctk.CTkButton(
            master=self,
            text="Übersetzer",
            fg_color=("#f3f3f3", "#191919"),
            text_color=("black", "#5d5d5d"),
            corner_radius=0,
            image=self.translator_icon,
            font=self.button_font,
            hover_color=self.button_color_hover,
            command=self.menu_func_text_multi
            ).grid(column=1, row=0, padx=0, sticky="nsew")

    def menu_func_text_multi(self):
        """versteckt das note_frame und zeigt das text_multi_frame an"""
        
        self.note_frame.pack_forget()
        self.text_multi_frame.pack(expand=True, fill="both")

    def menu_func_notes(self):
        """versteckt das text_multi_frame und zeigt das note_frame an"""
        
        self.text_multi_frame.pack_forget()
        self.note_frame.pack(expand=True, fill="both")