file = open("p067_triangle.txt")
T=file.read()

T = T.split('\n')
for r in range(len(T)):
    T[r] = T[r].split(' ')

T = T[:-1]
for r in range(len(T)):
    for c in range(len(T[r])):
        T[r][c] = int(T[r][c])

parent = {(0,0): 0}

def bfs():
    for r in range(len(T)):
        for c in range(len(T[r])):
            score = parent[(r,c)]+T[r][c]
            if (r+1, c) not in parent or parent[(r+1,c)] < score: parent[(r+1,c)] = score
            if (r+1, c+1) not in parent or parent[(r+1,c+1)] < score: parent[(r+1,c+1)] = score

if __name__ == '__main__':
    bfs()
    print(max(parent.values()))
