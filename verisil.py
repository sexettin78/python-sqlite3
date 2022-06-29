#DELETE FROM uyeler WHERE isim = 'cerez' (cerezin verilerini siler)
import sqlite3
db = sqlite3.connect("veritabani.db")
cr = db.cursor()

cr.execute("DELETE FROM uyeler WHERE isim = 'cerez'")

db.commit()