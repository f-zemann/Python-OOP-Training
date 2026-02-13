class Mitarbeiter:
    def __init__(self,name):
        self.name = name
        
    def zahle_kaffee(self,kasse,wert):
        if kasse.einzahlen(self.name,wert):
            return f"{self.name} hat {wert} Euro eingezahlt."
        return "Ungültiger Betrag."
    
class KassenVerwaltung:
    def __init__(self):
        self.kassen =[]
        
    def kasse_hinzufuegen(self, kasse):
        if not isinstance(kasse,Kaffeekasse):
            return False
        self.kassen.append(kasse)
        return True
    def gesamtbetrag(self):
        summe = 0
        for kasse in self.kassen:
            summe += kasse.betrag
        return summe
    def status_alle(self):
        return [kasse.status() for kasse in self.kassen]
            

class Kaffeekasse:
    def __init__(self,name,betrag=0):
        self.name = name
        self.betrag = betrag
        self.verlauf = []
    
    def einzahlen(self,name,wert):
        if wert <= 0:
            return False
        self.verlauf.append((name, wert))
        self.betrag += wert
        return True
        
    def status(self):
        return f"Kaffeekasse {self.name}: {self.betrag} Euro."
    def verlauf_anzeigen(self):
        #Damit die liste nicht von außen verändert wird geben wir kopie raus.
        return list(self.verlauf)



# ===== TESTS =====

k = Kaffeekasse("Test")
m = Mitarbeiter("Max")

# gültige Einzahlung
assert m.zahle_kaffee(k, 5) == "Max hat 5 Euro eingezahlt."
assert k.betrag == 5

# ungültige Einzahlung
assert m.zahle_kaffee(k, -3) == "Ungültiger Betrag."
assert k.betrag == 5   # darf sich nicht ändern

# Verlauf geprüft
verlauf = k.verlauf_anzeigen()
assert verlauf == [("Max", 5)]

# Verwaltung
v = KassenVerwaltung()
v.kasse_hinzufuegen(k)

k2 = Kaffeekasse("Test2")
m.zahle_kaffee(k2, 7)
v.kasse_hinzufuegen(k2)

assert v.gesamtbetrag() == 12

#status prüfen
v = KassenVerwaltung()

k1 = Kaffeekasse("Küche")
k2 = Kaffeekasse("Werkstatt")

m = Mitarbeiter("Max")

v.kasse_hinzufuegen(k1)
v.kasse_hinzufuegen(k2)

m.zahle_kaffee(k1, 5)
m.zahle_kaffee(k2, 7)

assert len(v.kassen) == 2
assert v.gesamtbetrag() == 12

assert v.status_alle() == [
    "Kaffeekasse Küche: 5 Euro.",
    "Kaffeekasse Werkstatt: 7 Euro."
]
print(v.status_alle())
print("Tests ok ✅")





print("Alle Tests bestanden ✅")





