import long_int

S = long_int.S
S = S.split('\n')
for i in range(len(S)):
    S[i] = int(S[i])

large_sum = str(sum(S))



if __name__ == "__main__":
    print(int(large_sum[:10]))