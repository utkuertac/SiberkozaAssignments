# A List is a collection which is ordered and changeable. Allows duplicate members.
# Create list
numbers_ue = [1, 2, 3, 4, 5]
fruits_ue = ['Apples', 'Oranges', 'Grapes', 'Pears']
             
# Use a constructor
numbers2_ue = list((1, 2, 3, 4, 5))

print(numbers_ue, numbers2_ue)

# Get a value
print(fruits_ue[1])

# Get length
print(len(fruits_ue))

# Append to list
fruits_ue.append('Mangos')

print(fruits_ue)

# Remove from list
fruits_ue.remove('Grapes')

print(fruits_ue)

# Insert into position
fruits_ue.insert(2, 'Strawberries')

print(fruits_ue)

# Remove with pop
fruits_ue.pop(2)

print(fruits_ue)

# Reverse list
fruits_ue.reverse()

print(fruits_ue)

# Sort list 
fruits_ue.sort()

print(fruits_ue)

# Reverse sort
fruits_ue.sort(reverse=True)

print(fruits_ue)

# Change value
fruits_ue[0] = 'Blueberries'

print(fruits_ue)
