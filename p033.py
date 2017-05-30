def check_curious():
    curious = set()
    for p in range(10,100):
        if p%10==0: continue
        for q in range(10, 100):
            if q%10==0: continue
            for pair in f_list(str(p),str(q)):
                if int(pair[0])/int(pair[1]) == p/q and p < q: curious.add((p,q))
    return curious

def f_list(p,q):
    f = []
    if p[0] == q[0]: f.append((p[1]+q[1]))
    if p[0] == q[1]: f.append((p[1], q[0]))
    if p[1] == q[0]: f.append((p[0], q[1]))
    if p[1] == q[1]: f.append((p[0], q[0]))
    return f

if __name__ == '__main__':
    print(check_curious())
