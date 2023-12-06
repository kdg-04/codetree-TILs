n = int(input())
cnt = 0

for i in range(1, n+1):
    n /= i
    print(n, i)
    if n > 1:
        cnt += 1
        continue
    else:
        break

print(cnt)