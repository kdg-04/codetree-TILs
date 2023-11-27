tcnt = 0
fcnt = 0

for i in range(1, 11):
    n = int(input())
    if n % 3 == 0:
        tcnt += 1
    if n % 5 == 0:
        fcnt += 1

print("%d %d" % (tcnt, fcnt))