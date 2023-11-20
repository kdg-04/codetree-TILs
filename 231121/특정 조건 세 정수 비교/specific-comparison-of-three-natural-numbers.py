x, y, z = map(int, input().split(" "))

if x <= y and x <= z:
    print("1", end=" ")
else:
    print("0", end=" ")

if x == y == z:
    print("1")
else:
    print("0")