def ESieve(N):
    l = [True for i in range(N)]
    l[0]=l[1]=False

    for p, isprime in enumerate(l):
        if isprime:
            for i in range(p*p, N, p):
                l[i] = False
    return [p for p, isprime in enumerate(l) if isprime]

N = 10**3
primes = ESieve(N)

def factor(n):
    factors = []
    while n > 1:
        for p in primes:
            deg = 0
            while n%p == 0:
                n = n//p
                deg += 1
            if deg: factors.append((p, deg))
    return factors

def find_prime_length(p):
    r = 1
    length = 0
    while True:
        while r < p: 
            r *= 10
            length += 1
        r %= p
        if r == 1: return length

memo = {}
for p in primes:
    if p in set([2,5]): continue
    p_power = p
    while p_power < N:
        memo[p_power] = find_prime_length(p_power)
        p_power *= p

def gcd(a,b):
    if a<b: a,b = b,a
    r = a%b
    while r != 0:
        r, a, b = a%b, b, r
    return b
def lcm(a,b):
    return a*b//gcd(a,b)

def cycle_length(n):
    n_factors = factor(n)
    l = 1
    for p, deg in n_factors:
        if p in set([2,5]): continue
        c_len = memo[p**deg]
        l = lcm(l, c_len)
    return l

if __name__ == '__main__':
    import time
    start = time.time()
    m, max_n = 0, 0
    for n in range(2, N): 
        c_len = cycle_length(n)
        if c_len > m: 
            m, max_n = c_len, n
    print(max_n)
    print(time.time()-start)

