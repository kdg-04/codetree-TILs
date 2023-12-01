x, y = map(int, input().split())
prod = 1

for _ in range(y):
    prod *= x

print(prod)