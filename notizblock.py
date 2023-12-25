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
#  4. integration von chat gpt
#  5. Wetter Api integrieren

class App(ctk.CTk):
    def __init__(self, title, is_dark):
        super().__init__(fg_color=("#f3f3f3", "#191919"))

        self.setup_window(title, is_dark)  # Window Setup
        self.setup_fonts()
        self.setup_colors()
        self.setup_images()
        self.setup_frames()
        
        self.about_window = None

        self.mainloop()

    def setup_window(self, title, is_dark):
        self.title(title)
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/hamster.ico')
        self.iconbitmap(icon_path)
        window_width = 400
        window_height = 650
        center_width = int((self.winfo_screenwidth() - window_width) / 2)
        center_height = int((self.winfo_screenheight() - window_height) / 2)
        self.geometry(f"{window_width}x{window_height}+{center_width}+{center_height}")
        self.attributes("-topmost", True)
        self.minsize(400, 650)
        self.maxsize(500, 800)
        self.title_bar_color(is_dark)

    def setup_fonts(self):
        # fonts
        self.button_font = ctk.CTkFont("Calibri", 22, weight="bold")
        self.button_font_small = ctk.CTkFont("Calibri", 18, weight="bold")
        self.textbox_notes_font = ctk.CTkFont("calibre", 20)

    def setup_colors(self):
        # colors
        self.button_color_hover = ("#dadada", "#2c2c2c")
        self.frame_bg_color = ("#f3f3f3", "#191919")
        self.frame_bg_color_invert = ("#191919", "#f3f3f3")
        self.button_font_color = ("#2c2c2c", "#5e5e5e")

    def setup_images(self):
        image25 = (25, 25)
        image_size_topmenu = (35, 35)
        
        # image des add buttons zum hinzufügen von Notizen
        add_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/add_button.png')
        add_icon_light = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/add_button_light.png')
        self.add_button_image = ctk.CTkImage(light_image=Image.open(add_icon_light), dark_image=Image.open(add_icon), size=(30, 30))
        
        # image des kopieren buttons welcher den übersetzten Text in die Zwischenablage kopiert
        copy_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/copy_light.png')
        copy_icon_dark = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/copy_dark.png')
        self.copy_image = ctk.CTkImage(light_image=Image.open(copy_icon), dark_image=Image.open(copy_icon_dark), size=image25)
        
        # image des image2text buttons
        image_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/image2text_light.png')
        image_icon_dark = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/image2text_dark.png')
        self.image2text = ctk.CTkImage(light_image=Image.open(image_icon), dark_image=Image.open(image_icon_dark), size=image25)
        
        # image des Notizen Tabs im Hauptmenu
        notizen_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/notizen.png')
        notizen_icon_dark = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/notizen_dark.png')
        self.notizen_icon = ctk.CTkImage(light_image=Image.open(notizen_icon), dark_image=Image.open(notizen_icon_dark), size=image_size_topmenu)

        # image des Übersetzer Tabs im Hauptmenu
        translator_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/übersetzer.png')
        translator_icon_dark = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/übersetzer_dark.png')
        self.translator_icon = ctk.CTkImage(light_image=Image.open(translator_icon), dark_image=Image.open(translator_icon_dark), size=image_size_topmenu)
        
        # image zum entfernen einzelner Notizen
        delete_icon = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/delete_button.png')
        self.delete_button_image = ctk.CTkImage(light_image=Image.open(delete_icon), dark_image=Image.open(delete_icon), size=(15, 15))
        
    def setup_frames(self):
        self.note_frame = Notes(
            self,
            self.textbox_notes_font,
            self.frame_bg_color,
            self.button_color_hover,
            self.add_button_image,
            self.delete_button_image,
            self.button_font_small,
            self.button_font_color,
            self.about_func
        )
        self.note_frame.pack_forget()
        
        self.text_multi_frame = TextMulti(
            self,
            self.button_font_small,
            self.textbox_notes_font,
            self.button_color_hover,
            self.frame_bg_color,
            self.frame_bg_color_invert,
            self.button_font_color,
            self.copy_image,
            self.image2text,
            self.add_button_image,
            self.about_func
            )
        self.text_multi_frame.pack_forget()
        
        TopMenu(self, self.button_font, self.button_color_hover,
                self.button_font_small, self.textbox_notes_font,
                self.text_multi_frame, self.note_frame, self.frame_bg_color,
                self.notizen_icon, self.translator_icon)
        
        TopSeparator(self)
        
        self.note_frame.pack(expand=True, fill="both")

    def about_func(self):
        if self.about_window is None or not self.about_window.winfo_exists():
            self.about_window = ctk.CTkToplevel(self)
            self.about_window.title("About")
            self.about_window.focus()
            self.about_window.geometry("300x300")
        else:
            self.about_window.focus()

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
    def __init__(self, parent, notes_font, frame_bg_color, button_color_hover, add_button_image, delete_button_image, button_font_small, button_font_color, about_func):
        super().__init__(parent, fg_color=frame_bg_color)
        self.pack(expand=True, fill="both")

        # Diese StringVariable setzt den initial Wert des Entry Feldes
        self.entry_str = ctk.StringVar(value="")
        self.count = 0
        self.notes_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'notes')
        
        # Eingaben
        self.button_font_small = button_font_small
        self.notes_font = notes_font
        self.frame_bg_color = frame_bg_color
        self.button_color_hover = button_color_hover
        self.add_button_image = add_button_image
        self.delete_button_image = delete_button_image
        self.button_font_small = button_font_small
        self.button_font_color = button_font_color
        self.about_func = about_func

        # Frames
        self.create_widgets()
        
        # Methode zum auslesen der notizen.txt Datei ausführen
        self.read_notes_text_at_start()

    def create_widgets(self):
        EntryFrame(self, self.add_task, self.entry_str, self.frame_bg_color, self.button_color_hover, self.add_button_image, self.notes_font)
        self.tasks_frame = TasksFrame(self, self.delete_task, self.notes_font, self.frame_bg_color, self.delete_button_image)
        NormalPackFrame(self, 0, self.frame_bg_color, "x", 50, self.button_font_small, self.about_func)
    
    def read_notes_text_at_start(self):
        for i in os.listdir(self.notes_file):
            file_path = f"{self.notes_file}/{i}"
            with open(file_path, "r") as file:  # Liest die Textdateien aus
                file_content = file.read().strip()
                note_id = self.tasks_frame.update_tasks(file_content)  # erstellt daraus einen neue Notiz 
     
            os.remove(file_path)  # löscht die alte Textdatei

            new_file_path = f"{self.notes_file}/{note_id}.txt"
            with open(new_file_path, "w") as new_file:
                new_file.write(file_content)  # schreibt den Inhalt der Notiz in eine neue Datei

    def add_task(self):
        # Beim Klicken auf den entry_button wird diese Methode ausgeführt
        new_task = self.entry_str.get()  # Der Inhalt des Entry feldes wird ausgelesen
        
        if new_task:  # prüfen ob das Entry Feld nicht leer ist
            note_id = self.tasks_frame.update_tasks(new_task) 
              
            # Öffne die Datei im Schreibmodus (falls die Datei nicht existiert, wird sie erstellt)
            with open(f"{self.notes_file}/{note_id}.txt", "w") as file:
                # Schreibe die neue Notiz in die Datei
                file.write(f"{new_task}")

            self.entry_str.set("")  # das Entry Feld wird wieder geleert
            
    def delete_task(self, frame, note_id):
        try:
            # Zerstören des Frames
            frame.destroy()
            
            # Entferne den Eintrag aus der Datei
            self.remove_task_from_file(note_id)

        except Exception as e:
            print(f"Ein Fehler ist aufgetreten in delete_task: {e}")

    def remove_task_from_file(self, note_id):
        try:
            # Entfernen der txt Datei
            unwanted_file = f"{self.notes_file}/{note_id}.txt"
            os.remove(unwanted_file)
            
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten in remove_task_from_file: {e}")
   
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

        self.textbox = TextboxGrid(
            parent=self,
            corner_radius=0,
            height=300,
            font=self.textbox_notes_font,
            fg_color=self.frame_bg_color,
            bg_color=self.frame_bg_color,
            column=0,
            columnspan=2,
            row=3,
            sticky="nsew",
            pady=0,
            padx=0,
            text_color=self.frame_bg_color_invert
        )
        
        ChoiceBox(
            parent=self,
            column=0,
            columnspan=1,
            row=4,
            fg_color=self.frame_bg_color,
            border_width=1,
            values=["deutsch", "englisch", "spanisch"],
            font=self.button_font_small,
            width=120,
            height=30,
            sticky="w",
            padx=10,
            dropdown_fg_color=self.frame_bg_color,
            text_color=self.button_font_color,
            dropdown_font=self.button_font_small,
            variable=self.target_language
        )

        Button(
            parent=self,
            text="About",
            func=self.about_func,
            col=1,
            row=4,
            fg_color=self.frame_bg_color,
            hover_color=self.frame_bg_color,
            text_color="grey",
            font=self.button_font_small,
            sticky="es"
            )
        
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


if __name__ == "__main__":
    App("", darkdetect.isDark())
