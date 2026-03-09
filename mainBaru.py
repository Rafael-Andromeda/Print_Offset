import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
import sys

# exe
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = os.path.join(BASE_DIR, "database.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


# login logic

def login():

    username = entry_user.get()
    password = entry_pass.get()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT role FROM users WHERE username=? AND password=?",
        (username, password)
    )

    result = cursor.fetchone()
    conn.close()

    if result:

        role = result[0]
        root.withdraw()

        if role == "admin":
            admin_dashboard()
        else:
            staff_dashboard()

    else:
        messagebox.showerror("Error", "Login gagal")


# logout logic

def logout(win):
    win.destroy()
    root.deiconify()


# Admin

def admin_dashboard():

    win = tk.Toplevel(root)
    win.title("Admin Dashboard")
    win.geometry("600x500")

    tk.Label(win, text="Menu Admin", font=("Arial", 16)).pack(pady=10)

    tk.Button(win, text="Lihat Orders", command=lihat_orders).pack(pady=5)
    tk.Button(win, text="Tambah Order", command=tambah_order).pack(pady=5)
    tk.Button(win, text="Manajemen User").pack(pady=5)

    tk.Button(win, text="Logout", command=lambda: logout(win)).pack(pady=20)


# staff
def staff_dashboard():

    win = tk.Toplevel(root)
    win.title("Staff Dashboard")
    win.geometry("600x500")

    tk.Label(win, text="Menu Staff", font=("Arial", 16)).pack(pady=10)

    tk.Button(win, text="Tambah Order", command=tambah_order).pack(pady=5)
    tk.Button(win, text="Lihat Orders", command=lihat_orders).pack(pady=5)

    tk.Button(win, text="Logout", command=lambda: logout(win)).pack(pady=20)


# new order logic
def tambah_order():

    win = tk.Toplevel(root)
    win.title("Tambah Order")
    win.geometry("400x300")

    tk.Label(win, text="Customer").grid(row=0, column=0, pady=10)
    tk.Label(win, text="Job Cetak").grid(row=1, column=0, pady=10)
    tk.Label(win, text="Quantity").grid(row=2, column=0, pady=10)

    customer = tk.Entry(win)
    job = tk.Entry(win)
    qty = tk.Entry(win)

    customer.grid(row=0, column=1)
    job.grid(row=1, column=1)
    qty.grid(row=2, column=1)

    def simpan():

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO orders (customer,job,quantity) VALUES (?,?,?)",
            (customer.get(), job.get(), qty.get())
        )

        conn.commit()
        conn.close()

        messagebox.showinfo("Sukses", "Order disimpan")
        win.destroy()

    tk.Button(win, text="Simpan", command=simpan).grid(row=3, column=1, pady=20)


#  show order logic
def lihat_orders():

    win = tk.Toplevel(root)
    win.title("Daftar Orders")
    win.geometry("400x300")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders")
    data = cursor.fetchall()

    conn.close()

    for row in data:
        tk.Label(win, text=row).pack()


# window login logic
root = tk.Tk()
root.title("Login")
root.geometry("400x300")

tk.Label(root, text="Username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack(pady=20)

root.mainloop()