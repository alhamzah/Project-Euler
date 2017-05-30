import time
start = time.time()
memo = {1:1, 2:1}

def febonacci(n):
    if n not in memo: 
        febonacci(n-2)
        febonacci(n-1)
        memo[n] = febonacci(n-1)+febonacci(n-2)
    return memo[n]

if __name__ == '__main__':
    n = 1
    while febonacci(n) < 10**999: n+=1
    print(n, time.time() - start)