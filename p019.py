months = {2: 29,
          4: 30,
          6: 30,
          9: 30,
          11: 30}
for i in range(1, 13):
    if i not in months: months[i] = 31

YEAR = (sum(months.values()))

def count_days(m, y):
    days = YEAR
    sundays = 0
    for year in range(1901, y):
        days -= 31
        for month in range(1,13):
            if year == y and month > m: break
            days += months[month]
            if month == 2 and y%4 == 0 and not (y%100 != 0 and not y%400 == 0) : days -= 1
            if days % 7 == 0: sundays += 1
    return sundays

if __name__ == '__main__':
    print(count_days(1, 2001))



