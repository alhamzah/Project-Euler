import p013_long_int

S = long_int.S
S = S.split('\n')
for i in range(len(S)):
    S[i] = int(S[i])

large_sum = str(sum(S))

print(int(large_sum[:10]))