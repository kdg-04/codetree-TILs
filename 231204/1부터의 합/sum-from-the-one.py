n = int(input())
prod = 0
ans = -1

for i in range(1, 101):
    prod += i
    if prod > n:
        ans = i
        break

print(i)