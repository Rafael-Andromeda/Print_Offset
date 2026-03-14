# import math
# def hitung_kertas():
#     qty = int(input("Masukkan Total Cetakan: "))
#     ptng_plano = int(input("Masukkan TOtal Potong per Plano: "))
    
#     jumlah_plano = math.ceil(qty / ptng_plano)
    
#     print(f"Total Plano yang Dibutuhkan: {jumlah_plano}")

# hitung_kertas()

# import math

# def hitung_plano():
#     print("Pilih ukuran plano:")
#     print("1. 61 x 86")
#     print("2. 65 x 200")
#     print("3. 79 x 109")
#     print("4. 90 x 120")

#     ukuran_plano = input("Masukkan pilihan ukuran plano (1-4): ")
#     total_kertas = int(input("Masukkan total kertas yang akan dicetak: "))
#     potong_per_plano = int(input("Masukkan jumlah potong per plano: "))

#     jumlah_plano = math.ceil(total_kertas / potong_per_plano)

#     print("Ukuran plano yang dipilih:", ukuran_plano)
#     print("Jumlah plano yang dibutuhkan =", jumlah_plano)

# hitung_plano()

import math

def hitung_plano():

    # daftar ukuran plano (cm)
    planos = {
        "A (61 x 86)": (61, 86),
        "B (65 x 200)": (65, 200),
        "C (79 x 109)": (79, 109),
        "D (90 x 120)": (90, 120)
    }

    # input ukuran desain
    lebar = int(input("Masukkan lebar desain (cm): "))
    tinggi = int(input("Masukkan tinggi desain (cm): "))
    qty = int(input("Masukkan total cetakan: "))

    hasil = {}

    print("\n=== Perhitungan Efisiensi ===")

    for nama, (p_lebar, p_tinggi) in planos.items():

        # orientasi normal
        potong1 = (p_lebar // lebar) * (p_tinggi // tinggi)

        # orientasi diputar
        potong2 = (p_lebar // tinggi) * (p_tinggi // lebar)

        potong_terbaik = max(potong1, potong2)

        hasil[nama] = potong_terbaik

        print(f"{nama} → {potong_terbaik} potong per plano")

    # mencari plano paling efisien
    plano_terbaik = max(hasil, key=hasil.get)
    potong_terbaik = hasil[plano_terbaik]

    jumlah_plano = math.ceil(qty / potong_terbaik)

    print("\n=== Hasil Terbaik ===")
    print("Plano paling efisien:", plano_terbaik)
    print("Potong per plano:", potong_terbaik)
    print("Jumlah plano dibutuhkan:", jumlah_plano)


hitung_plano()