while 1:
    width, length, x = input().split()
    width = int(width)
    length = int(length)

    print(width * length)

    if x == 'C':
        break