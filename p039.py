N = 10**3+1

def num_triangles(n):
    num_divisors = 1
    for p, deg in factor(n):
        if p == 2: deg -= 1
        num_divisors *= ((2*deg)+1)
    return num_divisors//2

memo, scores = {i*i:i for i in range(1,N)}, {}
max_sq = N**2
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