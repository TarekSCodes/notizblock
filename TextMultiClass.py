import customtkinter as ctk
import const
from frames import EntryFrame
from googletrans import Translator
import tkinter as tk
from PIL import Image
import pyperclip
import pytesseract
from tkinter.filedialog import askopenfilename

class TextMulti(ctk.CTkFrame):
    def __init__(self, parent, about_func):
        super().__init__(parent, corner_radius=0, fg_color=const.FRAME_BACKGROUND_COLOR)
        self.pack(expand=True, fill="both")

        self.entry_str = ctk.StringVar(value="")
        self.target_language = ctk.StringVar(value="deutsch")
        
        # func Eingaben
        self.about_func = about_func

        # grid definieren
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="b")
        self.rowconfigure(1, weight=1, uniform="b")
        self.rowconfigure(2, weight=1, uniform="b")
        self.rowconfigure(3, weight=100, uniform="c")
        self.rowconfigure(4, weight=1, uniform="b")

        self.create_widgets()

        self.translator = Translator()

    def create_widgets(self):
        
        test = EntryFrame(self, self.translate_text, self.entry_str)
        test.pack_forget()
        test.grid(column=0, columnspan=2, row=0, sticky="w", padx=0, pady=0)
        
        ubersetzenButton = ctk.CTkButton(
            master=self,
            text="Übersetzen",
            height=50,
            fg_color=const.FRAME_BACKGROUND_COLOR,
            hover_color=const.BUTTON_COLOR_HOVER,
            text_color=const.BUTTON_FONT_COLOR,
            command=self.translate_text,
            font=const.BUTTON_FONT_SMALL,
            corner_radius=0
        )
        ubersetzenButton.grid(column=0, row=1, sticky="ew")

        boxLeerenButton = ctk.CTkButton(
            master=self,
            text="Leeren",
            height=50,
            fg_color=const.FRAME_BACKGROUND_COLOR,
            hover_color=const.BUTTON_COLOR_HOVER,
            text_color=const.BUTTON_FONT_COLOR,
            command=self.empty_box,
            font=const.BUTTON_FONT_SMALL,
            corner_radius=0
        )
        boxLeerenButton.grid(column=1, row=1, sticky="ew")

        image2TextButton = ctk.CTkButton(
            master=self,
            text="",
            height=50,
            fg_color=const.FRAME_BACKGROUND_COLOR,
            hover_color=const.BUTTON_COLOR_HOVER,
            text_color=const.BUTTON_FONT_COLOR,
            command=self.imagefunk,
            font=const.BUTTON_FONT_SMALL,
            corner_radius=0,
            image=const.IMAGE2TEXT
        )
        image2TextButton.grid(column=1, row=2, sticky="ew")
        
        self.copy_button = ctk.CTkButton(
            master=self,
            text="",
            height=50,
            fg_color=const.FRAME_BACKGROUND_COLOR,
            hover_color=const.BUTTON_COLOR_HOVER,
            text_color=const.BUTTON_FONT_COLOR,
            command=self.copy_clipboard,
            font=const.BUTTON_FONT_SMALL,
            corner_radius=0,
            state=ctk.DISABLED,
            image=const.COPY_IMAGE
        )
        self.copy_button.grid(column=0, row=2, sticky="ew")

        self.textbox = ctk.CTkTextbox(
            master=self,
            corner_radius=0,
            height=300,
            font=const.TEXTBOX_NOTES_FONT,
            fg_color=const.FRAME_BACKGROUND_COLOR,
            bg_color=const.FRAME_BACKGROUND_COLOR,
            text_color=const.FRAME_BACKGROUND_COLOR_INVERT
        )
        self.textbox.grid(column=0, columnspan=2, row=3, sticky="nsew", pady=0, padx=0)
        
        auswahlUebersetzungsSprache = ctk.CTkComboBox(
            master=self,
            fg_color=const.FRAME_BACKGROUND_COLOR,
            border_width=1,
            values=["deutsch", "englisch", "spanisch"],
            font=const.BUTTON_FONT_SMALL,
            width=120,
            height=30,
            dropdown_fg_color=const.FRAME_BACKGROUND_COLOR,
            text_color=const.BUTTON_FONT_COLOR,
            dropdown_font=const.BUTTON_FONT_SMALL,
            variable=self.target_language
        )
        auswahlUebersetzungsSprache.grid(column=0, columnspan=1, row=4, sticky="w", padx=10)

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
        aboutButton.grid(column=1, row=4, sticky="e", padx=20)
      
    def translate_text(self):
        self.textbox.delete("1.0", tk.END)
        
        # prüfen welche Zielsprache ausgewählt ist und diese an den translator weitergeben
        current_language = ""
        if self.target_language.get() == "deutsch":
            current_language = "de"
        elif self.target_language.get() == "englisch":
            current_language = "en"
        else:
            current_language = "es"
            
        # prüfen ob entry feld nicht leer ist, wenn wahr dann wird der inhalt übersetzt
        # wenn unwahr wird die zwischenablage geprüft
        if self.entry_str.get():
            print(self.entry_str.get())
            result = self.translator.translate(self.entry_str.get(), dest=current_language).text
        elif self.clipboard_get():
            result = self.translator.translate(self.clipboard_get(), dest=current_language).text
            
        else:
            result = "Kein Text zum Übersetzen gefunden"
        self.textbox.insert(tk.END, result)
        self.copy_button.configure(state=ctk.NORMAL)

    def empty_box(self):
        self.textbox.delete("1.0", tk.END)
        self.copy_button.configure(state=ctk.DISABLED)
        self.entry_str.set("")

    def copy_clipboard(self):
        pyperclip.copy(self.textbox.get("1.0", tk.END))

    def imagefunk(self):
        self.textbox.delete("1.0", tk.END)
        name = askopenfilename()
        if name:
            string = pytesseract.image_to_string(Image.open(name))
            self.textbox.insert(tk.END, string)
            self.copy_button.configure(state=ctk.NORMAL)
            pyperclip.copy(self.textbox.get("1.0", tk.END))