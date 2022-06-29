import sqlite3
db = sqlite3.connect("veritabani.db")
cr = db.cursor()

#sorgu
cr.execute("SELECT isim, soyisim FROM uyeler WHERE soyisim = 'd'")

#listele
cekilen_veri = cr.fetchall()
print(cekilen_veri)

print(cekilen_veri[0][1]) #bu şekilde ilk üyenin 2.kolonu yani soyadını yazdırdık

#bu döngü ile daha okunaklı bir veri elde edebiliriz
for veri in cekilen_veri:
    print("İsim: "+veri[0])
    print("Soyisim: "+veri[1])
    print()