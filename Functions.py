# 1. Write a function greet(name) that prints “Hello, [name]”.
def greet(name):
  print(f'Hello, {name}')
#Input
greet("Jacton")
#Output
Hello, Jacton

# 2. Create a function add(a, b) that returns the sum
def add(a,b):
  return a+b

print(add(4,3))

#Output
7

# 3. Modify add() to print “even” or “odd” based on the result
def add(a, b):
    result = a + b
    if result % 2 == 0:
        print("even")
    else:
        print("odd")
    return result

    #Example
print(add(2,3))
print(add(4,6))

#Output
odd
5
even
10

# 4. Call a function from within another function.
def greet(name):
    print(f"Hello, {name}")

def comment_learner(name):
    greet(name)  # Calling the 'greet' function from within 'welcome_user'
    print("You are lazy!")

# Now, calling 'comment_learner'
comment_learner("Amos")

#Output
Hello, Amos
You are lazy!

Challenge
# Write a calculator function:

#Takes two numbers and an operation (+, -, *, /)
#Returns the result

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Testing the function
print(calculator(11, 5, '+'))  
print(calculator(9, 4, '-'))  
print(calculator(10, 9, '*'))  
print(calculator(50, 5, '/'))  
print(calculator(2, 0, '/'))  
print(calculator(8, 5, '^'))  

#Ouput
16
5
90
10.0
Error: Division by zero
Error: Invalid operation