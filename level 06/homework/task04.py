# პირველი გამოსახულება

print(True or False and False or True and False or False and False or False and True and False or True)



# ოპერატორების დამუსშავება

# ვამუშავებთ მხოლოდ and-ებს:

False and False        - False  
True and False         - False  
False and False        - False  
False and True         - False  
True and False         - False  

# შესაბამისად ვიღებთ შემდეგს:
print(True or False or False or False or False or False or True)
 

 # OR ოპერატორების დამუშავება

 # True or False or False or False or False or False or True - True

# result - true



# მეორე გამოსახულება

print(5 > 10 or 7 * 7 / 7 == 7 and False or True and "1234" != "1234" and 7 + 3 * 3 + 1 == 15 and True and True or 100 > 100 or True)  



# დავამუშაოთ AND ოპერატორი 

# 1 - 7 * 7 / 7 == 7 → 49 / 7 == 7 → 7 == 7 → True

# 2 - True and False → False

# 3 - rue and "1234" != "1234" → "1234" != "1234" → False → True and False → False

# 4 - 7 + 3 * 3 + 1 → 7 + 9 + 1 = 17 → 17 == 15 → False

# 7 * 7 / 7 == 7 and False               -> False  
True and "1234" != "1234"             - False  
7 + 3 * 3 + 1 == 15 and True and True - False  


# განვიხილოთ AND ოპერატორები 

print(5 > 10 or False or False or 100 > 100 or True)



# დავამუშაოთ OR ოპერტორები 

False or False or False or False or True



# result - true

True
True
