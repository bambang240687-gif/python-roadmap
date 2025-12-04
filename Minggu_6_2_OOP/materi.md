🎯 Minggu 6 — Tujuan Pembelajaran

Di akhir minggu ini kamu akan bisa:
- Memahami konsep dasar OOP (Class, Object, Method, Attribute)
- Menggunakan encapsulation, inheritance, polymorphism
- Membuat class sesuai kebutuhan program
- Mengorganisir kode dengan pendekatan OOP
- Membuat mini-project: Aplikasi Manajemen Siswa / Inventori OOP
Semua sesuai dengan dokumentasi resmi Python:
➡️ Classes — https://docs.python.org/3/tutorial/classes.html
➡️ OOP features — https://docs.python.org/3/reference/datamodel.html

📘 Materi Minggu 6
1️⃣ Apa itu OOP?

OOP = cara memodelkan objek dunia nyata ke dalam kode.

Class → cetak biru
Object → hasil nyata dari class
Attribute → data
Method → perilaku (fungsi dalam class)

2️⃣ Membuat Class & Object
Contoh dasar:
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        return f"Mobil {self.merk} berwarna {self.warna}"

mobil1 = Mobil("Toyota", "Hitam")
print(mobil1.info())

3️⃣ Encapsulation (Menyembunyikan Data)

Digunakan untuk melindungi atribut:

class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo   # private

    def lihat_saldo(self):
        return self.__saldo

4️⃣ Inheritance (Pewarisan)

Class anak mewarisi perilaku class induk:

class Hewan:
    def suara(self):
        return "Hewan bersuara"

class Kucing(Hewan):
    def suara(self):
        return "Meow"

k = Kucing()
print(k.suara())  # Meow

5️⃣ Polymorphism

Metode yang sama → hasil berbeda tergantung object.

6️⃣ Dunder Methods (Magic Methods)

Contoh: __str__, __len__, __add__
Bacaan resmi: https://docs.python.org/3/reference/datamodel.html

Contoh:

class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"{self.nama} - Rp{self.harga}"