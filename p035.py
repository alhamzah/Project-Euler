from collections import deque

def ESieve(N):
    l = [True]*N
    l[0] = l[1] = False

    for i in range(N):
        if l[i]:
            for j in range(i*i, N, i):
                l[j] = False
    primes = []
    for i, isprime in enumerate(l):
        if isprime: primes.append(i)
    return primes

primes, c_primes = set(ESieve(10**6)), set()

def find_perms():
    for p in primes:
        d = deque(str(p))
        perms = []
        for i in range(len(str(p))):
            d.rotate(1)
            perms.append(''.join(d))
        c = True
        for perm in perms:
            if int(perm) not in primes: 
                c = False
                break
        if c: c_primes.add(p)

find_perms()
print(len(c_primes))






