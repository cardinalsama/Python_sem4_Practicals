# a. Write a Python program to create a tuple with different data types
person = ("Mitren", 19, 'Student', 92.03)
print(person)

# b. Write a Python program to create a tuple with numbers and print one item
number_tuple = (1,2,3,4,5,6,7,8,9,10)
print(number_tuple)
print(number_tuple[5])

# c. Write a Python program to add an item in a tuple
number_tuple = number_tuple + (11,)
print(number_tuple)

# d. Writew a Python program to convert a tuple to a string
def toString(tuple) :
    # intializing an empty string
    str = ''
    for item in tuple:
        str += item
    return str

strtuple = ('H', 'e', 'l', 'l' ,'o')
print(strtuple)
print(toString(strtuple))

# e. Write a Python program to find the length of a tuple
print(len(strtuple))