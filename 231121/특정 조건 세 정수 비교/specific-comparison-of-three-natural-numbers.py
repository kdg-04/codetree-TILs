x, y, z = map(int, input().split(" "))
min = x

if min > y:
    min = y
if min > z:
    min = z

if min == x:
    print("1", end=" ")
else:
    print("0", end=" ")

if x == y == z:
    print("1")
else:
    print("0")