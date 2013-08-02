'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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

print(prime_no(10001))
