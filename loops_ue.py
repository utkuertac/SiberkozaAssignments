# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_ue = ['Utku', 'Paul', 'Sara', 'Susan']

# Simple for loop
 for person_ue in people_ue:
   print(f'Current Person: {person_ue}')
  
# Break
 for person_ue in people_ue:
    if person_ue == 'Sara':
      break
   print(f'Current Person: {person_ue}')
  
# Continue
 for person_ue in people_ue:
    if person_ue == 'Sara':
      continue
   print(f'Current Person: {person_ue}')
  
# range
for i_ue in range(len(people_ue)):
  print(people_ue[i_ue])
  
for i_ue range(0, 11):
  print(f'Number: {i_ue}')


# While loops execute a set of statements as long as a condition is true.

count_ue = 0
while count_ue <= 10:
  print(f'Count: {count_ue}')
  count_ue += 1
