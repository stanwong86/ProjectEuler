def parse_digits(n):
    sum = 0
    sum_str = ''
    if dict.get(n):
        sum_str += dict[n]
        #print('get'+str(sum))
    elif n >= 21 and n <= 99:
        tens = dict.get(int(str(n)[0]+'0'))
        units = dict.get(int(str(n)[-1]))
        #print('get_tens'+str(tens))
        #print('get_units'+str(units))
        sum_str += tens + units
    elif n >= 100 and n <= 999:
        hundreds = dict.get(int(str(n)[0]))
        other_temp = int(str(n)[1:])
        if(other_temp == 0):
            other = ''
        else:
            other = parse_digits(other_temp) + 'and'
        
        #print('get_other'+str(other))
        #print(hundreds)
        sum_str += hundreds + 'hundred' + other
    return sum_str

dict = {}
dict[1] = 'one'
dict[2] = 'two'
dict[3] = 'three'
dict[4] = 'four'
dict[5] = 'five'
dict[6] = 'six'
dict[7] = 'seven'
dict[8] = 'eight'
dict[9] = 'nine'
dict[10] = 'ten'
dict[11] = 'eleven'
dict[12] = 'twelve'
dict[13] = 'thirteen'
dict[14] = 'fourteen'
dict[15] = 'fifteen'
dict[16] = 'sixteen'
dict[17] = 'seventeen'
dict[18] = 'eighteen'
dict[19] = 'nineteen'
dict[20] = 'twenty'
dict[30] = 'thirty'
dict[40] = 'forty'
dict[50] = 'fifty'
dict[60] = 'sixty'
dict[70] = 'seventy'
dict[80] = 'eighty'
dict[90] = 'ninety'
dict[1000] = 'onethousand'


sum = 0
for number in range(1,1001):
    sum += len(parse_digits(number))
print sum


# 342 yields 23 letters
# 115 yields 20 letters
# 999 yields 24 letters
# 100 yields 10 letters

'''
x = 1000
print(len(parse_digits(x)))
print(parse_digits(x))
'''
