import sqlite3
db = sqlite3.connect("veritabani.db")
cr = db.cursor()

#veri girişi
cr.execute("INSERT INTO tabloadi (kolon1, kolon2) VALUES ('veri1','veri2')")

#veya
#INSERT INTO tabloadi VALUES ('veri1','veri2')

#veri işle
db.commit()