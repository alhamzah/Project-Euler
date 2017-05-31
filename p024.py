
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

n = build_perms_enefficiant()[10**6-1]
n = [str(i) for i in n]
N = ''.join(n)
print(N)