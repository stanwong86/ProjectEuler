best = 0
best_p = 0

for p in range(1,1000):
    a = 0
    b = 1
    count = 0

    while a < int(p/3):
        a += 1
        b = a
        while b < int(p/2):
            b += 1
            c = p - a - b
            if a > b or b > c or a > c:
                pass
            elif (a+b) <= c:
                pass
            elif(a**2 + b**2 == c**2):
                count += 1
                
    if count > best:
        print(p, count)
        best = count
        best_p = p
