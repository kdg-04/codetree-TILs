x, y = map(int, input().split())
sum_val = 0

for i in range(x, y + 1):
    if i % 6 == 0 and i % 8 != 0:
        sum_val += i

print(sum_val)