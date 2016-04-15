from sys import argv

script, input_file = argv

# Function called print_all
def print_all(f):
    print f.read()

# Function called rewind
def rewind(f):
    f.seek(0)

# Function called print_a_line
def print_a_line(line_count, f):
    print line_count, f.readline()

# Open input_file and assign it to current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Lets's print three lines"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
