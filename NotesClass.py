import customtkinter as ctk
import const
from notizblock import EntryFrame, Footer
from NotizModel import NotizModel as NM
from CSVDateiZugriff import CSVDateiZugriff as CDZ
from DatenGuiVerbindung import DatenGuiVerbindung as DGV

class Notes(ctk.CTkFrame):
    def __init__(self, master, about_func):
        super().__init__(master)
        self.pack(expand=True, fill="both")

        # Diese StringVariable setzt den initial Wert des Entry Feldes
        self.entry_str = ctk.StringVar(value="")
        
        # Eingaben
        self.about_func = about_func

        # Frames
        self.create_widgets()
        
        DGV.NotizenBeiStartInDieGuiLaden(self.NotizenFrame)

    def create_widgets(self):
        EntryFrame(self, self.erstelleNotizButton_Geklickt, self.entry_str)
        
        # Erstellen des Frames welches die NotizTextBoxen beinhaltet
        self.NotizenFrame = ctk.CTkScrollableFrame(
            master=self,
            corner_radius=0,
            fg_color=const.FRAME_BACKGROUND_COLOR)
        self.NotizenFrame.pack(fill="both", expand=True)
        self.NotizenFrame.columnconfigure(0, weight=1, uniform="a")
        
        Footer(
            parent=self,
            corner_radius=0,
            fill="x",
            height=50,
            about_func=self.about_func)

    def erstelleNotizButton_Geklickt(self, event=None):
        
        new_task = self.entry_str.get()  # Der Inhalt des Entry feldes wird ausgelesen

        if new_task:  # prüfen ob das Entry Feld nicht leer ist
            
            CDZ.ErstelleNotiz(NM(1, new_task))
            DGV.NotizHinzufuegen(master=self.NotizenFrame)
            self.entry_str.set("")  # das Entry Feld wird wieder geleert
    
    # TODO
    # Entfernen der Notiz aus der Datei und der Gui
    def NotizEntfernenButton_Geklickt(self):
        pass