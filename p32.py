'''
def permute(n):
    list = []
    s = str(n)
    list.append(n)
    for a in range(0,len(s)):
        for b in range(0,len(s)):
            if(a == b):
                continue
            else:
                if(a <= b):
                    s = s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]
                else:
                    s = s[:b] + s[a] + s[b+1:a] + s[b] + s[a+1:]
                list.append(int(s))
    return list
'''

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
list = permute(n)

for num in list:
    for a in range(0, int(len(n)/2)):
        for b in range((a+1),len(n)-a-1):
            num_a = int(num[:a+1])
            num_b = int(num[a+1:a+1+b+1])
            num_c = int(num[a+b+1:])
            #if num_b >= num_a:
            #    break
            if((num_a * num_b) == num_c):
                print(num,num_a,num_b)

#print(list)
#print(len(list))
