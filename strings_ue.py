# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name_ue = 'Utku'
age_ue = 22

# Concatenate
print('Hello, my name is ' + name_ue+ ' and I am ' + str(age_ue))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name_ue, age=age_ue))

#F-Strings (3.6+)
print(f'Hello, my name is {name_ue} and I am {age_ue}')

# String Methods

s_ue = 'hello world'

# Capitalize string 
print(s_ue.capitalize())

# Make all uppercase
print(s_ue.upper())

# Make all lower
print(s_ue.lower())

# Swap case
print(s_ue.swapcase())

# Get length
print(len(s_ue))

# Replace
print(s_ue.replace('world', 'everyone'))

# Count
sub = 'h'
print(s_ue.count(sub))

# Starts with
print(s_ue.startswith('hello'))

# Ends with
print(s_ue.endswith('d'))

# Split into a list 
print(s_ue.split())

# Find position
print(s_ue.find('w'))

# Is all alphanumeric
print(s_ue.isalnum())

#Is all alphabetic
print(s_ue.isalpha())

# Is all numeric
print(s_ue.isnumeric())
