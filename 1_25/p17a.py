def parse_digits(n):
    sum = 0
    if dict.get(n):
        sum += dict[n]
        #print('get'+str(sum))
    elif n >= 21 and n <= 99:
        tens = dict.get(int(str(n)[0]+'0'))
        units = dict.get(int(str(n)[-1]))
        #print('get_tens'+str(tens))
        #print('get_units'+str(units))
        sum += tens + units
        
    elif n >= 100 and n <= 999:
        hundreds = dict.get(int(str(n)[0]))
        other_temp = int(str(n)[1:])
        other = parse_digits(other_temp)
        #print('get_other'+str(other))
        sum += hundreds + 10 + other
    #print sum
    return sum

dict = {}
dict[1] = 3
dict[2] = 3
dict[3] = 5
dict[4] = 4
dict[5] = 4
dict[6] = 3
dict[7] = 5
dict[8] = 5
dict[9] = 4
dict[10] = 3
dict[11] = 6
dict[12] = 6
dict[13] = 8
dict[14] = 8
dict[15] = 7
dict[16] = 7
dict[17] = 9
dict[18] = 8
dict[19] = 8
dict[20] = 6
dict[30] = 6
dict[40] = 5
dict[50] = 5
dict[60] = 5
dict[70] = 7
dict[80] = 6
dict[90] = 6
dict[100] = 7+3
dict[200] = 7+3
dict[300] = 7+5
dict[400] = 7+4
dict[500] = 7+4
dict[600] = 7+3
dict[700] = 7+5
dict[800] = 7+5
dict[900] = 7+4
dict[1000] = 11

sum = 0
for number in range(1,1001):
    sum += parse_digits(number)    
print sum

#print(parse_digits(342))
#print(parse_digits(999))
