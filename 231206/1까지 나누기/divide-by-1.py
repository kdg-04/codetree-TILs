n = int(input())
cnt = 0

for i in range(1, n+1):
    val = n / i
    n = val
    
    if n <= 1:
        break

print(i)