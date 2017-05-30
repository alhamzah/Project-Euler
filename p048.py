import time
start = time.time()
if __name__ == '__main__':
    total = 0
    for i in range(1,1000):
        total += i**i
    print(str(total)[-10:])
    print(1000*(time.time()-start))

