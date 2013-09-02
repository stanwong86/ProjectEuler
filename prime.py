# list of prime numbers
def prime_no(n):
    prime = [2,3]
    x = 3
    while x < n:
        test = True
        for i in prime:
            if (x % i == 0):
                test = False
                break
        if test:
            prime.append(x)
        x += 2
    return prime
