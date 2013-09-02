'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

dict = {'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26
        }
# Get list of words from file
f = open('words.txt','wr')
lines = f.readline()
words = lines.replace('"','').split(',')

# generate triangle numbers
def tri_num(n):
    return (n*(n+1)/2)

tri_numbers = []
for i in range(1,100):
    tri_numbers.append(tri_num(i))

# calculate word value
count = 0
for word in words:
    sum = 0
    for ch in word:
        sum += dict[ch]
    if tri_numbers.count(sum) > 0:
        print(word)
        count += 1
print(count)
