from NotizModel import NotizModel as NM
import os

TEXT_DATEIEN_ORDNER: str = "./TextDateien"


class CSVDateiHelfer:

    def KompletterDateiPfad(dateiname: str) -> str:
        """
        Nimmt den Dateinamen und den Dateipfad verbindet diese und gibt einen string zurück 

        Args:
            dateiname (str): Beispiel.csv

        Returns:
            str: ./Verzeichnis/Beispiel.csv
        """
        DateiPfad = f"{TEXT_DATEIEN_ORDNER}/{dateiname}"
                
        return DateiPfad
    
    def Dateiladen(pfad: str) -> (list | str):
        ausgabe = []
        if os.path.exists(pfad) == False:
            return ausgabe
        
        with open(pfad, "r") as datei:
            for zeile in datei:
                ausgabe.append(zeile.strip())
        
        return ausgabe
    
    def KovertierenInNotizModel(zeilen: list) -> (list | NM):
        ausgabe = []
        
        for zeile in zeilen:
            cols = zeile.split("~")
            
            n = NM(
                id = cols[0],
                text = cols[1]
            )
            
            ausgabe.append(n)
        
        return ausgabe

    def SpeichernInNotizTextDatei(notizenModelListe, dateiName) -> None:
        
        zeilen = []
        
        for NM in notizenModelListe:
            zeilen.append(f"{ NM.id }~{ NM.text }\n")
        
        with open(CSVDateiHelfer.KompletterDateiPfad(dateiName), "w") as datei:
            for zeile in zeilen:
                datei.writelines(f"{zeile}")