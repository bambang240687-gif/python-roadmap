# Latihan 3 — Class Bank dengan saldo private (Pythonic)
"""
Bisa: setor(), tarik(), cek_saldo()
"""
class Bank:
    def __init__(self, saldo):
        self.__saldo = saldo
    
    def setor(self, jumlah):
        if jumlah > 0:
            return "Jumlah setor harus lebih dari 0!"

        self.__saldo += jumlah
        return f"Setor: Rp {jumlah:,.0f}. Saldo sekarang: Rp {self.__saldo:,.0f}"
        
    def tarik(self, jumlah):
        if jumlah > 0:
            return "Jumlah tarik harus lebih dari 0!"
        
        if jumlah > self.__saldo:
            return "Saldo tidak cukup!"
        
        self.__saldo -= jumlah
        return f"Tarik: Rp {jumlah:,.0f}. Sisa saldo: Rp {self.__saldo:,.0f}"
        
    def cek_saldo(self):
        return self.__saldo

bank = Bank(1_000)

bank_setor = bank.setor(500)
bank_tarik = bank.tarik(100)

print(bank_setor)
print(bank_tarik)
print("saldo saat ini:", bank.cek_saldo())
