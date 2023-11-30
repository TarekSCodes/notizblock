import customtkinter as ctk
from customtkinter.windows.widgets.font import CTkFont
from customtkinter.windows.widgets.image import CTkImage


# Buttons des Hauptmenüs
class MainMenuButton(ctk.CTkButton):
    def __init__(self, parent, column, row, text, corner_radius,
                 padx, sticky, font, hover_color, command, image=None):
        super().__init__(
            master=parent,
            text=text,
            corner_radius=corner_radius,
            image=image,
            fg_color=("#f3f3f3", "#191919"),
            font=font,
            text_color=("black", "#5d5d5d"),
            hover_color=hover_color,
            command=command
        )
        self.grid(column=column, row=row, padx=padx, sticky=sticky)


# Übersetzer Buttons
class Button(ctk.CTkButton):
    def __init__(self, parent, text, func, col, row, fg_color, hover_color, text_color, font, image=None,
                 state=ctk.NORMAL, corner_radius=0):
        super().__init__(
            master=parent,
            text=text,
            command=func,
            corner_radius=corner_radius,
            font=font,
            fg_color=fg_color,
            hover_color=hover_color,
            text_color=text_color,
            state=state,
            image=image
        )
        self.grid(column=col, row=row, sticky="nsew")
        

class CheckButton(ctk.CTkCheckBox):
        def __init__(self, parent, text, fg_color, checkbox_height, checkbox_width, border_width, border_color, hover_color):
            super().__init__(
                master=parent,
                text=text,
                fg_color=fg_color,
                checkbox_height=checkbox_height,
                checkbox_width=checkbox_width,
                border_width=border_width,
                border_color=border_color,
                hover_color=hover_color
            )
            self.pack(pady=5, anchor="w")


class ButtonPack(ctk.CTkButton):
    def __init__(self, parent, width, height, fg_color, hover_color, func, text, pady, anchor=None, side=None):
        super().__init__(
            master=parent,
            width=width,
            height=height,
            fg_color=fg_color,
            hover_color=hover_color,
            command=func,
            text=text
        )
        self.pack(pady=pady, anchor=anchor, side=side)