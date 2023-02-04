# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create function
def sayHello(name_ue):
  print(f'Hello {name_ue}')
  
  sayHello('Utku Ertaç')
  
  # Create function
def  sayHello(name_ue = 'Utku'):
  print(f'Hello {name_ue}')

sayHello()

# Return values
def getSum(num1_ue, num2_ue):
  total = num1_ue + num2_ue 
  return total
  
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

print(getSum(3, 4))

# Return values
def getSum(num1_ue, num2_ue):
  total = num1_ue + num2_ue 
  return total

num_ue = getSum(3, 4)

print(num_ue)

# Lambda function 

getSum = lambda num1_ue, num2_ue : num1_ue + num2_ue

print(getSum(10, 3))

