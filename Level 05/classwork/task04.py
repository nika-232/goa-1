letter = input("შეიყვანე შეფასების ასო (A, B, C, D ან F): ")

if letter.upper() == "A":
    print(100)
elif letter.upper() == "B":
    print(80)
elif letter.upper() == "C":
    print(60)
elif letter.upper() == "D":
    print(40)
elif letter.upper() == "F":
    print("Failed!")
else:
    print("არასწორი შეფასებაა შეყვანილი.")
