ams, aes = map(int, input().split())
bms, bes = map(int, input().split())

if ams > bms:
    print("A")
elif ams == bms and aes > bes:
    print("A")
else:
    print("B")