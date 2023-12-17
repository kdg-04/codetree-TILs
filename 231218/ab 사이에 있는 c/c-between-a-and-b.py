a, b, c = map(int, input().split())
check = 0

for i in range(a, b + 1):
    if i % c == 0:
        check = 1
        
if check == 1:
    print("YES")
else:
    print("NO")