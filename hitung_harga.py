MINIMAL_PRINT = 1000
HARGA_MINIMAL = 500000
HARGA_OVER_PRINT = 90   # <-- Ubah sesuai kebutuhan

def hitung_harga(jumlah):
    if jumlah <= MINIMAL_PRINT:
        return HARGA_MINIMAL
    else:
        return HARGA_MINIMAL + (jumlah - MINIMAL_PRINT) * HARGA_OVER_PRINT

# Contoh penggunaan
order = 1700
total = hitung_harga(order)
print(f"Total: Rp {total:,}".replace(',', '.'))  # Output: Rp 572.000