#2. alkalom




'''szam = input("Kérek egy számot: ")
if  szam.isdigit():
    szam = int(szam)
    if szam > 0:
        print("pozitiv")
    elif szam == 0:
        print("a szám sem nem pozitiv se nem negatív")
else:
    print("nem számot adtál meg")'''

'''
jegy = int(input("Kérek egy érdemjegyet"))
while jegy < 1 or jegy == 0 or jegy > 5:
    jegy = int(input("Kérek egy érdemjegyet"))
    if jegy == 10:
        print("csillagos ötös")
        break

print("Gratulálunk")

'''
'''
kocka = random.randint(1,6)
while True:
    tipp = int(input("Kérem egy tippet"))
    if tipp == kocka:
        break
print("Sikerült eltalálnod")
'''
'''
for elem in range(5):
    print(elem)
'''
'''
def fv(): new *
        pass

for elem in range(1,6):
    print(elem, "Nem leszek többet rossz!")
    if elem == 3:
        continue
'''
'''
try:
    print(10/0)

except ZeroDivisionError:
        print("hiba 0 val osztás")
except NameError:
        print("Hiba Névhiba")
print("ok")
'''
'''
while True:
    try:
        szam = int(input("Kérek egy egész számot"))
    except:
        print ("Nem egész számot adott meg")
    else:
        break'''


import p022

a= 4
b= 5

eredmeny = p022.negyszog(a, b)
print(eredmeny)
print(f"A {eredmeny[2]} kerület =", eredmeny[0])
print(f"A {eredmeny[2]} terület =", eredmeny[1])




