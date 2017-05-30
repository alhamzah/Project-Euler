ints = set()
for a in range(2, 100+1):
    for b in range(2, 100+1):
        ints.add(a**b)

if __name__ == '__main__':
    print(len(ints))