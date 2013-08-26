greatest = -1
for divisor in range(2,1000):
    
    dividend = 1
    quotient = 0
    remainder = 1
    count = 0
    digits = 10000
    while(count < digits and remainder != 0):
        count += 1
        dividend = remainder * 10
        quotient = quotient*10 + int(dividend / divisor)
        remainder = dividend % divisor

    str_q = str(quotient)
    save = ""
    
    for i in range(-1,-1*digits,-1):
        if(str_q[i:] == str_q[i*2:i]):
            if(len(str_q[i:]) > greatest):
                greatest = len(str_q[i:])
                print(divisor,greatest)
            break
