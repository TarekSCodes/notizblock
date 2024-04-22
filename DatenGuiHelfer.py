import const
import customtkinter as ctk

class DatenGuiHelfer:
    
    # TODO
    # Wie kann ich 
    def NotizTextBoxErstellen(models: list, master):
        reverseModelListe = sorted(models, key=lambda x: int(x.id), reverse=True)
        
        for model in reverseModelListe:
            
            # Das Main Frame der einzelnen Notiz
            single_note_frame = ctk.CTkFrame(
                master=master,
                corner_radius=5,
                fg_color=const.FRAME_BACKGROUND_COLOR
            )
            single_note_frame.pack(fill="x")
            
            # Das Textfeld der Notiz
            notizZettelTextBox = ctk.CTkTextbox(
                master=single_note_frame,
                corner_radius=5,
                height=100,
                font=const.TEXTBOX_NOTES_FONT,
                fg_color=const.NOTIZ_ZETTEL_BACKGROUND_COLOR,
                bg_color=const.FRAME_BACKGROUND_COLOR,
                text_color=const.NOTIZ_ZETTEL_TEXT_COLOR
            )
            notizZettelTextBox.pack(fill="x", pady=5, padx=10)
            
            notizZettelTextBox.insert("end", model.text)  # Hier wird die Eingabe aus dem Entry Feld in die text_box geschieben
            #notizZettelTextBox.bind("<Leave>", master.task_edit)
            
            NotizEntfernenButton = ctk.CTkButton(
                master=single_note_frame,
                width=10,
                height=10,
                fg_color=const.NOTIZ_DELETE_BUTTON_BACKGROUND_COLOR,
                bg_color=const.NOTIZ_DELETE_BUTTON_BACKGROUND_COLOR,
                hover_color=const.NOTIZ_DELETE_BUTTON_HOVER_COLOR,
                command= master.NotizEntfernen(single_note_frame),
                corner_radius=5,
                text="",
                image=const.DELETE_ICON_IMAGE
            )
            NotizEntfernenButton.place(rely=0.92, relx=0.95, anchor="se")
    
    def NotizTextBoxenEntfernen(master):
        for TextBox in master.winfo_children():
            TextBox.destroy()