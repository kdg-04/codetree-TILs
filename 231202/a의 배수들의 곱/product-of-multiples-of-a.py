x, y = map(int, input().split())
prod = 1

for i in range(1, y + 1):
    if i % x == 0:
        prod *= i
    
print(prod)