import time
start = time.time()

def ESieve(N):
    l = [True]*N
    l[0]=l[1]=False

    for p, isprime in enumerate(l):
        if isprime:
            for i in range(p*p, N, p): l[i] = False
    return [p for p, isprime in enumerate(l) if isprime]

N = 10**6
primes = ESieve(N)
primes_set = set(primes)

min_k = 0
cumulative_sum = [0]
for i in range(len(primes)):
    cumulative_sum.append(primes[i]+cumulative_sum[i])
# for i in range(len(primes)):
#     if cumulative_sum[i] > N:
#         min_k = cumulative_sum[i]
#         break
print(time.time()-start)

def get_sum(i,j):
    return cumulative_sum[j]-cumulative_sum[i]


def most_primes():
    for k in range(len(primes)-1, 1, -1):
        for i in range(len(primes)-k):
            p_sum = get_sum(i,i+k)
            if p_sum > N: break
            if p_sum in primes_set: return (p_sum, k)

if __name__=='__main__':
    print(most_primes())
    print(time.time()-start)