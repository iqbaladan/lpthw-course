# This is more practice on "Learn Python The Hardway" by Zed Shaw
print "Let's practice everything"
print 'You\'d need to know \'bout escapes with \\ that do\n newlines and \t tabs

# """ is multiline comments and than it stores to 'poem' as variabels
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "------------------------------"
print poem
print "------------------------------"

# This part, we practice about format charactes
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# Here is a function called secret_formula with one argument
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
    
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "Whith a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

start_point = start_point / 10

print "We can aslo do that this way:"
print "We'd have %d beans, %d jars, and %d crates" % secret_formula(start_point)
