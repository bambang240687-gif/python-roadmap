# Latihan 1 - Error Handling Input Angka.py. (Pythonic)
"""
Buat program yang menerima angka dan menangani 3 error:
🔹 input bukan angka
🔹 angka negatif
🔹 angka terlalu besar
"""
while True:
    try:
        angka = int(input("Masukkan Angka: "))

        if angka < 0:
            raise ValueError("Angka tidak boleh negatif.")
        
        if angka > 100:
            raise ValueError("Angka terlalu besar.")
        
        break
    except ValueError as e:
        print(f"Error: {e}")

print(f"Angka valid: {angka}")
