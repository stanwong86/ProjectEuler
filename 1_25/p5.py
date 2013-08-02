'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def prime_no(n):
    prime = [2,3]
    x = 3
    count = len(prime)
    while count < n:
        x += 2
        test = True
        for i in prime:
            if (x % i == 0):
                test = False
                break
        if test:
            prime.append(x)
        count = len(prime)
    return x

#print(prime_no(10001))


factors = [2]
for n in range (3,21):
    for i in factors:
        if(n % i == 0):
            n /= i
    if n > 1:
        factors.append(n)
print(factors)

product = 1
for x in factors:
    product *= x
print(product)
