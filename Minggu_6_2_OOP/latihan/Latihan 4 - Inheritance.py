# Latihan 4 — Inheritance
"""
Buat:
- class Hewan → method suara()
- class Anjing, class Kucing → override suara()
"""
class Hewan:
    def suara(self):
        return "Hewan bersuara."

class Anjing(Hewan):
    def suara(self):
        return "Guk guk!"

class Kucing(Hewan):
    def suara(self):
        return "Meong!"

suara_anjing = Anjing()
suara_kucing = Kucing()

print(suara_anjing.suara())
print(suara_kucing.suara())

