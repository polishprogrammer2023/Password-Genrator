import random
#start of chars
lower=[]
upper=[]
numb=[]
chars=[]
for l in range(0x61,0x7b):
	lower+=chr(l)
for u in range (0x41,0x5b):
    upper+=chr(u)
for n in range (0x30,0x3a):
    numb+=chr(n)
#chars
for c in range(0x21,0x30):
    chars+=chr(c)
for h in range(0x3a,0x41):
    chars+=chr(h)
for a in range(0x5b,0x61):
    chars+=chr(a)
for r in range(0x7b,0x7f):
    chars+=chr(r)
all=lower+upper+numb+chars
#end of chars
#main
print("Password generator 1.0")
leng=int(input("Input password lenght: "))
pas=""
for i in range(leng+1):
    pas+=random.choice(all)
print("You password is:",end=" ")
print(pas)