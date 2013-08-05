'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def factorial(n):
    product = 1

    for i in range(n):
        product *= (i+1)
    return product

print(factorial(9))
total = 0
for n in range(3,1000000):
    str_n = str(n)
    sum = 0
    for digit in str_n:
        sum += factorial(int(digit))
    if sum == n: print(n); total += n
    
print('total'+str(total))
