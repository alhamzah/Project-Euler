def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

if __name__ == '__main__':
    s = list(str(factorial(100)))
    for i in range(len(s)): s[i] = int(s[i])
    print(sum(s))