# Latihan 2 — Class Mahasiswa (pythonic)
"""
Attribute: nama, nim, jurusan
Method: tampilkan_info()
"""
import json

class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
    
    def to_dict(self):
        return {
            'nama': self.nama,
            'nim': self.nim,
            'jurusan': self.jurusan
        }
    
    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
        
    def to_xml(self):
        return f"""
<mahasiswa>
    <nama>{self.nama}</nama>
    <nim>{self.nim}</nim>
    <jurusan>{self.jurusan}</jurusan>
</mahasiswa>
""".strip()
    
mhs = Mahasiswa("Donto", "12345", "Teknik Sipil")

print(mhs.to_dict())
print(mhs.to_json())
print(mhs.to_xml())

