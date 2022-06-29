import sqlite3
db = sqlite3.connect("veritabani.db")
cr = db.cursor() #işlemler yapmak için işlem oluşturmak gerekli
#cr.execute("SQL SORGUSU BURAYA YAZILIR")
cr.execute("CREATE TABLE tabloadi ('kolon1', 'kolon2')")
