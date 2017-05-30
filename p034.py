def factorial(n):
    if n == 0: return 1
    return n*factorial(n-1)

f_dict = {i: factorial(i) for i in range(10)}

num_sum = 0

for n in range(3,10**7):
    s = str(n)
    f_sum = 0
    for i in s:
        f_sum += f_dict[int(i)]
    if f_sum == n: num_sum += n




if __name__ == '__main__':
    s =factorial(9)
    k = 1
    while 10**k < s*k:
        k += 1
    print(num_sum)


