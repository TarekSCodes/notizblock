import customtkinter as ctk
from buttons import*


# beinhaltet das Entry Feld und den hinzufügen Button
class EntryFrame(ctk.CTkFrame):
    def __init__(self, parent, add_task, entry_string, frame_bg_color):
        super().__init__(parent, corner_radius=0, fg_color=frame_bg_color)
        self.pack(fill="x")
        
        self.frame_bg_color = frame_bg_color

        # Entry zum Eingeben der Aufgaben
        entry = ctk.CTkEntry(self, textvariable=entry_string, corner_radius=5, border_width=1, width=200)
        entry.pack(side="left", padx=10, pady=5)

        # Button zum Hinzufügen der Aufgaben - führt beim klicken die Methode
        # add_task aus welche in der Klasse Notes deklariert und beim Aufruf
        # an die EntryFrame Klasse übergeben wird
        ButtonPack(self, 20, 20, "blue", "red", add_task, "+", 0, anchor=None, side="left")


# Klasse zum Hinzufügen von neuen Notizzetteln
# dies ist das Parent Frame für alle Notizen unter dem Entry Feld
class TasksFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, delete_task, notes_font, frame_bg_color):
        super().__init__(parent, corner_radius=0, fg_color=frame_bg_color)
        self.pack(fill="both", expand=True)

        self.columnconfigure(0, weight=1, uniform="a")
        
        self.frame_bg_color = frame_bg_color
        self.delete_task = delete_task
        self.notes_font = notes_font

    # wird vom hinzufügen button getriggert
    # erstellt für jeden neuen task_list Eintrag ein Frame, welches
    # ein label mit dem listen Eintrag und zwei buttons enthält
    def update_tasks(self, new_task, count):
        if new_task:
            
            # Das Main Frame der einzelnen Notiz
            single_note_frame = NormalGridFrame(self, 0, self.frame_bg_color, 0, count, "nsew")
 
            single_note_frame.columnconfigure(0, weight=10, uniform="a")  # Das Grid des Frames definieren - in column 0 befindet sich die text_box
            single_note_frame.columnconfigure(1, weight=1, uniform="a")  # In column 1 befindet sich das Frame für die beiden Buttons jeder Notiz - notes_button_frame

            # Das Textfeld der Notiz
            text_box = ctk.CTkTextbox(
                single_note_frame, font=self.notes_font,
                height=60, fg_color="#efb640",
                text_color="black", corner_radius=5)
            text_box.insert("end", new_task)  # Hier wird die Eingabe aus dem Entry Feld in die text_box geschieben
            text_box.grid(column=0, row=count, sticky="ew", pady=5, padx=10)

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
