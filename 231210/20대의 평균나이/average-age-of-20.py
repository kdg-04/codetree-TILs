cnt = 0
total_age = 0

while True:
    age = int(input())

    if age >= 30:
        break

    cnt += 1
    total_age += age

if cnt > 0:
    average_age = total_age / cnt
    print("%.2f" % average_age)