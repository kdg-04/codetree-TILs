n = int(input())

for i in range(1, n + 1):
    x = i // 8  
    y = i % 7
    if i % 2 == 0 and i % 4 != 0:
        continue
    if x % 2 == 0:
        continue
    if y < 4:
        continue
    print(i, end=" ")