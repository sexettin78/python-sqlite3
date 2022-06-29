#SELECT * FROM uyeler isim LIKE "F%D" (baş harfi F son harfi D olan kayıtları listeledik)
#SELECT * FROM uyeler isim LIKE "%d%" (içinde d olan kayıtları listeledik)
#SELECT * FROM uyeler isim LIKE "furkan%" (furkan ile başlayan ama de devamında ne olduğunu hatırlamadığımız kolonları güncelledik)
#DELETE FROM uyeler WHERE isim LIKE 'furkan%' (furkan ile başlayan ama de devamında ne olduğunu hatırlamadığımız kolonları sildik)
#UPDATE uyeler SET sifre = "yenisifre" WHERE isim LIKE 'furkan%' (furkan ile başlayan tüm verilerin şifresini değiştirdik)

# % işaretinin olduğu kısmı sqlite otomatik olarak dolduruyor