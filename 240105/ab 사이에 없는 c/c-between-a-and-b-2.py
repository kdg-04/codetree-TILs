a, b, c = map(int, input().split())

has_multiple = False

for i in range(a, b + 1):
    if i % c == 0:
        has_multiple = True
        break

if has_multiple:
    print("NO")
else:
    print("YES")