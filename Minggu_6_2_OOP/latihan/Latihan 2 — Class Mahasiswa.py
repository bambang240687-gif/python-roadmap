# Latihan 2 — Class Mahasiswa (pythonic)
class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
    
    def dict(self):
        return {
            'nama': self.nama,
            'nim': self.nim,
            'prodi': self.prodi
        }
    
    def json(self):
        return {
            'nama': self.nama,
            'nim': self.nim,
            'prodi': self.prodi
        }
    
    def xml(self):
        return {
            'nama': self.nama,
            'nim': self.nim,
            'prodi': self.prodi
        }

mhs = Mahasiswa("Donto", "12345", "Teknik Sipil")

print(mhs.dict())
print(mhs.json())
print(mhs.xml())

