n = int(input())
cnt = 0

while 1:
    if n == 1:
        break
    cnt += 1
    n = n // 2

print(cnt)