import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    role TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    job TEXT,
    quantity INTEGER
)
""")

cursor.execute("INSERT INTO users (username,password,role) VALUES ('admin','123','admin')")
cursor.execute("INSERT INTO users (username,password,role) VALUES ('staff','123','staff')")

conn.commit()
conn.close()

print("Database berhasil dibuat")