import customtkinter as ctk
from tkinter import messagebox

class TextboxGrid(ctk.CTkTextbox):
    def __init__(self, parent, corner_radius, height, font, fg_color, bg_color, column, columnspan, row, sticky, pady, padx, text_color):
        super().__init__(
            parent,
            corner_radius=corner_radius,
            height=height,
            font=font,
            fg_color=fg_color,
            bg_color=bg_color,
            text_color=text_color
            )
        self.grid(column=column, columnspan=columnspan, row=row, sticky=sticky, pady=pady, padx=padx)


class EntryFieldPack(ctk.CTkEntry):
    def __init__(self, parent, textvariable, corner_radius, border_width, width, height, side, padx, pady, font):
        super().__init__(
            master=parent,
            textvariable=textvariable,
            corner_radius=corner_radius,
            border_width=border_width,
            width=width,
            height=height,
            font=font
            )
        self.pack(side=side, padx=padx, pady=pady)
