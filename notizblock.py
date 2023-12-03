from buttons import *
import customtkinter as ctk
import darkdetect
from frames import *
from googletrans import Translator
import os
import pickle
from PIL import Image
import pyperclip
import pytesseract
from text_entry import *
import tkinter as tk
from tkinter.filedialog import askopenfilename

tesseract_path = os.path.join(os.environ['ProgramFiles'], 'Tesseract-OCR', 'tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = tesseract_path

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

# TODO
#  1. Status des Erledigt Buttons mit abspeichern
#  2. am Fuß von textmulti auswahl buttons hizufügen - de,spa,eng - oder funktion
#     jenachdem welche sprache ausgewählt ist wird die zielsprache der übersetzung geändert
#  3. veränderten Inhalt der Notizen in der notizen.txt anpassen
#  4. integration von chat gpt
#  5. Wetter Api integrieren

class App(ctk.CTk):
    def __init__(self, title, size, is_dark):
        super().__init__(fg_color=("#f3f3f3", "#191919"))

        self.setup_window(title, size, is_dark)  # Window Setup
        self.setup_fonts()
        self.setup_colors()
        self.setup_images()
        self.setup_frames()

        self.mainloop()

    def setup_window(self, title, size, is_dark):
        self.title(title)
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/hamster.ico')
        self.iconbitmap(icon_path)
        self.geometry(f"{size[0]}x{size[1]}")
        self.attributes("-topmost", True)
        self.minsize(258, 300)
        self.maxsize(500, 800)
        self.title_bar_color(is_dark)

    def setup_fonts(self):
        # fonts
        self.button_font = ctk.CTkFont("Calibri", 15, weight="bold")
        self.button_font_small = ctk.CTkFont("Calibri", 10, weight="bold")
        self.textbox_font = ctk.CTkFont("calibre", 15, weight="bold")
        self.notes_font = ctk.CTkFont("Arial", 15)

    def setup_colors(self):
        # colors
        self.button_color_hover = ("#dadada", "#2c2c2c")
        self.frame_bg_color = ("#f3f3f3", "#191919")
        self.frame_bg_color_invert = ("#191919", "#f3f3f3")
        self.button_font_color = ("#2c2c2c", "#5e5e5e")

    def setup_images(self):
        # image des add buttons zum hinzufügen von Notizen
        add_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/add_button.png')
        add_icon_light = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/add_button_light.png')
        self.add_button_image = ctk.CTkImage(light_image=Image.open(add_icon_light), dark_image=Image.open(add_icon))
        
        # image des kopieren buttons welcher den übersetzten Text in die Zwischenablage kopiert
        copy_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/copy_light.png')
        copy_icon_dark = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/copy_dark.png')
        self.copy_image = ctk.CTkImage(light_image=Image.open(copy_icon), dark_image=Image.open(copy_icon_dark), size=(15, 15))
        
        # image des image2text buttons
        image_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/image2text_light.png')
        image_icon_dark = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/image2text_dark.png')
        self.image2text = ctk.CTkImage(light_image=Image.open(image_icon), dark_image=Image.open(image_icon_dark))
        
        # image des Notizen Tabs im Hauptmenu
        notizen_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/notizen.png')
        notizen_icon_dark = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/notizen_dark.png')
        self.notizen_icon = ctk.CTkImage(light_image=Image.open(notizen_icon), dark_image=Image.open(notizen_icon_dark), size=(30, 30))

        # image des Übersetzer Tabs im Hauptmenu
        translator_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/übersetzer.png')
        translator_icon_dark = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/übersetzer_dark.png')
        self.translator_icon = ctk.CTkImage(light_image=Image.open(translator_icon), dark_image=Image.open(translator_icon_dark), size=(30, 30))
        
        # image zum entfernen einzelner Notizen
        delete_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/delete_button.png')
        self.delete_button_image = ctk.CTkImage(light_image=Image.open(delete_icon), dark_image=Image.open(delete_icon), size=(12, 12))
        
    def setup_frames(self):
        self.note_frame = Notes(self, self.notes_font, self.frame_bg_color, self.button_color_hover, self.add_button_image, self.delete_button_image)
        self.note_frame.pack_forget()
        self.text_multi_frame = TextMulti(
            self,
            self.button_font_small,
            self.textbox_font,
            self.button_color_hover,
            self.frame_bg_color,
            self.frame_bg_color_invert,
            self.button_font_color,
            self.copy_image,
            self.image2text,
            self.add_button_image
            )
        self.text_multi_frame.pack_forget()
        TopMenu(self, self.button_font, self.button_color_hover,
                self.button_font_small, self.textbox_font,
                self.text_multi_frame, self.note_frame, self.frame_bg_color,
                self.notizen_icon, self.translator_icon)
        TopSeparator(self)
        self.note_frame.pack(expand=True, fill="both")

    # Funktion zum Ändern Titelleiste je nachdem ob ein dunkles oder helles Thema ausgewählt ist
    def title_bar_color(self, is_dark):
        try:
            hwnd = windll.user32.GetParent(self.winfo_id())
            dwmwa_attribute = 35
            text_dwmwa_attribute = 36
            color = 0x00191919 if is_dark else 0x00f3f3f3
            text_color = 0x005d5d5d if is_dark else 0x00000000
            windll.dwmapi.DwmSetWindowAttribute(hwnd, dwmwa_attribute, byref(c_int(color)), sizeof(c_int))
            windll.dwmapi.DwmSetWindowAttribute(hwnd, text_dwmwa_attribute, byref(c_int(text_color)), sizeof(c_int))
        except:
            pass


class TopMenu(ctk.CTkFrame):
    def __init__(self, parent, button_font, button_color_hover,
                 button_font_small,textbox_font, text_multi_frame, note_frame, frame_bg_color, notizen_icon, translator_icon):
        super().__init__(parent, fg_color=frame_bg_color, corner_radius=0)
        self.pack(fill="x", ipady=10)

        # define top menu grid
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")

        # Eingaben aus der Hauptklasse (App)
        self.button_font = button_font
        self.button_font_small = button_font_small
        self.textbox_font = textbox_font
        self.button_color_hover = button_color_hover
        self.frame_bg_color = frame_bg_color
        self.text_multi_frame = text_multi_frame
        self.note_frame = note_frame
        self.notizen_icon = notizen_icon
        self.translator_icon = translator_icon

        # place widgets
        self.create_top_menu_widgets()

    def create_top_menu_widgets(self):
        # notes button
        MainMenuButton(parent=self,
                       column=0,
                       row=0,
                       text="Notizen",
                       corner_radius=0,
                       padx=0,
                       sticky="nsew",
                       image=self.notizen_icon,
                       font=self.button_font,
                       hover_color=self.button_color_hover,
                       command=self.menu_func_notes
                       )

        # translator button
        MainMenuButton(parent=self,
                       column=1,
                       row=0,
                       text="Übersetzer",
                       corner_radius=0,
                       padx=0,
                       sticky="nsew",
                       image=self.translator_icon,
                       font=self.button_font,
                       hover_color=self.button_color_hover,
                       command=self.menu_func_text_multi
                       )

    # versteckt das note_frame und zeigt das text_multi_frame an
    def menu_func_text_multi(self):
        self.note_frame.pack_forget()
        self.text_multi_frame.pack(expand=True, fill="both")

    # versteckt das text_multi_frame und zeigt das note_frame an
    def menu_func_notes(self):
        self.text_multi_frame.pack_forget()
        self.note_frame.pack(expand=True, fill="both")


class TopSeparator(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color=("black", "#5d5d5d"), height=1)
        self.pack(fill="x")


class Notes(ctk.CTkFrame):
    def __init__(self, parent, notes_font, frame_bg_color, button_color_hover, add_button_image, delete_button_image):
        super().__init__(parent, fg_color=frame_bg_color)
        self.pack(expand=True, fill="both")

        # Diese StringVariable setzt den initial Wert des Entry Feldes
        self.entry_str = ctk.StringVar(value="")
        self.count = 0
        self.notes_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'notizen.txt')

        # Frames
        EntryFrame(self,self.add_task, self.entry_str, frame_bg_color, button_color_hover, add_button_image)
        self.tasks_frame = TasksFrame(self, self.delete_task, notes_font, frame_bg_color, delete_button_image)
        self.read_notes_text_at_start()

    def read_notes_text_at_start(self):
        with open(self.notes_file, "r") as file:
            # Prüfe, ob die Datei nicht leer ist
            if file.readable() and not file.read().isspace():
                # Setze den Dateizeiger auf den Anfang der Datei zurück
                file.seek(0)

            # Iteriere über die Zeilen der Datei
            for i in file:
                self.tasks_frame.update_tasks(i.strip(), self.count)
                self.count += 1  # wird erhöht damit die Notizen in verschiedenen rows erstellt werden

    def add_task(self):
        # Beim Klicken auf den entry_button wird diese Methode ausgeführt
        new_task = self.entry_str.get()  # Der Inhalt des Entry feldes wird ausgelesen
        if new_task:  # prüfen ob das Entry Feld nicht leer ist
            # Öffne die Datei im Schreibmodus (falls die Datei nicht existiert, wird sie erstellt)
            with open(self.notes_file, "a") as file:
                # Schreibe die neue Notiz in die Datei
                #file.write(f"{new_task};{self.tasks_frame.checkbox_get_status()} \n")
                file.write(f"{new_task}\n")

            self.entry_str.set("")  # das Entry Feld wird wieder geleert
            self.tasks_frame.update_tasks(new_task, self.count)
            self.count += 1  # wird erhöht damit die Notizen in verschiedenen rows erstellt werden

    def delete_task(self, frame, new_task):
        # Entferne den Eintrag aus der Datei
        self.remove_task_from_file(new_task)

        # Zerstören des Frames
        frame.destroy()

    def remove_task_from_file(self, new_task):
        # alle Zeilen der Datei werden gelesen und in die Liste lines hinzugefügt
        with open(self.notes_file, "r") as file:
            lines = file.readlines()

        # durch die lines iterieren, Zeilen mit task überspringen den rest in eine neue Datei schreiben
        with open(self.notes_file, "w") as file:
            for line in lines:
                if line.strip() != new_task:
                    file.write(line)


class TextMulti(ctk.CTkFrame):
    def __init__(self, parent, button_font_small, textbox_font, button_color_hover, frame_bg_color, frame_bg_color_invert, button_font_color, copy_image, image2text, add_button_image):
        super().__init__(parent, fg_color=frame_bg_color, corner_radius=0)
        self.pack(expand=True, fill="both")

        self.entry_str = ctk.StringVar(value="")
        
        # font Eingaben
        self.button_font_small = button_font_small
        self.textbox_font = textbox_font

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

        # grid definieren
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="b")
        self.rowconfigure(1, weight=1, uniform="b")
        self.rowconfigure(2, weight=1, uniform="b")
        self.rowconfigure(3, weight=100, uniform="c")

        self.create_widgets()

        self.translator = Translator()

    def create_widgets(self):
        
        test = EntryFrame(self,self.translate_text, self.entry_str, self.frame_bg_color, self.button_color_hover, self.add_button_image)
        test.pack_forget()
        test.grid(column=0, columnspan=2, row=0, sticky="w", padx=0, pady=0)
        
        # übersetzen button
        Button(
            parent=self,
            text="Übersetzen",
            func=self.translate_text,
            col=0,
            row=1,
            fg_color=self.button_color,
            hover_color=self.button_color_hover,
            text_color=self.button_font_color,
            font=self.button_font_small
        )

        # box leeren button
        Button(
            parent=self,
            text="Leeren",
            func=self.empty_box,
            col=1,
            row=1,
            fg_color=self.button_color,
            hover_color=self.button_color_hover,
            text_color=self.button_font_color,
            font=self.button_font_small
        )

        # imagetotext button
        Button(
            parent=self,
            text="",
            func=self.imagefunk,
            col=1,
            row=2,
            fg_color=self.button_color,
            hover_color=self.button_color_hover,
            text_color=self.button_font_color,
            font=self.button_font_small,
            image=self.image2text
        )

        self.textbox = TextboxGrid(
            parent=self,
            corner_radius=0,
            height=300,
            font=self.textbox_font,
            fg_color=self.frame_bg_color,
            bg_color=self.frame_bg_color_invert,
            column=0,
            columnspan=2,
            row=3,
            sticky="nsew",
            pady=0,
            padx=0,
            text_color=self.frame_bg_color_invert
        )

        self.copy_button = Button(
            parent=self,
            text="",
            func=self.copy_clipboard,
            col=0,
            row=2,
            fg_color=self.button_color,
            hover_color=self.button_color_hover,
            text_color=self.button_font_color,
            font=self.button_font_small,
            state=ctk.DISABLED,
            image=self.copy_image
        )

    def translate_text(self):
        self.textbox.delete("1.0", tk.END)
        
        # prüfen ob entry feld nicht leer ist, wenn wahr dann wird der inhalt übersetzt
        # wenn unwahr wird die zwischenablage geprüft
        if self.entry_str.get():
            result = self.translator.translate(self.entry_str.get(), dest="de").text
        elif self.clipboard_get():
            result = self.translator.translate(self.clipboard_get(), dest="de").text
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
            image = Image.open(name)
            string = pytesseract.image_to_string(image)
            test = string
            self.textbox.insert(tk.END, test)
            self.copy_button.configure(state=ctk.NORMAL)
            pyperclip.copy(self.textbox.get("1.0", tk.END))


if __name__ == "__main__":
    App("", (300, 450), darkdetect.isDark())
