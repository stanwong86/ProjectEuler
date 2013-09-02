def triangle(n):
    return n*(n+1)/2

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)


tn = 286
pn = 166
hn = 144

found = False
while(not found):
    t = triangle(tn)
    p = pentagonal(pn)
    h = hexagonal(hn)
    if t == p and t == h:
        found = True
    else:
        smallest = min(t,p,h)
        if smallest == t:
            tn += 1
        elif smallest == p:
            pn += 1
        else:
            hn += 1

print(tn,triangle(tn))
print(pn,pentagonal(pn))
print(hn,hexagonal(hn))
