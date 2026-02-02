"""
OOP Miniübung – Fundbüro
Trainingsprojekt
Nicht für Produktion gedacht
"""

class Fundstueck:
    def __init__(self, name,fundort,abgeholt=False):
        self.name = name
        self.fundort = fundort
        self.abgeholt = abgeholt
        
    def als_abgeholt_markieren(self):
        self.abgeholt = True
    def info(self):
        #selbe Logik wie bei listcomprehension nur mit string statt liste Ausdruck falls bedingung sonst Ausdruck
        status = 'abgeholt' if self.abgeholt else 'nicht abgeholt'
        return f"Gegenstand: {self.name:<13} | Ort: {self.fundort:<10} | Status: {status}"
        
class Fundbuero:
    def __init__(self):
        self.funde = []
    def hinzufuegen(self,fundstueck):
        #Duplikatprüfung falls vorhanden sagen wir mit return False,hier stopp, nicht erneut hinzugefügt
        for objekt in self.funde:
            if objekt.name == fundstueck.name :
                return False
        self.funde.append(fundstueck)
        return True
    def abholen(self,name):
        #keine Listenprüfung nötig, da schleife nur greift wenn elemente in liste vorhanden.
        for objekt in self.funde:
            if objekt.name == name :
                objekt.als_abgeholt_markieren()
                print(f"{name} wurde gefunden.")
                return True
        #Dieser Block wird ausgeführt wenn Schleife ohne ergebnis endet.
        print(f"{name} wurde nicht gefunden.")
        return False
    def alle_anzeigen(self):
        #Bei leerer Liste geben wir eine Rückmeldung heraus
        if len(self.funde) == 0:
            print("Keine Funde vorhanden")
        else:
            for objekt in self.funde:
                print(objekt.info())
    def offene_funde_anzeigen(self):
        #Wir bauen eine Hilfslogik ein.
        gefunden = False
        for objekt in self.funde:
            if not objekt.abgeholt:
                print(objekt.info())
                gefunden = True
        #Hilfslogik nutzen um Rückmeldung zu geben, wenn Schleife ergebnislos bleibt.
        if not gefunden:
            print('Keine offenen Fundstücke.')

        
            
g1 = Fundstueck("Schlüsselbund", "Park")
g2 = Fundstueck("Rucksack", "Bus")

# ~ print(g1.info())
g1.als_abgeholt_markieren()
# ~ print(g1.info())

# ~ print(g2.info())

b = Fundbuero()

b.hinzufuegen(Fundstueck("Handy", "Zug"))
b.hinzufuegen(Fundstueck("Handy", "Zug"))
b.hinzufuegen(Fundstueck("Mütze", "Schule"))

# ~ b.alle_anzeigen()


b.hinzufuegen(Fundstueck("Handy", "Zug"))
b.hinzufuegen(Fundstueck("Mütze", "Schule"))

b.abholen("Handy")
b.abholen("Schlüssel")

# ~ b.alle_anzeigen()

b.hinzufuegen(Fundstueck("Handy", "Zug"))
b.hinzufuegen(Fundstueck("Mütze", "Schule"))

b.abholen("Handy")
print(' ')
b.offene_funde_anzeigen()
b.abholen("Mütze")
b.offene_funde_anzeigen()

