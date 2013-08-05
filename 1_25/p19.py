# Monday = 0, Sunday = 6
def date_to_days(year,month,day):
    days = 0
    years = (year - 1900)
    
    # standard years
    days += int(years*365)
    
    # leap years
    days += int(years/4+1)
    days -= int(years/100+1)
    days += int((years+300)/400)
        
    # months
    month_dict = [31,28,31,30,31,30,31,31,30,31,30,31]
    for m in range(0,month-1):
        days += month_dict[m]

    # days
    days += day
    return days

#print(date_to_days(1901,1,1) % 7)
#print(date_to_days(1900,1,1) % 7)

count = 0
for year in range(1901,2000):
    for month in range(1,13):
        if date_to_days(year,month,1) % 7 == 0:
            count += 1
print(count)
