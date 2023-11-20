x, y, z = map(int, input().split(" "))
min = x

if min > y:
    min = y
if min > z:
    min = z

print(min)