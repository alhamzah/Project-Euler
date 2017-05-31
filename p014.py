def longest_collatz(M):
    memo = {1:1}
    def helper(n):
        if n in memo: return memo[n]

        if n % 2 == 0:
            helper(n//2)
            memo[n] = (1 + helper(n//2))
        else:
            helper(3*n+1)
            memo[n] = (1 + helper(3*n+1))

    for n in range(1, M): helper(n)

    max_val = max(memo.values())
    for i in memo:
        if memo[i] == max_val: return i

print(longest_collatz(10**6))