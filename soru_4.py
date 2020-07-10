import math

asal_sayılar = []

def asal_mı(sayi):
    if sayi<=1:
        return False
    if sayi==2:
        return True
    if sayi%2==0:
        return False
    for i in range(3,int(math.sqrt(sayi))+1):
        if sayi%i==0:
            return False
    return True
for i in range (1,190410): #Hocam bir basamak daha eklediğim zaman işlem süresi çok uzun oluyor.
    if asal_mı(i) == True:
        asal_sayılar.append(i)

print(asal_sayılar)
