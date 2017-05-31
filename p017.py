numbers = {
    0: 0,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 7,
    1000: 12,
}

def find_letters(n):
    if n in numbers: return numbers[n]
    if n > 100: return find_letters(n//100)+find_letters(100)+3+find_letters(int(str(n)[1:]))
    return find_letters(int(str(n)[0])*10)+find_letters(int(str(n)[1]))

total = 0
for i in range(1,1001): total += find_letters(i)

total -= 3*8 
print(total)