n = int(input())

if 12 == n or n == 1:
    print("31")
elif 3 <= n <= 7:
    if n % 2 == 0:
        print("30")
    else:
        print("31")
elif  8 <= n <= 11:
    if n % 2 == 0:
        print("31")
    else:
        print("30")
else:
    print("28")