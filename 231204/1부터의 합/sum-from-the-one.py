n = int(input())
x = 0

for i in range(1, 101):
    x += i
    if x > n:
        break

print(i)