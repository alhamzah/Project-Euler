ints = set()
for a in range(2, 100+1):
    for b in range(2, 100+1):
        ints.add(a**b)

print(len(ints))