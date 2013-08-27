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

n = 1000000
truncate_list = []
prime_list = prime_no(n)
for prime in prime_list:
    truncatable = True
    for i in range(len(str(prime))):
        try:
            s = str(prime)
            prime_list.index(int(s[:i+1]))
            prime_list.index(int(s[i:]))
        except ValueError:
            truncatable = False
            break
    if(truncatable):
        truncate_list.append(prime)

final_list = []
sum = 0
for x in truncate_list:
    print(x)
    if (x > 9):
        final_list.append(x)
        sum += x

print (final_list)
print (len(final_list))
print (sum)
