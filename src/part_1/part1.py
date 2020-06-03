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