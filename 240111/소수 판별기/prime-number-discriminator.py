n = int(input())

for i in range(2, n):
    if n % i == 0:
        prime_number = False
        
if prime_number == False:
    print("C")
else:
    print("P")