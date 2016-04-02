# Lesson 2.6: Structured Data - Lists

# Similar to how strings are seuqences of characters, lists are
# sequences of anything! We can have lists of numbers, lists of
# characters, even lists of lists! And we can mix up the contents
# too so we can have lists containing many different things.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4180729266/m-48652460

p = ['y', 'a', 'b', 'b', 'a', '!']
print (p)
print (p[0])
print (p[2:4])

# Add your own code and notes here

# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

#['Moe','Larry','Shemp']

# but does not create a new List
# object.

stooges[2] = 'Shemp'
print (stooges)

# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0,0,7]

def replace_spy(spy):
    spy[2] = spy[2] + 1
    return spy

# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.

replace_spy(spy)
print (spy)
#>>> [0,0,8]


# Lesson 2.6: For Loops

# For loops, like while loops, are useful for running a block of code
# multiple times. For loops make iterating through elements in a list
# easier than using a while loop.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4152219158/m-48204891

def print_all_elements(p):
    for e in p:
        print (e)

myList = [1, 2, [3, 4]]
print_all_elements(myList)

# Add your own code and notes here

# Read through these examples and try to figure out what's going on.
# Press "Test Run" to see what they do.

print ("EXAMPLE 1: We can use for loops to go through a list of strings")
example_list_1 = ['a', 'b', 'c', 'd']
for thing in example_list_1:
    print (thing)
    

print ("EXAMPLE 2: We can use for loops on nested lists too!")
example_list_2 = [['China', 'Beijing'],
                  ['USA'  , 'Washington D.C.'],
                  ['India', 'Delhi']]
for country_with_capital in example_list_2:
    country = country_with_capital[0]
    capital = country_with_capital[1]
    print (capital + ' is the capital of ' + country)


# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

def sum_list(list):
    n = 0
    for i in list:
        n = n + i
    return n


print (sum_list([1, 7, 4, 5]))
#>>> 12

print (sum_list([9, 4, 10]))
#>>> 23

print (sum_list([44, 14, 76]))
#>>> 134

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(p):
    i = 0
    for e in p:
        if e[0] == 'U':
            i = i + 1
    return i

print (measure_udacity(['Dave','Sebastian','Katy']))
#>>> 0

print (measure_udacity(['Umika','Umberto']))
#>>> 2

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(list,value):
    n = 0
    for e in list:        
        if e == value:
            return n
        n = n+1
    return -1



print (find_element([1,2,3],3))
#>>> 2

print (find_element(['alpha','beta'],'gamma'))
#>>> -1

#<list>.index(<value>) do the same thing and is a built-in function
#if <value> is in the <list>, returns first position where <value> is found in <list>.
#Otherwise, produces an error

# <value> in <list>
# if <value> is in the <list>, output is True.
# Otherwise, outpu is False

# <value> not in <list> is the inverse of the first one

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(list, value):
    if value in list:
        return list.index(value)
    else:
    	return -1


print (find_element([1,2,3],3))
#>>> 2

print (find_element(['alpha','beta'],'gamma'))
#>>> -1