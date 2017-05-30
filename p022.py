lettter_vals = {chr(i): i-ord('A')+1 for i in range(ord('A'), ord('Z')+1)}
def name_scores(S):
    total = 0
    for i in range(len(S)):
        name = S[i]
        for l in name:
            total += (i+1)*lettter_vals[l]
    return total

if __name__ == '__main__':
    import time
    start = time.time()
    S = open('p022_names.txt').read()
    S = S.split(',')
    S = [name[1:-1] for name in S]
    S.sort()
    print(name_scores(S))
    print(time.time()-start)
