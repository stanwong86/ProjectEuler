'''
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''

from prime import *
import timeit

start = timeit.default_timer()

prime_list = prime_no(7071)
list = []

square_limit = len(prime_list)  #908
cube_limit = len(prime_no(368)) # 73
quad_limit = len(prime_no(84))# 23

a = 0
while a < square_limit:
    square_no = prime_list[a]**2
    b = 0
    while b < cube_limit:
        c = 0
        cube_no = prime_list[b]**3
        #if (square_no + cube_no) > 50000000:
            #break add count
        while c < quad_limit:
            quad_no = prime_list[c]**4
            sum = square_no + cube_no + quad_no
            if(sum > 50000000):
                break
            list.append(sum)
            c+=1
        b+=1
    a+=1

# Remove dupes
print('List including Dupes', len(list)) #1139575
print('List without Dupes',len(set(list)))

stop = timeit.default_timer()
print stop - start 
