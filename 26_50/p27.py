def is_prime(n):
    if (n % 2) == 0:
        return False
    i = 3
    while n > 1:
        if (n % i == 0):
            return False
        elif (i**2 > n):
            return True
        i += 2
    return True


print(is_prime(126479))

greatest = 0

for a in range(-999,1000):
    for b in range(-999,1000):
        for n in range(0,1000):
            num = (n**2)+(a*n)+b
            if(num < 1):
                break
            prime = is_prime(num)
            if prime:
                if (n > greatest):
                    print(a,b,n,a*b)
                    greatest = n
            else:
                break
