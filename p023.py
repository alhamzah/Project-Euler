def ESieve(limit):
    L = [True]*limit
    L[0]=L[1]=False
    for p, isprime in enumerate(L):
        if isprime:
            for i in range(p*p, limit, p): L[i] = False
    return [p for p, isprime in enumerate(L) if isprime ]

N = 21823
primes = ESieve(N)
primes_set = set(primes)

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

abundant_nums, abu_list = set(), list()
for n in range(12,21823):
    if divisors_sum(n) > n: 
        abundant_nums.add(n)
        abu_list.append(n)

total, s = 0, set()
for i in range(len(abu_list)):
    for j in range(i+1): s.add(abu_list[i]+abu_list[j])

for n in range(1,21823): 
    if n not in s: total += n

print(total)