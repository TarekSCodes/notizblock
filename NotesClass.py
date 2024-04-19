import customtkinter as ctk
import const
from notizblock import EntryFrame, TasksFrame, NormalPackFrame
from NotizModel import NotizModel as NM
from TextDatenVerbindung import TextDatenVerbindung as TDV
import os

class Notes(ctk.CTkFrame):
    def __init__(self, parent, about_func):
        super().__init__(parent)
        self.pack(expand=True, fill="both")

        # Diese StringVariable setzt den initial Wert des Entry Feldes
        self.entry_str = ctk.StringVar(value="")
        self.count = 0
        self.notes_file = 'notes'
        
        # Eingaben
        self.about_func = about_func

        # Frames
        self.create_widgets()
        
        # Methode zum auslesen der notizen.txt Datei ausführen
        self.read_notes_text_at_start()

    def create_widgets(self):
        EntryFrame(self, self.erstelleNotizButton_Geklickt, self.entry_str)
        self.tasks_frame = TasksFrame(self, self.delete_task)
        NormalPackFrame(
            parent=self,
            corner_radius=0,
            fill="x",
            height=50,
            about_func=self.about_func)
    
    # TODO
    # Beim starten der App die Notizen Datei auslesen, Zeilen in
    # in NotizModel Objekte umwandeln und in die GUI laden
    def read_notes_text_at_start(self):
        for i in os.listdir(self.notes_file):
            file_path = f"{self.notes_file}/{i}"
            with open(file_path, "r") as file:  # Liest die Textdateien aus
                file_content = file.read().strip()
                text_box_id = self.tasks_frame.update_tasks(file_content)  # erstellt daraus einen neue Notiz 
     
            os.remove(file_path)  # löscht die alte Textdatei

            new_file_path = f"{self.notes_file}/{text_box_id}.txt"
            with open(new_file_path, "w") as new_file:
                new_file.write(file_content)  # schreibt den Inhalt der Notiz in eine neue Datei
    
    # TODO
    # 
    def erstelleNotizButton_Geklickt(self):
        # Beim Klicken auf den entry_button wird diese Methode ausgeführt
        new_task = self.entry_str.get()  # Der Inhalt des Entry feldes wird ausgelesen
        
        if new_task:  # prüfen ob das Entry Feld nicht leer ist
            
            TDV.ErstelleNotiz(NM(1, new_task))
            
            text_box_id = self.tasks_frame.update_tasks(new_task) 
            
            self.entry_str.set("")  # das Entry Feld wird wieder geleert
            
    def delete_task(self, frame, text_box_id):
        try:
            # Zerstören des Frames
            frame.destroy()
            
            # Entferne den Eintrag aus der Datei
            self.remove_task_from_file(text_box_id)

        except Exception as e:
            print(f"Ein Fehler ist aufgetreten in delete_task: {e}")

    def remove_task_from_file(self, text_box_id):
        try:
            # Entfernen der txt Datei
            unwanted_file = f"{self.notes_file}/{text_box_id}.txt"
            os.remove(unwanted_file)
            
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten in remove_task_from_file: {e}")