x, y = map(int, input().split())
sum_val = 0

for i in range(x, y + 1):
    if i % 2 == 0:
        sum_val += i

print(sum_val)