# Latihan 5 — Polymorphism. Buat fungsi bernama bunyi(hewan) yang menerima object hewan apa saja. (Pythonic)
class Hewan:
    def suara(self):
        return "Hewan bersuara."

class Sapi(Hewan):
    def suara(self):
        return "Moo!"

class Burung(Hewan):
    def suara(self):
        return "Cik-cik!"

hewan_list= [h() for h in (Hewan, Sapi, Burung)]

for h in hewan_list:
    print(h.suara())
