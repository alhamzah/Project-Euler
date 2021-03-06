def find_digits_of_power(n):
    num = [1]
    def helper(num):
        new_numb = [0]*(len(num)+1)
        for i in range(len(num)):
            current = 2*num[i]+new_numb[i]
            first_dig = (current % 10)
            new_numb[i] = first_dig
            if current > 9: new_numb[i+1] = (current-first_dig)//10
        if not new_numb[-1]: new_numb.pop()
        return new_numb
    for i in range(n): num = helper(num)
    num.reverse()
    return num

print(sum(find_digits_of_power(1000)))