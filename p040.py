N = 10**6
limits = [(0,1)]
n = 1
while limits[-1][1] < N:
    limits.append((limits[-1][1], n*9*10**(n-1)+limits[-1][1]))
    n += 1

def find_range(n):
    i = 0
    while n >= limits[i][1]: i+=1
    return i

def find_digit(n):
    l = find_range(n)
    ord_n = (n-limits[l][0])//l
    return int(str(10**(l-1)+ord_n)[(n-limits[l][0])%l])

if __name__ == '__main__':
    product = 1
    for i in range(2,7):
        product *= find_digit(10**i)
    print(product)
