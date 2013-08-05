'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

count = 0
for a in range(2):
   for b in range(3):
       for c in range(5):
           for d in range(11):
               for e in range(21):
                   for f in range(41):
                       for g in range(101):
                           for h in range(201):
                                sum = (a)*200 + (b)*100 + (c)*50 + (d)*20 + (e)*10 + (f)*5 + (g)*2 + (h)*1
                                if sum == 200:
                                    count += 1
                                elif sum > 200:
                                    break
                                else:
                                    next

print(count)
