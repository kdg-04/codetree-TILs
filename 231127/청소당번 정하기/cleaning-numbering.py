clcnt = 0
flcnt = 0
recnt = 0

n = int(input())

for i in range(1, n+1):
    if i % 12 == 0:
        recnt += 1
    elif i % 3 == 0:
        flcnt += 1
    elif i % 2 == 0:
        clcnt += 1

print("%d %d %d" % (clcnt, flcnt, recnt))