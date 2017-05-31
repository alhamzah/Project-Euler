def ESieve(N):
    l = [True for i in range(N)]
    l[0]=l[1]=False

    for p, isprime in enumerate(l):
        if isprime:
            for i in range(p*p, N, p):
                l[i] = False
    return [p for p, isprime in enumerate(l) if isprime]

N = max([n*n-79*n+1601 for n in range(80)])
primes = ESieve(N)
primes_set = set(primes)

longest, i, b = (0, (0,0)), 0, primes[0]
while b <= 1000:
    b = primes[i]
    i += 1
    for a in range(-b, 1000):
        def f(n):
            return n**2+a*n+b
        n = 0
        while f(n) in primes_set: n+=1
        if n > longest[0]: longest = (n, (a,b))

print(longest[1][0]*longest[1][1])
