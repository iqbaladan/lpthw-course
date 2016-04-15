#
# Another example of raw_input()
#

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

# Printing the input from user based on format characters
print "So you are %r old, %r tall and %r heavy." % (
    age, height, weight)
