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

def tampil_data():
    cursor.execute("SELECT * FROM kertas")
    rows = cursor.fetchall()

    if not rows:
        print("\nData masih kosong!")
        return []

    print("\n DATA KERTAS ")
    for i, row in enumerate(rows, start=1):
        print(f"{i}. {row[1]} | {row[2]} gsm | {row[3]}x{row[4]} | Rp {row[5]}")

    return rows

def tambah_data():
    print("\n TAMBAH DATA KERTAS ")
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

def update_harga():
    rows = tampil_data()
    if not rows:
        return

    try:
        pilihan = int(input("\nPilih nomor yang ingin diupdate: "))
        if pilihan < 1 or pilihan > len(rows):
            print("Pilihan tidak valid!")
            return

        selected = rows[pilihan - 1]
        id_data = selected[0]

        harga_input = input("Masukkan Harga Baru: ")
        harga_baru = parse_harga(harga_input)

        cursor.execute("""
        UPDATE kertas
        SET harga = ?
        WHERE id = ?
        """, (harga_baru, id_data))

        conn.commit()
        print("Harga berhasil diupdate!")

    except ValueError:
        print("Input tidak valid!")

def hapus_data():
    rows = tampil_data()
    if not rows:
        return

    try:
        pilihan = int(input("\nPilih nomor yang ingin dihapus: "))
        if pilihan < 1 or pilihan > len(rows):
            print("Pilihan tidak valid!")
            return

        selected = rows[pilihan - 1]
        id_data = selected[0]

        cursor.execute("DELETE FROM kertas WHERE id = ?", (id_data,))
        conn.commit()

        print("Data berhasil dihapus!")

    except ValueError:
        print("Input tidak valid!")

while True:
    print("\n MENU UTAMA ")
    print("1. Tambah Data Kertas")
    print("2. Lihat Data Kertas")
    print("3. Update Harga Kertas")
    print("4. Hapus Data Kertas")
    print("5. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        tambah_data()
    elif pilih == "2":
        tampil_data()
    elif pilih == "3":
        update_harga()
    elif pilih == "4":
        hapus_data()
    elif pilih == "5":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid!")

conn.close()