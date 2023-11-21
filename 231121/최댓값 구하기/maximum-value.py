x, y, z = map(int, input().split())
max = x

if max <= y:
    if max <= z:
        max = z
    else:
        max = y

print(max)