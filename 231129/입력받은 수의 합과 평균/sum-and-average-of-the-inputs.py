n = int(input())
sum_val = 0
avg = 0
cnt = 0

for i in range(1, n + 1):
    m = int(input())
    sum_val += m
    cnt += 1

avg = sum_val / cnt

print("%d %.1f" % (sum_val, avg))