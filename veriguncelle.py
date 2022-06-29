#UPDATE uyeler SET email = 'furkand@leafyet.studio', sifre='deneme123' (bütün verilerin şifresi ve emailini değiştirir)
#UPDATE uyeler SET email = 'cerez@leafyetstudio.xyz' WHERE isim = 'cerez' (sadece çerezin emailini değiştirdik)

import sqlite3
db = sqlite3.connect("veritabani.db")
cr = db.cursor()

cr.execute("UPDATE uyeler SET email = 'cerez@leafyetstudio.xyz' WHERE isim = 'cerez'")

db.commit()