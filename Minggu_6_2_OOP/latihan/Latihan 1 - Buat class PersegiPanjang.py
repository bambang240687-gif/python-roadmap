# Latihan 1 - Buat class PersegiPanjang (pythonic)
"""
Attribute: panjang, lebar
Method: luas(), keliling()
"""
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def luas(self):
        return self.panjang * self.lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

persegi_panjang = PersegiPanjang(panjang, lebar)

print(f"Luas persegi panjang: {persegi_panjang.luas()}")
print(f"Keliling persegi panjang: {persegi_panjang.keliling()}")
