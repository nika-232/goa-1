number = int(input("შეიყვანე რიცხვი: "))  # მომხმარებლისგან რიცხვის მიღება

# პირობის შემოწმება:
# ლუწია → number % 2 == 0
# და 10-ზე მეტია → number > 10
# ან ტოლია 7-ის → number == 7

if (number % 2 == 0 and number > 10) or number == 7:
    print(True)
