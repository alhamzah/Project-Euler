pright = {23, 31, 37, 53, 73, 79}
pleft = {13, 17, 23, 37, 53, 73, 97}
pright_list = [list(pright)]
pleft_list = [list(pleft)]
global N
N = 10**5

def ESieve(limit):
    L = [True]*limit
    L[0]=L[1]=False
    for p, isprime in enumerate(L):
        if isprime:
            for i in range(p*p, limit, p): L[i] = False
    return [p for p, isprime in enumerate(L) if isprime ]

primes = ESieve(N)
global primes_set
primes_set = set(primes)

def new_length(direction):
    global N
    global primes_set
    if direction == 'r': p_list, p_set = pright_list, pright
    else: p_list, p_set = pleft_list, pleft
    if 10*p_list[-1][-1] > N:
        N*=10 
        primes = ESieve(N)
        primes_set = set(primes)

    new_p_list = []
    for p in p_list[-1]:
        for i in [1,3,7,9]:
            if direction == 'r': new_p = int(str(p)+str(i))
            else: new_p = int(str(i)+str(p))
            if new_p in primes_set: new_p_list.append(new_p)
    p_list.append(new_p_list)
    p_set |= set(new_p_list)

if __name__ == '__main__':
    import time
    start = time.time()
    while pright_list[-1] and pleft_list[-1] and len(pright.intersection(pleft)) < 11: 
        new_length('r')
        new_length('l')
    print(sum(pright.intersection(pleft)))
    print(time.time()-start)