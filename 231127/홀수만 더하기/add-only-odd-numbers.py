n = int(input())
sum_val = 0

for i in range(1, n+1):
    m = int(input())
    if m % 2 == 1 and m % 3 == 0:
        sum_val += m

print(sum_val)