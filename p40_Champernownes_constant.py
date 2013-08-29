'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

n = ''
i = 1
while len(n) < 1000000:
    n += str(i)
    i += 1

d = [1,10,100,1000,10000,100000,1000000]
product = 1
for i in d:
    product *= int(n[i-1])

print(product)
