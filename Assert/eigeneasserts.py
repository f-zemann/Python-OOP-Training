class Warenkorb:
    def __init__(self):
        self.preise = []

    def hinzufuegen(self, preis):
        if preis > 0:
            self.preise.append(preis)

    def anzahl(self):
        return len(self.preise)

    def gesamt(self):
        total = 0
        for p in self.preise:
            total += p
        return total

    def durchschnitt(self):
        if self.preise:
            return self.gesamt() / self.anzahl()
        return 0

w = Warenkorb()

assert len(w.preise) == 0
assert type(w.preise) == list
assert sum(w.preise) == 0
anzahl = w.anzahl()
assert anzahl == 0
gesamt = w.gesamt()
assert gesamt == 0
durchschnitt = w.durchschnitt()
assert durchschnitt == 0

w.hinzufuegen(5)
w.hinzufuegen(5)
w.hinzufuegen(10)
w.hinzufuegen(10.00)
assert w.anzahl() == 4
assert w.gesamt() == 30.00
assert w.durchschnitt() == 7.5


w.hinzufuegen(-5)
w.hinzufuegen(10000000)
w.hinzufuegen(0)

assert w.anzahl() == 2
assert w.gesamt() == 15
assert w.durchschnitt() == 7.5





class NotenListe:
    def __init__(self):
        self.noten = []

    def hinzufuegen(self, note):
        if type(note) is int and 1 <= note <= 6:

            self.noten.append(note)

    def anzahl(self):
        return len(self.noten)

    def beste(self):
        if not self.noten:
            return None
        return min(self.noten)

n = NotenListe()
assert len(n.noten) == 0
assert type(n.noten) == list
assert sum(n.noten) == 0
best = n.beste()
assert best == None

n.hinzufuegen(4)
n.hinzufuegen(1)
assert len(n.noten) == 2
assert sum(n.noten) == 5
n.hinzufuegen(8)
n.hinzufuegen('b')
n.hinzufuegen(-1)
n.hinzufuegen(1.0)
n.hinzufuegen(True)
assert len(n.noten) == 2
assert sum(n.noten) == 5
anzahl = n.anzahl()
assert anzahl == 2
best = n.beste()
assert best == 1











class PunkteKonto:
    def __init__(self):
        self.punkte = 0

    def sammeln(self, wert):
        if wert > 0:
            self.punkte += wert

    def einloesen(self, wert):
        if 0 < wert <= self.punkte:
            self.punkte -= wert

    def stand(self):
        return self.punkte


p = PunkteKonto()
assert p.punkte == 0

p.sammeln(3)
p.sammeln(60)
assert p.punkte == 63

p.sammeln(-50)
p.sammeln(0)
assert p.punkte == 63

p.einloesen(20)
p.einloesen(13)
assert p.punkte == 30

p.einloesen(-20)
p.einloesen(100)
p.einloesen(0)
assert p.punkte == 30

stand = p.stand()
assert stand == 30
