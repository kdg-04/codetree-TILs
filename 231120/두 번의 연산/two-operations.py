n = int(input())

if n % 2 != 0:
    n += 3

if n % 3 == 0:
    n /= 3

print(int(n))