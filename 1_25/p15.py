old_list = [3,6]
new_list = []

for x in range (3,21):
    for i in range(0, len(old_list)):
        if i == 0:
            new_list.append(old_list[i]+1)    
        else:
            new_list.append(old_list[i]+new_list[i-1])
    new_list.append(new_list[-1]*2)
    print (x, new_list)    
    old_list = new_list
    new_list = []
    
    
