# სწორი პაროლი
correct_password = "nika123"

# მომხმარებლის მიერ შეყვანილი პაროლი
password = input("nika1234: ")

# სანამ შეყვანილი პაროლი არ ემთხვევა სწორ პაროლს
while password != correct_password:
    print("The password is incorrect. Please try again..")
    password = input("nika123: ")

# როცა პაროლი სწორია
print("The password is correct. Welcome!")
