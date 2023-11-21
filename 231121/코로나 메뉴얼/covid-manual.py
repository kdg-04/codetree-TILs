sym1, temp1 = input().split()
temp1 = int(temp1)
sym2, temp2 = input().split()
temp2 = int(temp2)
sym3, temp3 = input().split()
temp3 = int(temp3)
cnt = 0

if sym1 == "Y":
    if temp1 >= 37:
        cnt += 1
if sym2 == "Y":
    if temp2 >= 37:
        cnt += 1
if sym3 == "Y":
    if temp3 >= 37:
        cnt += 1

if cnt >= 2:
    print("E")
else:
    print("N")