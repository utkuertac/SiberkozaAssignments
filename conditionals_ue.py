# If/ Else conditions are used to decide to do something based on something being true or false

x_ue = 10
y_ue = 50

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x_ue > y_ue:
  print(f'{x_ue} is greather than {y_ue}')

# If/ Else conditions 
if x_ue > y_ue:
  print(f'{x_ue} is greather than {y_ue}')
else:
  print(f'{y_ue} is greather than {x_ue}')

# elif
if x_ue > y_ue:
  print(f'{x_ue} is greather than {y_ue}')
elif x_ue == y_ue:
  print(f'{x_ue} is equal to {y_ue}')
else:
  print(f'{y_ue} is greather than {x_ue}')

# Nested if
if  x_ue > 2:
  if  x_ue <= 10:
    print(f'{x_ue} is greather than 2 and less than or equal to 10')

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if  x_ue > 2 and x_ue <= 10:
     print(f'{x_ue} is greather than 2 and less than or equal to 10')
# or
if  x_ue > 2 or ue <= 10:
     print(f'{x_ue} is greather than 2 or less than or equal to 10')

# not
if not(x_ue == y_ue):
  print(f'{x_ue} is not equal to {y_ue}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

# in
if x_ue in numbers_ue:
  print(x_ue in numbers_ue)

# not in 
if x_ue not in numbers_ue:
  print(x_ue not in numbers_ue)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is 
if x_ue is y_ue:
  print(x_ue is y_ue)

# is not 
if x_ue is not y_ue:
  print(x_ue is not y_ue)
  
