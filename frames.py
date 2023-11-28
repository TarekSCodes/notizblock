import customtkinter as ctk


# beinhaltet das Entry Feld und den hinzufügen Button
class EntryFrame(ctk.CTkFrame):
    def __init__(self, parent, add_task, entry_string):
        super().__init__(parent, corner_radius=0, fg_color=("white", "#191919"))
        self.pack(fill="x")

        # Entry zum Eingeben der Aufgaben
        entry = ctk.CTkEntry(self, textvariable=entry_string, corner_radius=5, border_width=1, width=200)
        entry.pack(side="left", padx=10, pady=5)

        # Button zum Hinzufügen der Aufgaben - führt beim klicken die Methode
        # add_task aus welche in der Klasse Notes deklariert und beim Aufruf
        # an die EntryFrame Klasse übergeben wird
        entry_button = ctk.CTkButton(
            self, text="+",
            command=add_task, width=20, height=20)
        entry_button.pack(side="left")


# Klasse zum Hinzufügen von neuen Notizzetteln
# dies ist das Parent Frame für alle Notizen unter dem Entry Feld
class TasksFrame(ctk.CTkScrollableFrame):
    def __init__(self, parent, delete_task, notes_font):
        super().__init__(parent, corner_radius=0, fg_color=("white", "#191919"))
        self.check_button = ctk.CTkCheckBox(self)
        self.pack(fill="both", expand=True)

        self.columnconfigure(0, weight=1, uniform="a")
        self.delete_task = delete_task
        self.notes_font = notes_font

    # wird vom hinzufügen button getriggert
    # erstellt für jeden neuen task_list Eintrag ein Frame, welches
    # ein label mit dem listen Eintrag und zwei buttons enthält
    def update_tasks(self, new_task, count):
        if new_task:
            # Das Main Frame der einzelnen Notiz
            single_note_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=("white", "#191919"))
            single_note_frame.grid(column=0, row=count, sticky="nsew")

            # Das Grid des Frames definieren - in column 0 befindet sich die text_box
            single_note_frame.columnconfigure(0, weight=10, uniform="a")
            # In column 1 befindet sich das Frame für die beiden Buttons jeder Notiz - button_frame
            single_note_frame.columnconfigure(1, weight=1, uniform="a")

            # Das Textfeld der Notiz
            text_box = ctk.CTkTextbox(
                single_note_frame, font=self.notes_font,
                height=60, fg_color="#efb640",
                text_color="black", corner_radius=5)
            text_box.insert("end", new_task)  # Hier wird die Eingabe aus dem Entry Feld in die text_box geschieben
            text_box.grid(column=0, row=count, sticky="ew", pady=5, padx=10)

            # Das Frame was beide Buttons beinhaltet
            button_frame = ctk.CTkFrame(single_note_frame, corner_radius=0, fg_color=("white", "#191919"))
            button_frame.grid(column=1, row=count, sticky="nsew")

            # Button zum Setzen der Notiz auf "Erledigt"
            self.check_button = ctk.CTkCheckBox(
                button_frame, text="", fg_color="green",
                checkbox_height=20, checkbox_width=20,
                border_width=1, border_color="#5e5e5e",
                hover_color="green")
            self.check_button.pack(pady=5, anchor="w")

            # Button zum Entfernen der Notiz
            delete_button = ctk.CTkButton(
                button_frame, text="X", fg_color="#970000",
                height=20, width=20, hover_color="#ff0000",
                command=lambda: self.delete_task(single_note_frame, new_task))
            delete_button.pack(pady=5, anchor="w")

