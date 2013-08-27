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

# Get rotations of number n
def rotations(n):
    list = []
    s = str(n)
    for i in range(len(s)):
        list.append(s)
        s = s[-1] + s[:-1]
    return list

n = 1000000
circular_prime = []
prime_list = prime_no(n)

for p in prime_list:
    permute_list = rotations(p)    
    circular = True
    for current in permute_list:
        try:
            if prime_list.index(int(current)):
                continue
        except ValueError:
            circular = False
            break
    if circular:
        circular_prime.append(int(current))

print(len(circular_prime))
