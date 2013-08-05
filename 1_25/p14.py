'''
n  n/2 (n is even)
n  3n + 1 (n is odd)
'''


def collatz(n):
    global count
    count += 1
    if(n <= 1):
        return
    elif(n % 2 == 0):
        return collatz(n/2)
    else:
        return collatz(3*n + 1)


greatest = -1
for i in range(1,1000000,2):
    count = 0
    collatz(i)
    if count > greatest:
        greatest = count
        print("i:"+str(i)+", count:"+str(count))
    
    
print('greatest = '+str(greatest))
