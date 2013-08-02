f1 = 1
f2 = 1

i = 3
f3 = f1 + f2
while(len(str(f3)) < 1000):
    #print("F" + str(i) + ' = ' + str(f3))
    f1 = f2
    f2 = f3
    i += 1
    f3 = f1 + f2    
print("F" + str(i) + ' = ' + str(f3))
