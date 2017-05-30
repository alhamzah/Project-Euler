import time
start = time.time()

primes = [2]
primes_set = {2}
def find_next_prime():
    n = primes[-1]
    found = False
    while not found:
        found = True
        n += 1
        for p in primes:
            if n%p == 0: 
                found = False
                break
    primes.append(n)
    primes_set.add(n)
    return

while primes[-1] < 1001: find_next_prime()
b_range = len(primes)

longest = (0, (0,0))
for i in range(b_range):
    b = primes[i]
    for a in range(-b, 1000):
        def f(n):
            return n**2+a*n+b
        n = 0
        while f(n) in primes_set: 
            n+=1
            while f(n) > primes[-1]: find_next_prime()

        if n > longest[0]: longest = (n, (a,b))

if __name__ == '__main__':
    print(longest[1][0]*longest[1][1])
    print(time.time()-start)
