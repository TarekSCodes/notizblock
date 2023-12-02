import customtkinter as ctk
from buttons import*
from text_entry import *


# beinhaltet das Entry Feld und den hinzufügen Button
class EntryFrame(ctk.CTkFrame):
    def __init__(self, parent, add_task, entry_string, frame_bg_color, button_color_hover, add_button_image):
        super().__init__(parent, corner_radius=0, fg_color=frame_bg_color)
        self.pack(fill="x")
        
        # Eingaben
        self.add_task = add_task
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
        ButtonPack(self, 20, 20, self.frame_bg_color, self.button_color_hover, self.add_task, "", 0, anchor=None, side="left", image=self.add_button_image)


# Klasse zum Hinzufügen von neuen Notizzetteln
# dies ist das Parent Frame für alle Notizen unter dem Entry Feld
class TasksFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, delete_task, notes_font, frame_bg_color):
        super().__init__(parent, corner_radius=0, fg_color=frame_bg_color)
        self.pack(fill="both", expand=True)

        # grid definieren
        self.columnconfigure(0, weight=1, uniform="a")
        
        # Eingaben
        self.frame_bg_color = frame_bg_color
        self.delete_task = delete_task
        self.notes_font = notes_font

    # wird vom hinzufügen button getriggert erstellt für jeden neuen task_list Eintrag ein Frame,
    # welches ein label mit dem listen Eintrag und zwei buttons enthält
    def update_tasks(self, new_task, count):
        if new_task:
            
            # Das Main Frame der einzelnen Notiz
            single_note_frame = NormalGridFrame(self, 0, self.frame_bg_color, 0, count, "nsew")
 
            single_note_frame.columnconfigure(0, weight=10, uniform="a")  # Das Grid des Frames definieren - in column 0 befindet sich die text_box
            single_note_frame.columnconfigure(1, weight=1, uniform="a")  # In column 1 befindet sich das Frame für die beiden Buttons jeder Notiz - notes_button_frame

            # Das Textfeld der Notiz
            text_box = TextboxGrid(
                parent=single_note_frame,
                corner_radius=5,
                height=60,
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

            # Das Frame was beide Buttons beinhaltet
            notes_button_frame = NormalGridFrame(parent=single_note_frame, corner_radius=0, fg_color=self.frame_bg_color, column=1, row=count, sticky="nsew")

            # Button zum Setzen der Notiz auf "Erledigt"
            CheckButton(notes_button_frame,"", "green", 20, 20, 1, "#5e5e5e", "green")

            # Button zum Entfernen der Notiz
            ButtonPack(notes_button_frame, 20, 20, "#970000", "#ff0000", lambda: self.delete_task(single_note_frame, new_task), "x", "5", "w")


class NormalGridFrame(ctk.CTkFrame):
    def __init__(self, parent, corner_radius, fg_color, column, row, sticky):
        super().__init__(parent, corner_radius=corner_radius, fg_color=fg_color)
        self.grid(column=column, row=row, sticky=sticky)
