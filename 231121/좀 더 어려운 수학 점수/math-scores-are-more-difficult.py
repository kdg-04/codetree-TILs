ams, aes = map(int, input().split())
bms, bes = map(int, input().split())

if ams > bms or (ams == bms and aes > bes):
    print("A")
else:
    print("B")