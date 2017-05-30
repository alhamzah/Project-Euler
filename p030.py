memo = {i:i**4 for i in range(10)}
pairs_sum = set()

for i in range(10):
    for j in range(10):
        pairs_sum.add(memo[i]+memo[j])

power_sum = list()
for i in range(10, 10**5):
    num = str(i)
    if int(num[0])+int(num[1]) in 
