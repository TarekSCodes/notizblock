from customtkinter import CTkFont
# Colors Buttons
BUTTON_COLOR_HOVER = ("#dadada", "#2c2c2c")
BUTTON_FONT_COLOR = ("#2c2c2c", "#5e5e5e")
ABOUT_BUTTON_FONT_COLOR = "grey"

# Colors Frames
FRAME_BACKGROUND_COLOR = ("#f3f3f3", "#191919")
FRAME_BACKGROUND_COLOR_INVERT = ("#191919", "#f3f3f3")

# Colors Notizzettel
NOTIZ_ZETTEL_BACKGROUND_COLOR = "#efb640"
NOTIZ_ZETTEL_TEXT_COLOR = "black"
NOTIZ_DELETE_BUTTON_BACKGROUND_COLOR = "#efb640"
NOTIZ_DELETE_BUTTON_HOVER_COLOR = "#ff0000"


# Images


# Fonts
BUTTON_FONT = None
BUTTON_FONT_SMALL = None
TEXTBOX_NOTES_FONT = None

def initaliziereFonts():
    global BUTTON_FONT, BUTTON_FONT_SMALL, BUTTON_FONT_COLOR, TEXTBOX_NOTES_FONT
    BUTTON_FONT = CTkFont("Calibre", 22, weight="bold")
    BUTTON_FONT_SMALL = CTkFont("Calibre", 18, weight="bold")
    TEXTBOX_NOTES_FONT = CTkFont("calibre", 20)