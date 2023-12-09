cnt = 0

while cnt != 3:
    n = int(input())

    if n % 2 != 0:
        continue
    else:
        cnt += 1
        print(n // 2)