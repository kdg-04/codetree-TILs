x, y, z = map(int, input().split(" "))
arr = [x, y, z]
print(sum(arr))
print("%.0f" % (sum(arr) / len(arr)))