# Latihan 2 — Class Mahasiswa (pythonic)
"""
Attribute: nama, nim, jurusan
Method: tampilkan_info()
"""
class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def dict(self):
        return {
            'nama': self.nama,
            'nim': self.nim,
            'jurusan': self.jurusan
        }
    
    def json(self):
        return {
            'nama': self.nama,
            'nim': self.nim,
            'jurusan': self.jurusan
        }
    
    def xml(self):
        return {
            'nama': self.nama,
            'nim': self.nim,
            'jurusan': self.jurusan
        }

mhs = Mahasiswa("Donto", "12345", "Teknik Sipil")

print(mhs.dict())
print(mhs.json())
print(mhs.xml())

