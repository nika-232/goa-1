

sist = int(input("სისტოლური წნევა >>> "))
diast = int(input("დიასტოლური წნევა >>> "))


if diast > 140 or diast > 90:
    print("მაღალი წნევა!!!")
elif sist < 90 or diast < 60:
    print("დაბალი წნევა!!!")


