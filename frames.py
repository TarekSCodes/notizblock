import customtkinter as ctk

# beinhaltet das Entry Feld und den hinzufügen Button
class EntryFrame(ctk.CTkFrame):
    def __init__(self, parent, func, entry_string, frame_bg_color, button_color_hover, add_button_image, textbox_notes_font):
        super().__init__(parent, corner_radius=0, fg_color=frame_bg_color)
        self.pack(fill="x")
        
        # Eingaben
        self.command = func
        self.entry_string = entry_string
        self.frame_bg_color = frame_bg_color
        self.button_color_hover = button_color_hover
        self.add_button_image = add_button_image
        self.textbox_notes_font = textbox_notes_font
        
        self.create_widgets()

    def create_widgets(self):
        # Entry zum Eingeben der Aufgaben
        ctk.CTkEntry(
            master=self,
            textvariable=self.entry_string,
            corner_radius=5,
            border_width=1,
            width=300,
            height=40,
            font=self.textbox_notes_font
        ).pack(side="left", padx=10, pady=5)
        
        # Button zum Hinzufügen der Aufgaben - führt beim klicken die Methode add_task aus welche in
        # der Klasse Notes deklariert und beim Aufruf an die EntryFrame Klasse übergeben wird
        ctk.CTkButton(
            master=self,
            text="",
            width=20,
            height=40,
            fg_color=self.frame_bg_color,
            hover_color=self.button_color_hover,
            command=self.command,
            corner_radius=5, 
            image=self.add_button_image
            ).pack(pady=0, anchor=None, side="left")
    

class TasksFrame(ctk.CTkScrollableFrame):
    """ Klasse zum Hinzufügen von neuen Notizzetteln,
    dies ist das Parent Frame für alle Notizen unter dem Entry Feld
    """
    def __init__(self, parent, delete_task, textbox_notes_font, frame_bg_color, delete_button_image):
        super().__init__(parent, corner_radius=0, fg_color=frame_bg_color)
        self.pack(fill="both", expand=True)

        # grid definieren
        self.columnconfigure(0, weight=1, uniform="a")
        
        # Eingaben
        self.frame_bg_color = frame_bg_color
        self.delete_task = delete_task
        self.textbox_notes_font = textbox_notes_font
        self.delete_button_image = delete_button_image

    # wird vom hinzufügen button getriggert erstellt für jeden neuen task_list Eintrag ein Frame,
    # welches ein label mit dem listen Eintrag und zwei buttons enthält
    def update_tasks(self, new_task):
        if new_task:
            # Das Main Frame der einzelnen Notiz
            single_note_frame = ctk.CTkFrame(
                master=self,
                corner_radius=5,
                fg_color=self.frame_bg_color
            )
            single_note_frame.pack(fill="x")

            # Das Textfeld der Notiz
            notizZettelTextBox = ctk.CTkTextbox(
                master=single_note_frame,
                corner_radius=5,
                height=100,
                font=self.textbox_notes_font,
                fg_color="#efb640",
                bg_color=self.frame_bg_color,
                text_color="black"
            )
            notizZettelTextBox.pack(fill="x", pady=5, padx=10)
            
            notizZettelTextBox.insert("end", new_task)  # Hier wird die Eingabe aus dem Entry Feld in die text_box geschieben
            notizZettelTextBox.bind("<Leave>", self.task_edit)
            text_box_id = id(notizZettelTextBox)
            
            ctk.CTkButton(
                master=single_note_frame,
                width=10,
                height=10,
                fg_color="#efb640",
                bg_color="#efb640",
                hover_color="#ff0000",
                command=lambda: self.delete_task(single_note_frame, text_box_id),
                corner_radius=5,
                text="",
                image=self.delete_button_image
            ).place(rely=0.92, relx=0.95, anchor="se")
            
            return text_box_id

    def task_edit(self, event): 
        # Zugriff auf das Eltern-Widget
        parent_widget = event.widget.master
        if isinstance(parent_widget, ctk.CTkTextbox):
            text_box = parent_widget
            current_content = text_box.get("0.0", "end").strip()
            note_path = f"notes/{id(text_box)}.txt"

            with open(note_path, "r") as file:
                file_content = file.read().strip()
            if file_content == current_content:
                pass
            else:
                with open(note_path, "w") as file:
                    file.write(current_content)       
         
          
class NormalGridFrame(ctk.CTkFrame):
    def __init__(self, parent, corner_radius, fg_color, column, row, sticky):
        super().__init__(parent, corner_radius=corner_radius, fg_color=fg_color)
        self.grid(column=column, row=row, sticky=sticky)


class NormalPackFrame(ctk.CTkFrame):
    def __init__(self, parent, corner_radius, fg_color, fill, height, button_font_small, about_func):
        super().__init__(
            master=parent,
            corner_radius=corner_radius,
            fg_color=fg_color,
            height=height
        )
        self.pack(fill=fill)
        
        # grid definieren
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.rowconfigure(0, weight=1, uniform="a")
        
        # Eingaben
        self.button_font_small = button_font_small
        self.frame_bg_color = fg_color
        self.about_func = about_func
        
        self.create_widgets()
        
    def create_widgets(self):
        ctk.CTkButton(
            master=self,
            text="About",
            fg_color=self.frame_bg_color,
            hover_color=self.frame_bg_color,
            text_color="grey",
            command=self.about_func,
            font=self.button_font_small
            ).grid(column=1, row=0, sticky="e")
