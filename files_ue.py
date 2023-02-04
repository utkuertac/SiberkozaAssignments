# Python has functions for creating, reading, updating, and deleting files.

# Open a file

myFile_ue = open('myfile_ue.txt', 'w')

# Get some info
print('Name: ', myFile_ue.name)
print('Is Closed: ', myFile_ue.closed)
print('Opening Mode: ', myFile_ue.mode)

# Write to file
myFile_ue.write('I Love Python')
myFile_ue.write(' and Java')
myFile_ue.close()

# Append to file
myFile_ue = open('myfile_ue.txt', 'a')
myFile_ue.write(' I also like PHP')
myFile_ue.close()

# Read from file
myFile_ue = open('myfile_ds.txt', 'r+')
text_ue = myFile_ue.read(100)

print(text_ue)
