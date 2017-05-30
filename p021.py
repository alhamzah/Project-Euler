primes = [2]
primes_set = set()
def find_next_prime():
    n, found = primes[-1], False
    while not found:
        found = True
        n += 1
        for p in primes:
            if n%p == 0: 
                found = False
                break
    primes.append(n)
    primes_set.add(n)
    # memo{n:1}

def find_prime_divisors(n):
    while n > primes[-1]: find_next_prime()
    divisors = []
    for p in primes:
        if n%p == 0: divisors.append((p, find_prime_degree(n, p)))
    return divisors

def find_prime_degree(n, p):
    counter = 0
    while n%p == 0: 
        counter += 1
        n = n//p
    return counter

def divisors_sum(n):
    prime_div = find_prime_divisors(n)
    total = 1
    for p,a in prime_div:
        total *= (p**(a+1)-1)//(p-1)
    return total - n

ints = {}

for i in range(2,10000):
    ints[i] = divisors_sum(i)

total = 0
for i in range(3,10000):
    for j in range(2,i):
        if ints[i] == j and ints[j] == i: total+= (i+j)




if __name__ == '__main__':
    print(ints)
    print(total)
