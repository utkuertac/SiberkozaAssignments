# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
# Create class
class User_ue:
  # Constructor
  def __init__(self_ue, name_ue, email_ue, age_ue):
    self_ue.name = name_ue
    self_ue.email = email_ue
    self_ue.age = age_ue
    
  def greeting_ue(self_ue):
    return f'My name is {self_ue.name} and I am {self_ue.age}'
  
  def has_birthday_ds(self_ue):
    self_ue.age += 1
    
    
# Extend class
class Customer(User_ue):
  
 def __init__(self_ue, name_ue, email_ue, age_ue):
    self_ue.name = name_ue
    self_ue.email = email_ue
    self_ue.age = age_ue
    self_ue.balance = 0
    
 def set_balance(self_ue, balance_ue):
    self_ue.balance = balance_ue
    
 def greeting_ds(self_ue):
    return f'My name is {self_ue.name} and I am {self_ue.age} and my balance is {self_ue.balance}'
  
# Init user object
dilara = User_ds('Utku Ertaç', 'utkuertac@gmail.com', 22)

#print(type(utku))

print(utku.name)

print(utku.age)

print(utku.email)

print(utku.has_birthday_ds())

utku.greeting()

# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com' 25)

janet.set_balance(500)
print(janet.greeting())
