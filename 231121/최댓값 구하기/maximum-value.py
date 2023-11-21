x, y, z = map(int, input().split())

if x >= y:
    if x >= z:
        print(x)
    else:
        print(z)
elif y >= x:
    if y >= z:
        print(y)
    else:
        print(z)