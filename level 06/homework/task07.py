# მომხმარებლის მიერ შეყვანილი წელი
year = int(input("შეიყვანე წელი: "))


# იყოფა 4-ზე და არ იყოფა 100-ზე, ან იყოფა 400-ზე
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is leap year")
else:
    print("This is not a leap year")
