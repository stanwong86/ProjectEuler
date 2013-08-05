total = 0
for num in range(2,1000000):
    sum = 0
    for letter in str(num):
        sum += int(letter)**5
    if sum == num:
        print(num)
        total += num
    
print(total)
