memo, COINS = {}, [1, 2, 5, 10, 20, 50, 100, 200]

def C(n, m=len(COINS)):
    if n < 0 or m <= 0: return 0
    if n == 0: return 1
    if (n, m) not in memo: memo[(n,m)] = C(n-COINS[m-1], m)+C(n, m-1) 
    return memo[(n,m)]

print(C(200))