def ESieve(N):
    l = [True for i in range(N)]
    l[0]=l[1]=False

    for p, isprime in enumerate(l):
        if isprime:
            for i in range(p*p, N, p):
                l[i] = False
    return [p for p, isprime in enumerate(l) if isprime]

N = 10**4+1
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

def divisors_sum(n):
    prime_div = factor(n)
    total = 1
    for p,a in prime_div: total *= (p**(a+1)-1)//(p-1)
    return total - n

divs_sum = {}
for i in range(1,10000): divs_sum[i] = divisors_sum(i)

total = 0
for i in range(3,10000):
    j = divs_sum[i]
    if j<i and divs_sum[j] == i: total+= (i+j)

print(total)