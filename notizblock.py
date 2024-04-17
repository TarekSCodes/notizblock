import customtkinter as ctk
import const
import darkdetect
from frames import *
from NotesClass import *
from TextMultiClass import TextMulti
from TopMenuClass import TopMenu
import os
from PIL import Image
import pyperclip
import pytesseract
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

        const.initaliziereFonts()
        self.setup_window(title, is_dark)  # Window Setup
        self.setup_images()
        self.setup_frames()
        
        self.about_window = None

        self.mainloop()

    def setup_window(self, title, is_dark):
        self.title(title)
        #icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images/hamster.ico')
        #self.iconbitmap(icon_path)
        window_width = 400
        window_height = 650
        center_width = int((self.winfo_screenwidth() - window_width) / 2)
        center_height = int((self.winfo_screenheight() - window_height) / 2)
        self.geometry(f"{window_width}x{window_height}+{center_width}+{center_height}")
        self.attributes("-topmost", True)
        self.minsize(400, 650)
        self.maxsize(1000, 1000)
        self.title_bar_color(is_dark)

    def setup_images(self):
        image25 = (25, 25)
        image_size_topmenu = (35, 35)
        
        # image des add buttons zum hinzufügen von Notizen
        add_icon = 'images\\add_button.png'
        add_icon_light = 'images\\add_button_light.png'
        self.add_button_image = ctk.CTkImage(light_image=Image.open(add_icon_light), dark_image=Image.open(add_icon), size=(30, 30))
        
        # image des kopieren buttons welcher den übersetzten Text in die Zwischenablage kopiert
        copy_icon = 'images\\copy_light.png'
        copy_icon_dark = 'images\\copy_dark.png'
        self.copy_image = ctk.CTkImage(light_image=Image.open(copy_icon), dark_image=Image.open(copy_icon_dark), size=image25)
        
        # image des image2text buttons
        image_icon = 'images\\image2text_light.png'
        image_icon_dark = 'images\\image2text_dark.png'
        self.image2text = ctk.CTkImage(light_image=Image.open(image_icon), dark_image=Image.open(image_icon_dark), size=image25)
        
        # image des Notizen Tabs im Hauptmenu
        notizen_icon = 'images\\notizen.png'
        notizen_icon_dark = 'images\\notizen_dark.png'
        self.notizen_icon = ctk.CTkImage(light_image=Image.open(notizen_icon), dark_image=Image.open(notizen_icon_dark), size=image_size_topmenu)

        # image des Übersetzer Tabs im Hauptmenu
        translator_icon = 'images\\übersetzer.png'
        translator_icon_dark = 'images\\übersetzer_dark.png'
        self.translator_icon = ctk.CTkImage(light_image=Image.open(translator_icon), dark_image=Image.open(translator_icon_dark), size=image_size_topmenu)
        
        # image zum entfernen einzelner Notizen
        delete_icon = 'images\\delete_button.png'
        self.delete_button_image = ctk.CTkImage(light_image=Image.open(delete_icon), dark_image=Image.open(delete_icon), size=(15, 15))
        
    def setup_frames(self):
        self.note_frame = Notes(
            parent=self,
            add_button_image=self.add_button_image,
            delete_button_image=self.delete_button_image,
            about_func=self.about_func
        )
        self.note_frame.pack_forget()
        
        self.text_multi_frame = TextMulti(
            self,
            self.copy_image,
            self.image2text,
            self.add_button_image,
            self.about_func
            )
        self.text_multi_frame.pack_forget()
        
        TopMenu(
            self,
            self.text_multi_frame,
            self.note_frame,
            self.notizen_icon,
            self.translator_icon
            )
        
        TopSeparator = ctk.CTkFrame(
            master=self,
            corner_radius=0,
            fg_color=("black", "#5d5d5d"),
            height=1)
        TopSeparator.pack(fill="x")
        
        
        self.note_frame.pack(expand=True, fill="both")

    def about_func(self):
        if self.about_window is None or not self.about_window.winfo_exists():
            self.about_window = ctk.CTkToplevel(self)
            self.about_window.title("About")
            self.about_window.focus()
            self.about_window.geometry("300x300")
        else:
            self.about_window.focus()

    def title_bar_color(self, is_dark):
        """Funktion zum Ändern Titelleiste je nachdem ob ein dunkles oder helles Thema ausgewählt ist"""
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


if __name__ == "__main__":
    App("", darkdetect.isDark())
    