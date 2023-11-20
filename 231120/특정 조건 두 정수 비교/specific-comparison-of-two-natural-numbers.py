x, y = map(int, input().split(" "))

if y > x:
    print("1", end=" ")
else:
    print("0", end=" ")

if x == y:
    print("1")
else:
    print("0")