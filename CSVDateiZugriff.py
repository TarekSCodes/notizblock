from NotizModel import NotizModel as NM
from CSVDateiHelfer import CSVDateiHelfer as CDH

NOTIZ_DATEI: str = "Notizen.csv"

class CSVDateiZugriff:

    def ErstelleNotiz(model) -> NM:
        """
        Lädt die Notizen Textdatei und erstellt aus den Daten jeder Zeile ein NotizenModel Objekt.
        
        Ermittelt die höchste Id und weißt dem der Methode übergebenen Objekt die höchste Id + 1 hinzu.

        Speichert zum Schluss alle Objekte in die Textdatei.
        
        Args:
            model (NotizModel): _description_

        Returns:
            NM: Gibt das NotizModel Objekt mit der richtig zugewiesenen Id zurück
        """
        
        # Lädt die Datei und konvertiert den Text in eine Liste = [NotizModel, NotizModel]
        Pfad = CDH.KompletterDateiPfad(NOTIZ_DATEI)
        Datei = CDH.Dateiladen(Pfad)
        notizenModelListe = CDH.KovertierenInNotizModel(Datei)

        # Die maximale ID finden
        aktuelleId = 1
        if len(notizenModelListe) > 0:
            listeAbsteigend = sorted(notizenModelListe, key=lambda x: int(x.id), reverse=True)
            aktuelleId = int(listeAbsteigend[0].id) + 1

        model.id = aktuelleId
        
        notizenModelListe.append(model)

        # Konvertiert die notizenModelListe in eine string Liste
        # Speichert die string Liste in die Textdatei
        CDH.SpeichernInNotizTextDatei(notizenModelListe, NOTIZ_DATEI)

        return model

    def LadeNotizen() -> (list | NM):
        """
        Lädt beim start der App die Textdatei ein und erstellt aus den Daten der Zeilen NotizModel Objekte
        
        Returns:
            list NotizenModel: Gibt eine Liste mit den NotizModel Objekten zurück
        """
        
        Pfad = CDH.KompletterDateiPfad(NOTIZ_DATEI)
        Datei = CDH.Dateiladen(Pfad)
        notizenModelListe = CDH.KovertierenInNotizModel(Datei)
        
        return notizenModelListe
        