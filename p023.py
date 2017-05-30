
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

def find_prime_divisors(n):
    while n > primes[-1]: find_next_prime()
    divisors = []
    for p in primes:
        if p > n: break
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

abundant_nums = set()
abu_list = list()
for n in range(12,21823):
    if divisors_sum(n) > n: 
        abundant_nums.add(n)
        abu_list.append(n)

total = 0
s = set()
for i in range(len(abu_list)):
    for j in range(i+1):
        s.add(abu_list[i]+abu_list[j])

for n in range(1,21823):
    if n not in s: total += n


if __name__ == '__main__':
    print(total)

