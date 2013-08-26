def base10to2(n):
    base2 = ""
    for i in range(21,-1,-1):
        subtract = int(n/(2**i)) #1 or 0
        base2 += str(subtract)
        n -= subtract * (2**i)
    return int(base2)

def palindrome(n):
    if(str(n)[::-1] == str(n)):
        return True
    return False

sum = 0
for i in range(1000000):
    if(palindrome(i) and palindrome(base10to2(i))):
        sum += i
        

print(sum)
