'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def prime_no(n):
    prime = [2,3]
    x = 3
    sum = 5
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
            sum += x
    return sum

print(prime_no(2000000))
