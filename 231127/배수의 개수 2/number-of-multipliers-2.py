cnt = 0

for i in range(1, 11):
    n = int(input())
    if n % 2 != 0:
        cnt += 1

print(cnt)