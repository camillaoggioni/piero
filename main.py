import random
x= random.randint(0,50)
y= random.randint(0,50)
z= random.randint(0,50)
if x<y and x<z:
    print(x)
    if y<z:
        print (y)
        print(z)
    else :
        print(z)
        print(y)

elif y<z :
    print(y)
    if x<z :
        print(x)
        print(z)
    else :
        print(z)
        print(x)
else  :
    print(z)
    if x<y :
        print(x)
        print(y)
    else :
        print(y)
        print(x)
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")

automobili= ["berta","uga","piera","silvia","rodolfa"]
moto= ["giovanni","umberto","ignacio","rodrigo"]
motomobili= automobili + moto
motomobili.sort()
print(motomobili)
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")

import random
numeri=[]
for i in range(50):
    numeri.append(random.randint(0,1000))
dispari=[]
for x in numeri:
    if x%2==1:
        dispari.append(x)
numeri=dispari
print(numeri)
print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø")
