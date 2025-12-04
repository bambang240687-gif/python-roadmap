# Aplikasi Manajemen Siswa (OOP) dan Pythonic.
"""
Fitur:
- Tambah siswa
- Tampilkan semua siswa
- Hapus siswa
- Cari siswa
- Edit data siswa
Gunakan struktur:
    class Siswa:
        # attribute & method

    class Sekolah:
        # CRUD siswa

Ini akan melatih kamu berpikir dalam OOP + modular.
"""
import os

class Siswa:
    def __init__(self, nama, umur, kelas):
        self.nama = nama
        self.umur = umur
        self.kelas = kelas
    
    def info(self):
        return f"Nama: {self.nama} | Umur: {self.umur} tahun | Kelas: {self.kelas}"

class Sekolah:
    def __init__(self):
        self.siswa = []
    
    def tambah_siswa(self, siswa):
        if any([s.nama == siswa.nama for s in self.siswa]):
            print(f"Siswa dengan nama {siswa.nama} sudah terdaftar.")
            return
        
        self.siswa.append(siswa)
        print(f"Siswa {siswa.nama} berhasil ditambahkan.")
    
    def tampilkan_siswa(self):
        if not self.siswa:
            return "Tidak ada siswa yang terdaftar."
        return "\n".join(s.info() for s in self.siswa)
        
    def hapus_siswa(self, nama_siswa):
        for s in self.siswa:
            if s.nama == nama_siswa:
                self.siswa.remove(s)
                return True
        return False
    
    def cari_siswa(self, nama_siswa):
        for s in self.siswa:
            if s.nama == nama_siswa:
                return s
        return None
    
    def edit_siswa(self, nama_siswa, umur_baru, kelas_baru):
        for s in self.siswa:
            if s.nama == nama_siswa:
                s.umur = umur_baru
                s.kelas = kelas_baru
                return True
        return False
    
    def total_siswa(self):
        return len(self.siswa)
    
    def rata_umur(self):
        if not self.siswa:
            return 0
        return sum(s.umur for s in self.siswa) / len(self.siswa)
    
    def keluar(self):
        print("Terima kasih telah menggunakan aplikasi ini.")

sekolah =Sekolah()

while True:
    print("-" * 20)
    print("=== MANAJEMEN SISWA ===")
    print("-" * 20)
    print("1. Tambah Siswa")
    print("2. Tampilkan Semua Siswa")
    print("3. Hapus Siswa")
    print("4. Cari Siswa")
    print("5. Edit Data Siswa")
    print("6. Total Siswa")
    print("7. Rata-rata Umur Siswa")
    print("0. Keluar")
    print("-" * 20)

    pilihan = input("Pilih Menu: ")

    if pilihan == '1':
        nama = input("Input Nama Siswa: ")
        umur = int(input("Input Umur Siswa: "))
        kelas = input("Input Kelas Siswa: ")

        siswa_baru = Siswa(nama, umur, kelas)
        sekolah.tambah_siswa(siswa_baru)
    
    elif pilihan == '2':
        if sekolah.siswa:
            print(sekolah.tampilkan_siswa())
        else:
            print("Tidak ada siswa yang terdaftar.")

    elif pilihan == '3':
        nama_siswa = input("Input Nama Siswa Yang Ingin Dihapus: ")
        if sekolah.hapus_siswa(nama_siswa):
            print(f"Siswa {nama_siswa} berhasil dihapus.")
        else:
            print(f"Siswa {nama_siswa} tidak ditemukan.")
    
    elif pilihan == '4':
        nama_siswa = input("Input Nama Siswa Yang Ingin Dicari: ")
        cari_siswa = sekolah.cari_siswa(nama_siswa)
        if cari_siswa:
            print(cari_siswa.info())
        else:
            print(f"Siswa {nama_siswa} tidak ditemukan.")
    
    elif pilihan == '5':
        nama_siswa = input("Input Nama Siswa Yang Ingin Diubah: ")
        umur_baru = int(input("Input Umur Baru: "))
        kelas_baru = input("Input Kelas Baru: ")

        if sekolah.edit_siswa(nama_siswa, umur_baru, kelas_baru):
            print(f"Siswa {nama_siswa} berhasil diubah.")
        else:
            print(f"Siswa {nama_siswa} tidak ditemukan.")
    
    elif pilihan == '6':
        print(f"Total Siswa: {sekolah.total_siswa()}")
    
    elif pilihan == '7':
        print(f"Rata-rata Umur Siswa: {sekolah.rata_umur():.2f}")
    
    elif pilihan == '0':
        sekolah.keluar()
        break

    else:
        print("Pilihan tidak valid. Silahkan coba lagi.")

    print("-" * 20)
    input("Tekan Enter untuk kembali...")

    os.system("cls" if os.name == "nt" else "clear")

print("Terima kasih telah menggunakan aplikasi ini.")
