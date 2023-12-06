import customtkinter as ctk
from buttons import*
from text_entry import *


# beinhaltet das Entry Feld und den hinzufügen Button
class EntryFrame(ctk.CTkFrame):
    def __init__(self, parent, func, entry_string, frame_bg_color, button_color_hover, add_button_image):
        super().__init__(parent, corner_radius=0, fg_color=frame_bg_color)
        self.pack(fill="x")
        
        # Eingaben
        self.command = func
        self.entry_string = entry_string
        self.frame_bg_color = frame_bg_color
        self.button_color_hover = button_color_hover
        self.add_button_image = add_button_image
        
        self.create_widgets()

    def create_widgets(self):
        # Entry zum Eingeben der Aufgaben
        EntryFieldPack(self, self.entry_string, 5, 1, 200, "left", 10, 5)
        
        # Button zum Hinzufügen der Aufgaben - führt beim klicken die Methode add_task aus welche in
        # der Klasse Notes deklariert und beim Aufruf an die EntryFrame Klasse übergeben wird
        ButtonPack(self, 20, 20, self.frame_bg_color, self.button_color_hover, self.command, 5, "", 0, anchor=None, side="left", image=self.add_button_image)
    
# Klasse zum Hinzufügen von neuen Notizzetteln
# dies ist das Parent Frame für alle Notizen unter dem Entry Feld
class TasksFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, delete_task, notes_font, frame_bg_color, delete_button_image):
        super().__init__(parent, corner_radius=0, fg_color=frame_bg_color)
        self.pack(fill="both", expand=True)

        # grid definieren
        self.columnconfigure(0, weight=1, uniform="a")
        
        # Eingaben
        self.frame_bg_color = frame_bg_color
        self.delete_task = delete_task
        self.notes_font = notes_font
        self.delete_button_image = delete_button_image

    # wird vom hinzufügen button getriggert erstellt für jeden neuen task_list Eintrag ein Frame,
    # welches ein label mit dem listen Eintrag und zwei buttons enthält
    def update_tasks(self, new_task, count):
        if new_task:
            
            # Das Main Frame der einzelnen Notiz
            single_note_frame = NormalGridFrame(
                parent=self,
                corner_radius=5,
                fg_color=self.frame_bg_color,
                column=0,
                row=count,
                sticky="nsew"
            )
 
            single_note_frame.columnconfigure(0, weight=1, uniform="a")

            # Das Textfeld der Notiz
            text_box = TextboxGrid(
                parent=single_note_frame,
                corner_radius=5,
                height=100,
                font=self.notes_font,
                fg_color="#efb640",
                bg_color=self.frame_bg_color,
                column=0,
                columnspan=1,
                row=count,
                sticky="ew",
                pady=5,
                padx=10,
                text_color="black"
            )
            text_box.insert("end", new_task)  # Hier wird die Eingabe aus dem Entry Feld in die text_box geschieben

            ButtonPlace(
                parent=single_note_frame,
                width=10,
                height=10,
                fg_color="#efb640",
                bg_color="#efb640",
                hover_color="#ff0000",
                func=lambda: self.delete_task(single_note_frame, new_task),
                corner_radius=5,
                text="",
                rely=0.92,
                relx=0.95,
                anchor="se",
                image=self.delete_button_image
            )

class NormalGridFrame(ctk.CTkFrame):
    def __init__(self, parent, corner_radius, fg_color, column, row, sticky):
        super().__init__(parent, corner_radius=corner_radius, fg_color=fg_color)
        self.grid(column=column, row=row, sticky=sticky)
