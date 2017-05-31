letters_vals = {chr(i): i-ord('A')+1 for i in range(ord('A'), ord('Z')+1)}

S = open('p042_words.txt').read()
S = S.split(',')
S = [s[1:-1] for s in S]
N = len(max(S, key=len))
max_n = 1
while (max_n*max_n-max_n)//2 < N*letters_vals['Z']: max_n+=1
memo = {(n*n-n)//2 for n in range(1,max_n)}
num_triangles = 0
for word in S:
    score = 0
    for letter in word:
        score += letters_vals[letter]
    if score in memo: num_triangles += 1
print(num_triangles)