tarih = input("Lütfen bir tarih giriniz.(Gün-Ay-Yıl) formatında:")
tarih = tarih.split("-")
gün = tarih[0]

aylar = {1:"Ocak", 2:"Şubat", 3:"Mart",4:"Nisan",5:"Mayıs",6:"Haziran",7:"Temmuz",8:"Ağustos",9:"Eylül",10:"Ekim",11:"Kasım:",
         12:"Aralık"}
ay = tarih[1]
ay= aylar[int(ay)]

yıl = tarih[2]
print(gün,"-",ay,"-",yıl)