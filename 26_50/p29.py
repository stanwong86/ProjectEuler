factors = []

for a in range(2,101):
    for b in range(2,101):
        x = a ** b
        unique = True
        for i in factors:
            if x == i:
                unique = False
                break
        if unique:
            factors.append(x)
print(len(factors))
