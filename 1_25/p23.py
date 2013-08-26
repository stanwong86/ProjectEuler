# function for factorial
def getFactors(n):
    factors = []
    for i in range(1,n):
        if (n % i) == 0:
            if (n/i) < i:
                break
            elif (n/i) == i or i==1:
                factors.append(i)
            else:
                factors.append(i)
                factors.append(int(n/i))
    return factors

def write_to_file():
    f = open('abundant_num.txt','w')
    # List of Abundant Numbers under 28123
    abundant_num = []
    for num in range(11,28123):
        sum = 0
        for factor in getFactors(num):
            sum += factor
        if (num < sum):
            #abundant_num.append(num)
            f.write('%s,' % num)
    f.close()
    abundant_num.pop()

#write_to_file()

f = open('abundant_num.txt','r')
line = f.readline()
abundant_num = line.split(' ')
print(len(abundant_num))
print('Abundant Numbers Loaded')

limit = 28123
total_sum = 0
for i in range(1,limit):
    total_sum += i
    
print('List Loaded')

i = 0
dict = {}
while i < len(abundant_num):
    j = i
    while j < len(abundant_num):
        n = int(abundant_num[i]) + int(abundant_num[j])
        if n < limit:
            dict[n]=1
        j += 1
    i += 1

sum = 0
for i in range(limit):
    if(not dict.get(i)):
        sum += i
print('Final Answer',(sum))
