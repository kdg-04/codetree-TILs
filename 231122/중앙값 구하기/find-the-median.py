x, y, z = map(int, input().split())

if a > b:
    if c > a:
        # a > b, c > a 일때 (c > a > b)
        print(a)
    # a > b, a > c 일때 (a가 가장 크고, b와 c중 더 큰 수가 중앙값)
    elif b > c:
        print(b)
    else:
        print(c)
else:
    if c > b:
        # b > a, c > b 일때 (c > b > a)
        print(b)
    # b > a, b > c 일때 (b가 가장 크고, a와 c중 더 큰 수가 중앙값)
    elif a > c:
        print(a)
    else:
        print(c)