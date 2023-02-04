# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x_ue = 3
y_ue = 7.5
name_ue = 'Utku'
is_cool_ue = True

x_ue, y_ue, name_ue, is_cool_ue = (3, 7.5, 'Utku', True)

a_ue= x_ue + y_ue

x_ue = str(x_ue)
y_ue = int(y_ue)
z_ue = float(y_ue)

print(type(x_ue))
print(type(y_ue), y_ue)
print(type(z_ue)) 
