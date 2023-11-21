x, y, z = map(int, input().split())

if (z >= x >= y) or (y >= x >= z):
    print(x)
elif (x >= y >= z) or (z >= y >= x):
    print(y)
else:
    print(z)