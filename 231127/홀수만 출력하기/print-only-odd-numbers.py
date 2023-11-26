n = int(input())

for i in range(1, n+1):
    m = int(input())
    if m % 2 != 0 and m % 3 == 0:
        print(m)