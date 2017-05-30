
#BAD runntime
import time
start = time.time()
NUMS = [i for i in range(10)]
all_perms = []

def build_perms_enefficiant(num_list=NUMS):
    l = len(num_list)
    if not l: return [[]]
    perms = []
    for i in range(l):
        nums = num_list[:]
        perm = [nums.pop(i)]
        for p in build_perms_enefficiant(nums):
            if len(perms) == 10**6: break
            perms.append(perm+p)
        if len(perms) == 10**6: break
    return perms

# memo = {0:1}
# def factorial(n):
#     if n not in memo: memo[n] = n*factorial(n-1)
#     return memo[n]

# def build_perms(num_list=NUMS, N=10**6):
#     result = []
#     while N:
#         rank = factorial(len(num_list))
#         if rank > N:
#             result.append(num_list[0])
#             num_list = num_list[1:]
#             N -= rank


if __name__=='__main__':
    n = build_perms_enefficiant()[10**6-1]
    n = [str(i) for i in n]
    N = ''.join(n)
    print(N)
    print(time.time()-start)