from NotizModel import NotizModel as NM
from TextDateiVerarbeiter import TextDateiVerarbeiterKlasse as TDVK

NOTIZ_DATEI: str = "Notizen.csv"

class TextDatenVerbindung:

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
        Pfad = TDVK.KompletterDateiPfad(NOTIZ_DATEI)
        Datei = TDVK.Dateiladen(Pfad)
        notizenModelListe = TDVK.KovertierenInNotizModel(Datei)

        # Die maximale ID finden
        aktuelleId = 1
        if len(notizenModelListe) > 0:
            listeAbsteigend = sorted(notizenModelListe, key=lambda x: int(x.id), reverse=True)
            aktuelleId = int(listeAbsteigend[0].id) + 1

        model.id = aktuelleId
        
        notizenModelListe.append(model)

        # Konvertiert die notizenModelListe in eine string Liste
        # Speichert die string Liste in die Textdatei
        TDVK.SpeichernInNotizTextDatei(notizenModelListe, NOTIZ_DATEI)

        return model
