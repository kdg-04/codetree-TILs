mts, fts = map(int, input().split())

if mts >= 90 and fts >= 95:
    print("100000")
elif mts >= 90 and fts >= 90:
    print("50000")
else:
    print("0")