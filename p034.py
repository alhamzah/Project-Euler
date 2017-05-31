def factorial(n):
    if n == 0: return 1
    return n*factorial(n-1)

f_dict = {i: factorial(i) for i in range(10)}

num_sum = 0
for n in range(3,10**5):
    f_sum, s = 0, str(n)
    for i in s: f_sum += f_dict[int(i)]
    if f_sum == n: num_sum += n

print(num_sum)