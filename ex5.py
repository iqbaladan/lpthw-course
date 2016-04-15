## More Variable and Printing

name = 'Iqbal Adan'
age = 29 # not a lie
height = 180 # metres
weight = 85 # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %r." % name
print "He's %r inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffe." % teeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %r." % (
    age, height, weight, age + height + weight)

