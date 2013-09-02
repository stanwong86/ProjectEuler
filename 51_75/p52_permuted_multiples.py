'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

n = 100000
while n < 2000000:
    test = True
    for m in range(2,7):
        s = int(''.join(sorted(list(str(m*n)))))
        x = int(''.join(sorted(list(str(n)))))
        if x != s:
            test = False
            break
    if (test):
        print n
        break
    n += 1

#s = int(''.join(sorted(list(str(2*n)))))
#s = list(str(2*n))
#s = ''.join(sorted(s))
