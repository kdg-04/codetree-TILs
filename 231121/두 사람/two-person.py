age_1, sex_1 = input().split()
age_1 = int(age_1)
age_2, sex_2 = input().split()
age_2 = int(age_2)

if (age_1 >= 19 or age_2 >= 19) and (sex_1 == "M" or sex_2 == "M"):
    print("1")
else:
    print("0")