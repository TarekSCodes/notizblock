import customtkinter as ctk


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