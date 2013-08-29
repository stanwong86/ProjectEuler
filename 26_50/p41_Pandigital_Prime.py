We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

# Returns list of possible values
def permute(s):
    if len(s) <= 1:
        return s
    list = []
    for i in range(0,len(s)):
        sub_list = permute(s[:i]+s[i+1:])
        for x in sub_list:
            list.append(s[i]+x)
    return list


# check if prime
def prime(n):
    if n % 2 == 0:
        return False
    i = 3
    while (i*i) < n:
        if(n % i) == 0:
            return False
        i += 2
    return True

# Create list of unique pandigital numbers
n = ''
for digit in range(1,9):
    n += str(digit)
    list = permute(n)
    pandigital = []

    sorted(list)
    for i in range(len(list)-1,-1,-1):
        if prime(int(list[i])):
            print(list[i])
            break
