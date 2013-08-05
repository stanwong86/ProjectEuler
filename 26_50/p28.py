total = 1001*1001
sum = 1
i = 1
n = 1
while i < total:
    for x in range(4):
        i += 2*n
        sum += i
        if(i >= 1002001):
            break
    n += 1
print(i,sum)
