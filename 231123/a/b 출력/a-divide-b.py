x, y = map(int, input().split())

print(f'{x//y}.', end="")

x %= y 

for _ in range(20):
    x *= 10
    print(x // y, end="")
    x %= y