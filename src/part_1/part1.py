# print hello world
print('Hello World')

# declare a variable
name = 'Ruth'

# print a variable
print(name)

# string concatenation
print('Hello ' + name)
# format strings
print(f'Hello {name}')

#### data structures ####

## Lists (like arrays in JS)
p = [10, 60, 20, 51, "Banana"]
print(p)

# add an element to the end of p
p.append('Pear')
print(p)

# loop over the list p, and print every element
# colon indicates we're starting a code block, like curlies in JS
for element in p:
    print(element)
    print("oops I printed again") # without the indent, it no longer belongs to the block

# print the index and element at the index of p
for (index, element) in enumerate(p):
    print(f'Element at {index} is {p[index]} == {element}')
    # enumerage goes through the list and returns a tuple => [(0, 10), (1, 60), (2, 20)...]

# List comprehensions
# another way to create a list
numbers = [1, 4, 9, 16, 25]
# create a new list of squares from the numbers list
# non fancy way...
squares = []
for num in numbers:
    squares.append(num*num)
print(squares)

# lets use List Comprehensions
# for each element from numbers, multiply by itself, then add to cooler_squares
fancy_squares = [ num*num for num in numbers ]
print(fancy_squares)

# lets create a list of just even numbers
evens = [num for num in numbers if num % 2 == 0]
# no triple equals in python!
print(evens)

# create a new list containing only names that start with s
names = ["Sarah", "jorge", "sam", "Frank", "bob", "sandy", "shawn"]
s_names = [name for name in names if name[0].lower() == "s"]
# can treat each name like a list and reference a given position
print(s_names)
# also, capitalize all names
s_names_capitalized = [name.capitalize() for name in names if name[0].lower() == "s"]
print(s_names_capitalized)


## Dictionaries
# otherwise known as maps/hashmaps/objects
# a key => value data structure
new_dict = {}

# create a dictionary with some keys and values
food_dict = {
    'apple': 'is a fruit',
    'carrot': 'is a vegetable'
}

# let's add a new key value pair
food_dict['cucumber'] = 'is maybe a vegetable?'
print(food_dict)

# access and print a specific element in food_dict
chosen_food = 'apple'
# food_dict.apple is not allowed in python (only JS)
print(food_dict[chosen_food])

# iterate through the keys and values of a dictionary
# for element in dict, do some code
for key, value in food_dict.items():
    print(f'{key}: {value}')

# how can we check if an element exists in a dictionary
# is apple in food_dict?
print('apple' in food_dict) # returns true
print('banana' in food_dict) # returns false

### Tuples and Sets ###

## tuples
# not iterable
tup = (1,2,3,4)
for item in tup:
    print(item)

# access a particular element
print(tup[1])

## sets
# basically dictionaries without values
fruit = {'cucumber', 'apple', 'banana'}

for item in fruit:
    print(item)

if 'cucumber' in fruit:
    print("I don't THINK so, ma'am")
