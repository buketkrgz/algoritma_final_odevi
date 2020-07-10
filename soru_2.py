sayi = int(input(" Bir sayı giriniz:"))
i = 0
toplam = 0
faktöriyel = 1

if sayi >= 16 or sayi < 0:
    print("Lütfen 0 ile 16 arası bir sayı giriniz:")
elif sayi >= 9 and sayi < 16:
    for i in range(0,(sayi * 2) + 1,2):
        toplam = toplam+i
    print("Girilen Sayı:",sayi,"Sayının 2'şerli toplamı:",toplam)
elif sayi <9 and  sayi >=0 :
    for i in range (1,(sayi* 3) + 1 ):
        faktöriyel = faktöriyel*i

    print("Girilen Sayı:",sayi, "Sayının Faktörileyi: ",faktöriyel)
