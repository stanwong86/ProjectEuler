def sum_of_div(n):
    factors = []
    for i in range(1,int(n/2)):
        if(int(n/i) < i):
            break
        if(i*i == n):
            factors.append(i)
            break
        if(i == 1):
            factors.append(i)
        elif(n % i) == 0:
            factors.append(i)
            factors.append(int(n/i))
    return sum(factors)
    
amicable_nums = []
for a in range(1,10000):
    b = sum_of_div(a)
    res = sum_of_div(b)
    if(a == res and a != b):
        amicable_nums.append(a)
print(sum(amicable_nums))
