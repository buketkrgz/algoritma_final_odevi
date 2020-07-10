harf_sayi={
    "a":1,
    "b":2,
    "u": 21,
    "k":11,
    "e": 5,
    "t":20,
    "r":18,
    "g":7,
    "o":15,
    "z":26
        }

A=[[1,2,-1],[2,5,-2],[-1,2,2]]

b=harf_sayi.get("b")
u=harf_sayi.get("u")
k=harf_sayi.get("k")
e=harf_sayi.get("e")
t=harf_sayi.get("t")
a=harf_sayi.get("a")
r=harf_sayi.get("r")
g=harf_sayi.get("g")
o=harf_sayi.get("o")
z=harf_sayi.get("z")


buk=[[b,u,k]]
etk=[[e,t,k]]
ara=[[a,r,a]]
goz=[[g,o,z]]


def sifre(a,b):
    sonuc = [[0,0,0]]

    liste = []
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                sonuc[i][j] += a[i][k] * b[k][j]
    return sonuc
print("BUK:",sifre(buk,A))
print("ETK:",sifre(etk,A))
print("ARA:",sifre(ara,A))
print("GOZ:",sifre(goz,A))



