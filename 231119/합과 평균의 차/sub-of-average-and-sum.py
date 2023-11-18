x, y, z = map(int, input().split(" "))
arr = [x, y, z]
avg = sum(arr) / len(arr)

print(sum(arr))
print("%d" % (avg))
print("%d" % (sum(arr) - avg))