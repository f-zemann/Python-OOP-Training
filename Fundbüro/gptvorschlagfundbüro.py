"""
Fundbüro – Refactorte Trainingsversion
Fokus: OOP-Struktur, Trennung von Logik und UI, klare Rückgaben
"""

from enum import Enum
from typing import List, Optional


# -------------------------
# Domain Layer
# -------------------------
#Der Status wurde als eigene Klasse definiert, jetzt gibt es nur 
#einen eindeutigen zustand zur gleichen zeit und der ist selbsterklärend.
class Status(Enum):
    OFFEN = "offen"
    ABGEHOLT = "abgeholt"

#Type hints wurden hinzugefügt, damit entwickler bei der anwendung von
#Code gleich wissen ob sie ihn richtig anwenden, auch ohne den Inhalt zu interpretieren
class Fundstueck:
    """Repräsentiert ein einzelnes Fundstück."""

    _id_counter: int = 0

    def __init__(self, name: str, fundort: str) -> None:
        Fundstueck._id_counter += 1
        
        self.id: int = Fundstueck._id_counter
        #wie man sehen kann werden parameter bereinigt bevor sie übernommen werden
        #so führt ein leerzeichen nicht zu NameError
        self.name: str = name.strip()
        self.fundort: str = fundort.strip()
        #Status wurde Standardmäßig festgelegt, sinnvolle Ausgangslage
        self.status: Status = Status.OFFEN

    def markiere_abgeholt(self) -> bool:
        """Markiert das Fundstück als abgeholt. Gibt False zurück, wenn bereits abgeholt."""
        if self.status == Status.ABGEHOLT:
            return False
        self.status = Status.ABGEHOLT
        return True

    def ist_offen(self) -> bool:
        #Hier wird überprüft ob der Status offen ist
        return self.status == Status.OFFEN

    def format_zeile(self) -> str:
        """Formatierte Darstellung für UI-Schicht."""
        #Dasselbe wie ein einzelner langer fstring nur übersichtlicher
        #fürs Auge besser erweiterbar
        return (
            f"ID: {self.id:<3} | "
            f"Gegenstand: {self.name:<15} | "
            f"Ort: {self.fundort:<12} | "
            f"Status: {self.status.value}"
        )


# -------------------------
# Repository / Service Layer
# -------------------------

class Fundbuero:
    """Verwaltet alle Fundstücke."""

    def __init__(self) -> None:
        #der_ sagt unsere Liste soll von außen nicht verändert werden.
        self._funde: List[Fundstueck] = []

    def hinzufuegen(self, name: str, fundort: str) -> Fundstueck:
        fund = Fundstueck(name, fundort)
        self._funde.append(fund)
        return fund

    def finde_per_id(self, id_nummer: int) -> Optional[Fundstueck]:
        #next schon Rechenleistung, wenn gefunden fertig, schleife endet
        #gute vorbereitung auf größere Programme
        return next((f for f in self._funde if f.id == id_nummer), None)

    def alle(self) -> List[Fundstueck]:
        #Hier geben wir für die anzeige eine Kopie unserer internen liste raus
        return list(self._funde)

    def offene(self) -> List[Fundstueck]:
        #Hier wird eine neue Liste aus gefilterten Daten erstellt
        return [f for f in self._funde if f.ist_offen()]

    def anzahl_offen(self) -> int:
        return len(self.offene())

    def abholen(self, id_nummer: int) -> str:
        #Statt die funktion unten mehrfach aufzurufen, 
        #speichern wir sie und arbeiten mit der Variablen
        #Das ist kürzer, weniger fehleranfällig.
        fund = self.finde_per_id(id_nummer)

        if not fund:
            return "NICHT_GEFUNDEN"

        if not fund.markiere_abgeholt():
            return "BEREITS_ABGEHOLT"

        return "OK"


# -------------------------
# UI Layer (CLI)
# -------------------------
#usereingaben und Fehlerprüfung haben wir in einer funktion
#festgelegt und können sie jetzt beliebig oft verwenden.
def eingabe_int(prompt: str) -> Optional[int]:
    try:
        return int(input(prompt))
    except ValueError:
        print("Bitte eine gültige Zahl eingeben.")
        return None


def anzeigen_liste(liste: List[Fundstueck]) -> None:
    #für das anzeigen haben wir eine eigene funktion definiert
    #die im Menü flexibel wiederverwertbar ist, das spart tipparbeit.
    if not liste:
        print("Keine Einträge vorhanden.")
        return

    for f in liste:
        print(f.format_zeile())


def menue() -> None:
    buero = Fundbuero()

    while True:
        print("\n--- Fundbüro ---")
        print("1 = Alle anzeigen")
        print("2 = Fundstück hinzufügen")
        print("3 = Fundstück abholen")
        print("4 = Nur offene anzeigen")
        print("0 = Beenden")

        wahl = input("Auswahl: ").strip()

        if wahl == "1":
            anzeigen_liste(buero.alle())

        elif wahl == "2":
            #da diese Eingabe nicht auf den typ int beschränkt 
            #ist, bekommt sie ihre eigene Beschreibung.
            name = input("Gegenstand: ").strip()
            ort = input("Fundort: ").strip()

            if not name or not ort:
                print("Name und Fundort dürfen nicht leer sein.")
                continue

            fund = buero.hinzufuegen(name, ort)
            print(f"Hinzugefügt mit ID {fund.id}")

        elif wahl == "3":
            if buero.anzahl_offen() == 0:
                print("Keine offenen Fundstücke.")
                continue

            anzeigen_liste(buero.offene())
            id_nummer = eingabe_int("ID: ")
            if id_nummer is None:
                continue

            result = buero.abholen(id_nummer)

            if result == "OK":
                print("Fundstück wurde abgeholt.")
            elif result == "BEREITS_ABGEHOLT":
                print("Dieses Fundstück war bereits abgeholt.")
            else:
                print("ID nicht gefunden.")

        elif wahl == "4":
            anzeigen_liste(buero.offene())

        elif wahl == "0":
            print("Programm beendet.")
            break

        else:
            print("Ungültige Auswahl.")


if __name__ == "__main__":
    menue()

