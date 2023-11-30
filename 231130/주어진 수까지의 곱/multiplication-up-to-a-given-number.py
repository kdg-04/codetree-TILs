x, y = map(int, input().split())
prod = 1

for i in range(x, y + 1):
    prod *= i

print(prod)