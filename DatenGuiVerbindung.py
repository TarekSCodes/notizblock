from CSVDateiZugriff import CSVDateiZugriff as CDZ
from DatenGuiHelfer import DatenGuiHelfer as DGH

class DatenGuiVerbindung:
    
    
    def NotizenBeiStartInDieGuiLaden(master):
        DGH.NotizTextBoxErstellen(models=CDZ.LadeNotizen(), master=master)
    
    def NotizHinzufuegen(master):
        DGH.NotizTextBoxenEntfernen(master=master)
        DGH.NotizTextBoxErstellen(models=CDZ.LadeNotizen(), master=master)
        
    # TODO
    # Beim ändern des Textes in einer Notiz soll der Text auch in der Textdatei geändert werden
    def NotizTextBoxAendern():
        pass
    
    def NotizEntfernen(master):
        pass
    