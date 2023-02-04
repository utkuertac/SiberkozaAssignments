# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits_ue = ('Apples', 'Oranges', 'Grapes')
# fruits2_ue = tumple(('Apples', 'Oranges', 'Grapes')) 
fruits2_ue = ('Apples',)

print(fruits2_ue, type(fruits2_ue))

# Get value

print(fruits_ue[1])

# Can't change value

fruits_ue[0] = 'Pears'

# Delete tuple
del fruits2_ue 

print(fruits2_ue) 

# Get lenght
print(len(fruits_ue)

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set_ue = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set_ue)

# Add duplicate
fruits_set_ue.add('Grape')
 
print(fruits_set_ue

# Remove from set
fruits_set_ue.remove('Grape')     

print(fruits_set_ue)

# Clear set      
fruits_set_ue.clear()     
      
print(fruits_set_ue)      

# Delete
del fruits_set_ue
      
print(fruits_set_ue)    
