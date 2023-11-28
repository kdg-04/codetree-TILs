x, y = map(int, input().split())
sum_val = 0

if x > y:
    temp = y
    y = x
    x = temp


for i in range(x, y + 1):
    if i % 5 == 0:
        sum_val += i

print(sum_val)