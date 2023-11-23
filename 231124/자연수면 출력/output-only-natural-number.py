x, y = map(int, input().split())

if x > 0:
    for i in range(y):
        print(x, end="")
elif x <= 0:
    print(0)