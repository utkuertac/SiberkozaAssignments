# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person_ue = {
  'first_name_ue': 'Utku',
  'lats_name_ue': 'Ertaç',
  'age_ue': 22
}

print(person_ue, type(person_ue))

# Use constructor
person2_ue = dict(first_name_ue='Sara', last_name_ue='Williams')

print(person2_ue, type(person2_ue))

# Get value
print(person_ue['first_name_ue'])
print(person_ue.get('last_name_ue'))

# Add key/value
person_ue['phone_ue'] = '555-555-5555'

print(person_ue)

# Get dict keys
print(person_ue.keys())

# Get dict items
print(person_ue.items())

# Copy dict
person2_ue = person_ue.copy()
person2_ue['city'] = 'Ankara'

print(person2_ue)

# Remove item
del(person_ue['age_ue'])
person_ue.pop('phone_ue')

print(person_ue)

# Clear 
person_ue.clear()

print(person_ue)

# Get length
print(len(person2_ue))

# List of dict
people_ue = [
    {'name_ue': 'Martha', 'age_ue': 30},
    {'name_ue': 'Kevin', 'age_ue': 25}
]

print(people_ue[1]['name_ue'])
