'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palin(n):
    str_reverse = ""
    str_n = str(n)
    length = len(str_n)
    
    if(length % 2 == 1):
        str_first = str_n[0:int(length/2)+1]
    else:
        str_first = str_n[0:int(length/2)]

    for i in range(length,int(length/2),-1):
        str_reverse += str_n[i-1]

    if str_first == str_reverse: return True
    return False
    
def largest_palindrome():
    n = 998001
    final = 1000
    while n > 10000:
        if(is_palin(n)):
            
            a = 100
            while a < 1000:
                if (n % a == 0):
                    if len(str(int(n/a))) == 3:
                        return n
                a += 1
        n -= 1
                    
print(largest_palindrome())
minx = 100*100
maxx = 999*999
#print(minx)
#print(maxx)
