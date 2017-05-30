N = 10**3+1

def num_triangles(n):
    num_divisors = 1
    for p, deg in factor(n):
        if p == 2: deg -= 1
        num_divisors *= ((2*deg)+1)
    return num_divisors//2

if __name__ == '__main__':
    import time
    start = time.time()
    memo = {i*i:i for i in range(1,N)}
    max_sq = N**2
    scores={}
    for a in range(N): 
        for b in range(a+1, N):
            sq_sum = a*a+b*b
            if sq_sum > max_sq: break
            if sq_sum in memo:
                p = a+b+memo[sq_sum]
                if p>N: break
                if p not in scores: scores[p]=set()
                scores[p].add(tuple(sorted((a,b,p-a-b))))
    s = {p:len(scores[p]) for p in scores}
    print(max(s, key=s.get))
    print(time.time()-start)

# def ESieve(N):
#     l = [True for i in range(N)]
#     l[0]=l[1]=False

#     for p, isprime in enumerate(l):
#         if isprime:
#             for i in range(p*p, N, p):
#                 l[i] = False
#     return [p for p, isprime in enumerate(l) if isprime]

# primes = ESieve(N)

# def factor(n):
#     factors = []
#     while n > 1:
#         for p in primes:
#             deg = 0
#             while n%p == 0:
#                 n = n//p
#                 deg += 1
#             if deg: factors.append((p, deg))
#     return factors