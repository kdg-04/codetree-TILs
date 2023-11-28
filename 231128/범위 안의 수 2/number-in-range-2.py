sum_val = 0
avg_val = 0
cnt = 0

for _ in range(1, 11):
    n = int(input())
    if 200 >= n >= 0:
        sum_val += n
        cnt += 1

avg_val = sum_val / cnt
print("%d %.1f" % (sum_val, avg_val))