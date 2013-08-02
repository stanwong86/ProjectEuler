# Monday = 1, Sunday = 7
def date_to_days(year,month,day):
    days = 0
    years = (year - 1900)
    # standard years
    days += years*365
    
    # leap years
    days += (years/4+1)
    days -= (years/100+1)
    days += ((years+300)/400)
    if years % 4 == 0 and month <= 2 and day < 29:
        days -= 1
        
    # months
    month_dict = [31,28,31,30,31,30,31,31,30,31,30,31]
    for m in range(0,month-1):
        days += month_dict[m]

    # days
    days += day
    return days

def day_of_week(n):
    return (days % 7) +1

days = date_to_days(1901,1,1)
print day_of_week(days)
print(date_to_days(1901,1,1))
