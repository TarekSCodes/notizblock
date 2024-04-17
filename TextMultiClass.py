import customtkinter as ctk
from frames import EntryFrame
from googletrans import Translator
import tkinter as tk
from PIL import Image
import pyperclip
import pytesseract
from tkinter.filedialog import askopenfilename

class TextMulti(ctk.CTkFrame):
    def __init__(self, parent, button_font_small, textbox_notes_font, button_color_hover, frame_bg_color, frame_bg_color_invert, button_font_color, copy_image, image2text, add_button_image, about_func):
        super().__init__(parent, fg_color=frame_bg_color, corner_radius=0)
        self.pack(expand=True, fill="both")

        self.entry_str = ctk.StringVar(value="")
        self.target_language = ctk.StringVar(value="deutsch")
        
        # font Eingaben
        self.button_font_small = button_font_small
        self.textbox_notes_font = textbox_notes_font

        # color Eingaben
        self.button_color = frame_bg_color
        self.button_color_hover = button_color_hover
        self.button_font_color = button_font_color
        self.frame_bg_color = frame_bg_color
        self.frame_bg_color_invert = frame_bg_color_invert
        
        # image Eingaben
        self.copy_image = copy_image
        self.image2text = image2text
        self.add_button_image = add_button_image
        
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
        
        test = EntryFrame(self,self.translate_text, self.entry_str, self.frame_bg_color, self.button_color_hover, self.add_button_image, self.textbox_notes_font)
        test.pack_forget()
        test.grid(column=0, columnspan=2, row=0, sticky="w", padx=0, pady=0)
        
        ubersetzenButton = ctk.CTkButton(
            master=self,
            text="Übersetzen",
            height=50,
            fg_color=self.button_color,
            hover_color=self.button_color_hover,
            text_color=self.button_font_color,
            command=self.translate_text,
            font=self.button_font_small,
            corner_radius=0
        ).grid(column=0, row=1, sticky="ew")

        boxLeerenButton = ctk.CTkButton(
            master=self,
            text="Leeren",
            height=50,
            fg_color=self.button_color,
            hover_color=self.button_color_hover,
            text_color=self.button_font_color,
            command=self.empty_box,
            font=self.button_font_small,
            corner_radius=0
        ).grid(column=1, row=1, sticky="ew")

        image2TextButton = ctk.CTkButton(
            master=self,
            text="",
            height=50,
            fg_color=self.button_color,
            hover_color=self.button_color_hover,
            text_color=self.button_font_color,
            command=self.imagefunk,
            font=self.button_font_small,
            corner_radius=0,
            image=self.image2text
        ).grid(column=1, row=2, sticky="ew")
        
        self.copy_button = ctk.CTkButton(
            master=self,
            text="",
            height=50,
            fg_color=self.button_color,
            hover_color=self.button_color_hover,
            text_color=self.button_font_color,
            command=self.copy_clipboard,
            font=self.button_font_small,
            corner_radius=0,
            state=ctk.DISABLED,
            image=self.copy_image
        ).grid(column=0, row=2, sticky="ew")

        self.textbox = ctk.CTkTextbox(
            master=self,
            corner_radius=0,
            height=300,
            font=self.textbox_notes_font,
            fg_color=self.frame_bg_color,
            bg_color=self.frame_bg_color,
            text_color=self.frame_bg_color_invert
        ).grid(column=0, columnspan=2, row=3, sticky="nsew", pady=0, padx=0)
        
        auswahlUebersetzungsSprache = ctk.CTkComboBox(
            master=self,
            fg_color=self.frame_bg_color,
            border_width=1,
            values=["deutsch", "englisch", "spanisch"],
            font=self.button_font_small,
            width=120,
            height=30,
            dropdown_fg_color=self.frame_bg_color,
            text_color=self.button_font_color,
            dropdown_font=self.button_font_small,
            variable=self.target_language
        ).grid(column=0, columnspan=1, row=4, sticky="w", padx=10)

        aboutButton = ctk.CTkButton(
            master=self,
            text="About",
            fg_color=self.frame_bg_color,
            hover_color=self.frame_bg_color,
            text_color="grey",
            command=self.about_func,
            font=self.button_font_small,
            corner_radius=0
            ).grid(column=1, row=4, sticky="es")
      
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