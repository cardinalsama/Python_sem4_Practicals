
# a. Write a Python script to check whether a given key already exists in a dictionary.
def checkKeyIsPresent(dict, key):

    # If key is present then print its value
    if key in dict:
        print(key, " is present.")
        print("Value = ", dict[key])
    else:
        print(key, " is not present.")

# A dictionary about a person
person_A = {
    'first_name' : 'Mitren',
    'middle_name' : 'Vipulkumar',
    'last_name' : 'Kadiwala',
    'DOB' : '14/07/2002'
}
print(person_A)

checkKeyIsPresent(person_A, 'Birthdate')
checkKeyIsPresent(person_A, 'DOB')

# b. Write a python script to merge two python dictionaries.

def Merge(a, b):
    return a.update(b)

# A dictionary about a person A
A = {
    'a' : 1,
    'b' : 2
}
print(A)
# A dictionary about a person A
B = {
    'c' : 3,
    'd' : 4
}
print(B)
Merge(A,B)
print(A)

#c. Write a Python program to sum all the items in a dictionary.
Marks = {
     'PIP': 90,
     'DBMS': 95,
     'DSA': 92
}
print(sum(Marks.values()))

#d. Write a Python script to add a key to a dictionary.
dict = {0: 'A', 1: 'B'}
dict[2] = 'C'
print(dict)

#e. Write a Python script to concatenate following dictionaries to create a new one.
dicA = {1: "a", 2: 'b'}
dicB = {3: 'c', 4: "d"}
dicC = {5: 'e', 6: 'f'}
dicD = {}
for i in (dicA, dicB, dicC) : 
    dicD.update(i)
print(dicD)