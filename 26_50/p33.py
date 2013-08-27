non_trivial = []
for a in range(10,100):
    for b in range(10,100):
        num = str(a)
        den = str(b)
        if num[-1] == den[0] and int(num[0]) < int(den[-1]):
            if (1.0*a/b) == 1.0*int(num[0])/int(den[-1]):
                print(a,b)
                non_trivial.append((a,b))
        elif num[0] == den[-1] and int(num[-1]) < int(den[0]):
            if (1.0*a/b) == 1.0*int(num[-1])/int(den[0]):
                print(a,b)
                non_trivial.append((a,b))

num = 1
den = 1
for frac in non_trivial:
    num *= frac[0]
    den *= frac[-1]

c = 2
while(c <= num):
    while( num % c == 0 and den % c == 0):
        num /= c
        den /= c
    c += 1
print (num,den)
