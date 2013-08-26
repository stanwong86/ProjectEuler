def prime_no(n):
    prime = [2,3]
    x = 3
    while x < n:
        x += 2
        test = True
        for i in prime:
            if (x % i == 0):
                test = False
                break
            if (i*i > x):
                break
        if test:
            prime.append(x)
    return prime

# function for factorial
def getFactors(n):
    factors = []
    for i in range(1,n):
        if (n % i) == 0:
            if (n/i) < i:
                break
            elif (n/i) == i or i==1:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(int(n/i))
    return factors

if
print(prime_no(20))

