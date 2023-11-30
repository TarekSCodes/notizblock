import customtkinter as ctk

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
