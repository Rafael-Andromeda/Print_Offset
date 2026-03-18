import sqlite3

conn = sqlite3.connect("kertas.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS kertas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_kertas TEXT,
    gsm INTEGER,
    lebar REAL,
    tinggi REAL,
    harga INTEGER,
    UNIQUE(nama_kertas, gsm, lebar, tinggi)
)
""")

conn.commit()


def parse_harga(harga_str):
    return int(harga_str.replace("Rp", "").replace(".", "").strip())


while True:
    nama = input("Masukkan Nama Kertas (plano): ").lower()
    gsm = int(input("Masukkan Tebal Kertas (gsm): "))
    lebar = float(input("Masukkan Lebar: "))
    tinggi = float(input("Masukkan Tinggi: "))
    harga_input = input("Masukkan Harga Per Lembar (plano) : ")

    harga = parse_harga(harga_input)
    try:
        cursor.execute("""
        INSERT INTO kertas(nama_kertas, gsm, lebar, tinggi, harga)
        VALUES (?, ?, ?, ?, ?)
        """, (nama, gsm, lebar, tinggi, harga))
        conn.commit()
        print("Data berhasil disimpan!")
    except sqlite3.IntegrityError:
        print("Data sudah ada (kombinasi sama)!")
        
    lanjut = input("Input lagi? (y/n): ")
    if lanjut.lower() != 'y':
        break
conn.close()