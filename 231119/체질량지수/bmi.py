m, kg = map(int, input().split(" "))
m /= 100
bmi = int(kg // (m ** 2))

print(bmi)
if bmi >= 25:
    print("Obesity")