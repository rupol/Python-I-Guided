# define a doubling function that passes args by value
# def keyword
def double(x):
    return x * 2
# x is passed by value (the value of that variable is essentially copied, temporary value is created in memory...loosely)

# directly invoke and print
print(double(21))

# or can use in a variable
y = double(12)
print(y)

# define a doubling function for a list of variables
def double_list(l):
    for i in range(len(l)): # this line is a keeper, standard for iterating lists
        l[i] *= 2
# l is passed by reference (list is directly modified)
# l is a pointer to a list
# don't need to return because it is directly modified

some_nums = [1, 2, 3, 4]
print(some_nums)
double_list(some_nums)
print(some_nums)

