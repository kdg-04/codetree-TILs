x, y, z = map(int, input().split(" "))
min = x

if min > y:
    min = y
elif min > z:
    min = z

print(min)