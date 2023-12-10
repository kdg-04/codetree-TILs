cnt = 0
total_age = 0

while 1:
    age = int(input())

    if age >= 30:
        break

    cnt += 1
    total_age += age

if cnt > 0:
    print("%.2f" % (total_age / cnt))