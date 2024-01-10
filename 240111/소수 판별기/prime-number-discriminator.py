n = int(input())

for i in range(1, n):
    if n % i == 0:
        prime_number = 0
    else:
        prime_number = 1
if prime_number == 1:
    print("P")
else:
    print("C")