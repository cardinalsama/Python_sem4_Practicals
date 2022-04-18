# 20CS066 - Dhritiman Senpramanik
# GIT Link - 

# a. Write a Python program to add member(s) in a set and clear a set
fruits = {'Apple', 'Banana', 'Orange'}
print(fruits)
fruits.add('Lemon')
print(fruits)
fruits.clear()
print(fruits)
print()

# b. Write a Python program to remove an item from a set if it is present in the set
fruits = {'Apple', 'Banana', 'Orange', 'Lemon'}
print(fruits)
fruits.remove('Lemon')
print(fruits)
print()

# c. Write a Python program to create an intersection, Union, difference of sets
fruits = {'Apple', 'Banana', 'Orange', 'Lemon', 'Tomato'}
vegetables = {'Potato', 'Onion', 'Cabbage', 'Lemon', 'Tomato'}
print(fruits)
print(vegetables)
print('Union', fruits.union(vegetables))
print('Intersection', fruits.intersection(vegetables))
print('Difference', fruits.difference(vegetables))
print()

# d. Writew a Python program to find maximum and the minimum value in a set
numbers = {1,2,3,4,5}
print(numbers)
print(max(numbers))
print(min(numbers))
print()

# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary

## For list:
def mostFrequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num, i

numbers = [1, 2, 2, 3, 3, 3]
print(numbers)
print("Most frequent number & frequency: ", mostFrequent(numbers))

## For tuple:
def mostFrequent(Tuple, x):
    count = 0
    for i in Tuple:
        if i == x :
            count += 1
    return count

number_tuple = (1,1,2,2,2,3,3,3,3)
print(mostFrequent(number_tuple, 3))

## For Dictionary:
def mostFrequent(Dictionary):
    values_list = list(Dictionary.values())
    return max(set(values_list), key = values_list.count)

number_dict = {
    'Year1' : 1990,
    'Year2' : 2002,
    'Year3' : 2002,
    'Year4' : 2002,
    'Year5' : 2022,
}

print(number_dict)
print(mostFrequent(number_dict))