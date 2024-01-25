Drainage = True
cnt = 0

for i in range(5):
    if i % 3 == 0:
        cnt += 1
    if cnt == 5:
        Drainage = False

if Drainage == True:
    print("1")
else:
    print("0")