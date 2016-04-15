# Importing modules from sys
from sys import argv

# Unpacking the arguments
script, filename = argv

# Assigning an open function into 'txt'
txt = open(filename)

# Printing the filename
print "Here's your file %r:" % filename

# Printing filename from open function
print txt.read()

# Printing filename again
print "Type the filename again:"

# Prompting filename again and assign it to 'file_again'
file_again = raw_input("> ")

# Open 'file_again' and assign it to 'txt_again'
txt_again = open(file_again)

# Printing 'txt_again.read()'
print txt_again.read()
