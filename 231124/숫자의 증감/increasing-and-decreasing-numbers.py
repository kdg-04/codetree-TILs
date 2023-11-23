x, y = input().split()
y = int(y)

if x == 'A':
    for i in range(1, y+1):
        print(i, end=" ")
elif x == 'D':
    for i in range(y, -1):
        print(i, end=" ")