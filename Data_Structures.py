#1. Create a list of 5 fruits and print the third fruit.
def fruit_list():
  fruits = ['mango', 'apple', 'orange', 'pawpaw', 'guava']
print(fruits[2])
#Output
orange

# 2. Create a dictionary with keys: name, age. Print the value of age.
learner = {'name': 'Moses', 'age': 34}
print(learner['age'])
#Ouput
34

# 3. Define a tuple with three numbers. Try modifying it. What happens?
numbers = (3,4,5)
#Trying to modify tuple
numbers[3] = 4
#Output
TypeError: 'tuple' object does not support item assignment
#Explanation: Tuples are immutable in Python, meaning once they're defined, their values can't be changed.

# 4. Create a set from a list with duplicate values.
fruit_list = ['mangoe', 'banana', 'mangoe', 'cherry', 'apple' 'banana']
fruit_set = set(fruit_list)
print(fruit_set)
#Output
{'mangoe', 'banana', 'applebanana', 'cherry'}


Challenge
#Create a program that:

#Takes 5 user inputs and stores them in a list
#Converts the list into a set and prints the unique values
# Step 1: Take 5 user inputs and store them in a list
user_inputs = []
for _ in range(5):
    user_input = input("Enter a value: ")
    user_inputs.append(user_input)

# Step 2: Convert the list into a set to remove duplicates
unique_values = set(user_inputs)

# Print the unique values
print("Unique values:", unique_values)

#Output
Enter a value: 1
Enter a value: 2
Enter a value: 3
Enter a value: 4
Enter a value: 5
Unique values: {'1', '3', '2', '4', '5'}