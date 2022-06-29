import sqlite3
#SELECT name FROM sqlite_master WHERE type='table'
db = sqlite3.connect("veritabani.db")
cr = db.cursor()

#tablo isimlerini almak
cr.execute("SELECT name FROM sqlite_master WHERE type='table'")

#tablo isimlerini yazdırmak
tablolar = cr.fetchall()
print(tablolar)