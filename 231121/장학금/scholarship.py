mts, fts = map(int, input().split())

if mts >= 90:
    if fts >= 95:
        print("100000")
    elif fts >= 90:
        print("50000")
    else:
        print("0")
else:
    print("0")