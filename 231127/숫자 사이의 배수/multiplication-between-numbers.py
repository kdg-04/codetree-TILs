x, y = map(int, input().split())
sum_val = 0
cnt = 0

for i in range(x, y+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
    cnt += 1

avg = sum_val / cnt
print("%d %.1f" % (sum_val, avg))