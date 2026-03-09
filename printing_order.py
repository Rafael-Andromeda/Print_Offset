import tkinter as tk
from tkinter import ttk

def hitung_harga():

    qty = int(entry_qty.get())
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())

    bahan = combo_bahan.get()
    finishing = combo_finishing.get()

    # harga bahan per rim
    harga_bahan = {
        "Art Paper": 120000,
        "Art Carton": 150000
    }

    harga_finishing = {
        "Tanpa": 0,
        "Laminasi Doff": 200,
        "Laminasi Glossy": 200
    }

    rim_price = harga_bahan.get(bahan,0)
    finish_price = harga_finishing.get(finishing,0)

    # asumsi 1 rim = 500 lembar
    harga_per_lembar = rim_price / 500

    total = (harga_per_lembar + finish_price) * qty

    label_harga.config(text=f"Rp {round(harga_per_lembar,2)}")
    label_rim.config(text=f"Rp {rim_price}")
    label_total.config(text=f"Rp {round(total,2)}")


root = tk.Tk()
root.title("Kalkulator Harga Cetak Brosur")
root.geometry("500x420")

title = tk.Label(root,text="Hitung Harga Cetak Brosur",font=("Arial",14))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

# Quantity
tk.Label(frame,text="Quantity").grid(row=0,column=0,sticky="w")
entry_qty = tk.Entry(frame)
entry_qty.insert(0,"0")
entry_qty.grid(row=0,column=1)

# Panjang
tk.Label(frame,text="Panjang (cm)").grid(row=1,column=0,sticky="w")
entry_panjang = tk.Entry(frame)
entry_panjang.insert(0,"0")
entry_panjang.grid(row=1,column=1)

# Lebar
tk.Label(frame,text="Lebar (cm)").grid(row=2,column=0,sticky="w")
entry_lebar = tk.Entry(frame)
entry_lebar.insert(0,"0")
entry_lebar.grid(row=2,column=1)

# Warna
tk.Label(frame,text="Warna").grid(row=3,column=0,sticky="w")
combo_warna = ttk.Combobox(frame,values=["Full Colour","1 Warna"])
combo_warna.current(0)
combo_warna.grid(row=3,column=1)

# Cetak
tk.Label(frame,text="Cetak").grid(row=4,column=0,sticky="w")
combo_cetak = ttk.Combobox(frame,values=["1 Muka","2 Muka"])
combo_cetak.current(0)
combo_cetak.grid(row=4,column=1)

# Bahan
tk.Label(frame,text="Bahan").grid(row=5,column=0,sticky="w")
combo_bahan = ttk.Combobox(frame,values=["Art Paper","Art Carton"])
combo_bahan.current(0)
combo_bahan.grid(row=5,column=1)

# Ketebalan
tk.Label(frame,text="Ketebalan GSM").grid(row=6,column=0,sticky="w")
combo_gsm = ttk.Combobox(frame,values=["150","210","260"])
combo_gsm.current(0)
combo_gsm.grid(row=6,column=1)

# Finishing
tk.Label(frame,text="Finishing").grid(row=7,column=0,sticky="w")
combo_finishing = ttk.Combobox(frame,values=["Tanpa","Laminasi Doff","Laminasi Glossy"])
combo_finishing.current(0)
combo_finishing.grid(row=7,column=1)

# Tombol
btn = tk.Button(root,text="Cek Harga",command=hitung_harga)
btn.pack(pady=10)

# Output
result_frame = tk.Frame(root)
result_frame.pack()

tk.Label(result_frame,text="Harga / Lembar").grid(row=0,column=0)
label_harga = tk.Label(result_frame,text="Rp 0")
label_harga.grid(row=0,column=1)

tk.Label(result_frame,text="Harga Rim").grid(row=1,column=0)
label_rim = tk.Label(result_frame,text="Rp 0")
label_rim.grid(row=1,column=1)

tk.Label(result_frame,text="Total Order").grid(row=2,column=0)
label_total = tk.Label(result_frame,text="Rp 0")
label_total.grid(row=2,column=1)

root.mainloop()