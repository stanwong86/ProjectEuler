'''
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
'''
array = []
# Import data into array
for line in open('py11.txt'):
    line = line.rstrip('\n')
    x = line.split(' ')
    array.append(x)

print('Horizontal')
prod_horizontal = 1
for a in range(0,len(array)):
    for b in range(0,len(array[a])-3):
        current_prod = int(array[a][b]) * int(array[a][b+1]) * int(array[a][b+2]) * int(array[a][b+3])
        if (current_prod > prod_horizontal):
            prod_horizontal = current_prod
            #print(str(a)+','+str(b)+','+str(current_prod))

print(prod_horizontal)

print('\nVertical')
prod_vertical = 1
for a in range(0,len(array)-3):
    for b in range(0,len(array[a])):
        current_prod = int(array[a][b]) * int(array[a+1][b]) * int(array[a+2][b]) * int(array[a+3][b])
        if (current_prod > prod_vertical):
            prod_vertical = current_prod
            #print(str(a)+','+str(b)+','+str(current_prod))

print(prod_vertical)

print('\nDiag Neg')
prod_diagonal_neg = 1
for a in range(0,len(array)-3):
    for b in range(0,len(array[a])-3):
        current_prod = int(array[a][b]) * int(array[a+1][b-1]) * int(array[a+2][b-2]) * int(array[a+3][b-3])
        if (current_prod > prod_diagonal_neg):
            prod_diagonal_neg = current_prod
            #print(str(a)+','+str(b)+','+str(current_prod))

print(prod_diagonal_neg)

print('\nDiag Pos')
prod_diagonal_pos = 1
for a in range(3,len(array)):
    for b in range(3,len(array[a])):
        current_prod = int(array[a][b]) * int(array[a-1][b-1]) * int(array[a-2][b-2]) * int(array[a-3][b-3])
        if (current_prod > prod_diagonal_pos):
            prod_diagonal_pos = current_prod
            #print(str(a)+','+str(b)+','+str(current_prod))

print(prod_diagonal_pos)

