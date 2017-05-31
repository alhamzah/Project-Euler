def pal(s):
    return s == s[::-1]

total = 0
for n in range(10**6):
    if pal(str(n)) and pal(bin(n)[2:]): total += n

print(total)