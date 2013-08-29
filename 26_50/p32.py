def permute(s):
    if len(s) <= 1:
        return s
    list = []
    for i in range(0,len(s)):
        sub_list = permute(s[:i]+s[i+1:])
        for x in sub_list:
            list.append(s[i]+x)
    return list

n = '123456789'

# Create list of unique pandigital numbers
list = permute(n)
pandigital = []

# Permute through list to find product
for num in list:
    for a in range(0, int(len(n)/2)):
        for b in range((a+1),len(n)-a-1):
            try:
                num_a = int(num[:a+1])
                num_b = int(num[a+1:a+1+b+1])
                num_c = int(num[a+1+b+1:])
            except ValueError:
                pass
            if num_b < num_a:
                break
            elif((num_a * num_b) == num_c):
                pandigital.append((num,num_a,num_b,num_c))

# Find sum unless it is a dupe
sum = 0
#f = open('p32.txt','w')
final_list = []
for tup in pandigital:
#    f.write(str(tup) + '\n')
    if final_list.count(tup[3]) == 0:
        final_list.append(tup[3])

#f.close()

for x in final_list:
    sum += x


print(sum)
