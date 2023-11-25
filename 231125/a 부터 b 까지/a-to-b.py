x, y = map(int, input().split())

while y >= x:
    print(x, end=" ")
    if x % 2 != 0:
        x *= 2
    else:
        x += 3