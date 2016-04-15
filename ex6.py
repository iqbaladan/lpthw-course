# Put a string into 'x' 
x = "There are %d types of people." % 10

binary = "binary" # Binary 
do_not = "don't" # Don't

# Put a string into 'y'
y = "Those who know %s and those who %s." % (binary, do_not)

print x # Printing variable 'x'
print y # Printing variable 'y'

print "I said: %r." % x # String inside string
print "I also said: '%s'." % y # # String inside string

hilarious = False # Boolean
joke_evaluation = "Isn't this joke so funny?! %r" # String

# Another string inside string
print joke_evaluation % hilarious

# Assigning string into 'w'
w = "This is the left side of ..."
# Assigning another string into 'e'
e = "a string with a right side."

# Printing w and e together by adding each strings.
print w + e
