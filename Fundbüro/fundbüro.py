"""
OOP Miniübung – Fundbüro
Trainingsprojekt
Nicht für Produktion gedacht
"""


class Fundstueck:    
    #Diese Variable gehört der klasse nicht dem objekt
    id_counter = 0
    def __init__(self, name,fundort,abgeholt=False):
        #Wir erhöhen die Variable über den Klassennamen, so generieren wir fortlaufende ids 
        Fundstueck.id_counter +=1
        self.id = Fundstueck.id_counter
        self.name = name
        self.fundort = fundort
        self.abgeholt = abgeholt
        
    def als_abgeholt_markieren(self):
        self.abgeholt = True
    def info(self):
        #selbe Logik wie bei listcomprehension nur mit string statt liste Ausdruck falls bedingung sonst Ausdruck
        status = 'abgeholt' if self.abgeholt else 'nicht abgeholt'
        return f"ID: {self.id:<3} | Gegenstand: {self.name:<13} | Ort: {self.fundort:<10} | Status: {status}"

        
class Fundbuero:
    def __init__(self):
        self.funde = []
    def hinzufuegen(self,fundstueck):
        self.funde.append(fundstueck)
    def finde_per_id(self, id_nummer):
        for objekt in self.funde:
            if objekt.id == id_nummer:
                return objekt
        return None

    def abholen_per_id(self, id_nummer):
        objekt = self.finde_per_id(id_nummer)
        if objekt is None:
            return "nicht_gefunden"
        else:
            if objekt.abgeholt:
                return "bereits_abgeholt"
            objekt.als_abgeholt_markieren()
            return "ok"


    def alle_anzeigen(self):
        #Bei leerer Liste geben wir eine Rückmeldung heraus
        if len(self.funde) == 0:
            print("Keine Funde vorhanden")
        else:
            for objekt in self.funde:
                print(objekt.info())
                
    def offene_funde_anzeigen(self):
        #Hilfslogik eingebaut
        gefunden = False
        for objekt in self.funde:
            if not objekt.abgeholt:
                print(objekt.info())
                gefunden = True
        #Wenn schleife nicht greift dann sinnvolle Rückmeldung
        if not gefunden:
            print('Keine offenen Fundstücke.')

    #Kurzform wäre: return sum(1 for o in self.funde if not o.abgeholt)
    def anzahl_offen(self):
        anzahl = 0
        for objekt in self.funde:
            if not objekt.abgeholt:
                anzahl += 1
        return anzahl


def menue():
    b = Fundbuero()

    while True:
        print("\n--- Fundbüro ---")
        print("1 = Anzeigen")
        print("2 = Hinzufügen")
        print("3 = Abholen per ID")
        print("0 = Ende")

        wahl = input("Auswahl: ")

        if wahl == "1":
            b.alle_anzeigen()

        elif wahl == "2":
            name = input("Name: ")
            ort = input("Fundort: ")
            b.hinzufuegen(Fundstueck(name, ort))

        elif wahl == "3":
            if b.anzahl_offen() == 0:
                print('Keine Produkte zum abholen verfügbar.')
                continue
            print("Offene Fundstücke:")
            b.offene_funde_anzeigen()
            #robuster für fehleingaben und tippfehler
            try:
                id_nummer = int(input("ID: "))
            except ValueError:
                print("Bitte Zahl eingeben.")
                continue

            ergebnis = b.abholen_per_id(id_nummer)
            if ergebnis == "ok":
                print("Abgeholt!")
            elif ergebnis == "bereits_abgeholt":
                print("War schon abgeholt.")   
            elif ergebnis == "nicht_gefunden":
                print("ID nicht gefunden.")

        elif wahl == "0":
            break
    

menue()


