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

# List of Abundant Numbers under 29000
abundant_num = []
for num in range(1,29000):
    sum = 0
    for factor in getFactors(num):
        sum += factor
    if (num < sum):
        abundant_num.append(num)

print(len(abundant_num))

print('a')

list = []
i = 0
while i < len(abundant_num):
    j = i
    while j < len(abundant_num):
        n = abundant_num[i] + abundant_num[j]
        unique = True
        for el in list:
            if (el == n or n>=28999):
                unique = False
                break
            elif (el < n):
                break
        if (unique):
            list.append(n)
        j += 1
    i += 1

print(len(list))

sum = 0
sum1 = 0
for i in range(57998):
    sum1 += i

sum2 = 0
for j in list:
    sum2 += j

print('c')
print(sum1 - sum2)
#print(list)
#print(abundant_num)
