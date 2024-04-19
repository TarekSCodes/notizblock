from customtkinter import CTkFont, CTkImage
from PIL import Image

# Colors Buttons
BUTTON_COLOR_HOVER = ("#dadada", "#2c2c2c")
BUTTON_FONT_COLOR = ("#2c2c2c", "#5e5e5e")
ABOUT_BUTTON_FONT_COLOR = "grey"
TOP_MENU_BUTTON_FONT_COLOR = ("black", "#5d5d5d")


# Colors Frames
FRAME_BACKGROUND_COLOR = ("#f3f3f3", "#191919")
FRAME_BACKGROUND_COLOR_INVERT = ("#191919", "#f3f3f3")


# Colors Notizzettel
NOTIZ_ZETTEL_BACKGROUND_COLOR = "#efb640"
NOTIZ_ZETTEL_TEXT_COLOR = "black"
NOTIZ_DELETE_BUTTON_BACKGROUND_COLOR = "#efb640"
NOTIZ_DELETE_BUTTON_HOVER_COLOR = "#ff0000"


# Images
IMAGE25 = (25,25)
IMAGE_SIZE_TOPMENU = (35,35)

# image des add buttons zum hinzufügen von Notizen
ADD_ICON = 'images\\add_button.png'
ADD_ICON_LIGHT = 'images\\add_button_light.png'
ADD_BUTTON_IMAGE = CTkImage(light_image=Image.open(ADD_ICON_LIGHT), dark_image=Image.open(ADD_ICON), size=(30, 30))

# image des kopieren buttons welcher den übersetzten Text in die Zwischenablage kopiert
COPY_ICON = 'images\\copy_light.png'
COPY_ICON_DARK = 'images\\copy_dark.png'
COPY_IMAGE = CTkImage(light_image=Image.open(COPY_ICON), dark_image=Image.open(COPY_ICON_DARK), size=IMAGE25)

# image des image2text buttons
IMAGE_ICON = 'images\\image2text_light.png'
IMAGE_ICON_DARK = 'images\\image2text_dark.png'
IMAGE2TEXT = CTkImage(light_image=Image.open(IMAGE_ICON), dark_image=Image.open(IMAGE_ICON_DARK), size=IMAGE25)

# image des Notizen Tabs im Hauptmenu
NOTIZEN_ICON = 'images\\notizen.png'
NOTIZEN_ICON_DARK = 'images\\notizen_dark.png'
NOTIZEN_ICON_IMAGE = CTkImage(light_image=Image.open(NOTIZEN_ICON), dark_image=Image.open(NOTIZEN_ICON_DARK), size=IMAGE_SIZE_TOPMENU)

# image des Übersetzer Tabs im Hauptmenu
TRANSLATOR_ICON = 'images\\übersetzer.png'
TRANSLATOR_ICON_DARK = 'images\\übersetzer_dark.png'
TRANSLATOR_ICON_IMAGE = CTkImage(light_image=Image.open(TRANSLATOR_ICON), dark_image=Image.open(TRANSLATOR_ICON_DARK), size=IMAGE_SIZE_TOPMENU)

# image zum entfernen einzelner Notizen
DELETE_ICON = 'images\\delete_button.png'
DELETE_ICON_IMAGE = CTkImage(light_image=Image.open(DELETE_ICON), dark_image=Image.open(DELETE_ICON), size=(15, 15))


# Fonts
BUTTON_FONT = None
BUTTON_FONT_SMALL = None
TEXTBOX_NOTES_FONT = None

def initaliziereFonts():
    global BUTTON_FONT, BUTTON_FONT_SMALL, BUTTON_FONT_COLOR, TEXTBOX_NOTES_FONT
    BUTTON_FONT = CTkFont("Calibre", 22, weight="bold")
    BUTTON_FONT_SMALL = CTkFont("Calibre", 18, weight="bold")
    TEXTBOX_NOTES_FONT = CTkFont("calibre", 20)