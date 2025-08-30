# 1. Print the type of 42, 3.14, and 'hello'

print(type(2))
print (type(3.14))
print(type('hello'))

#Output
<class 'int'>
<class 'float'>
<class 'str'>

# 2. Converting string '100' to an integer.
s = '100'
n = int(s)
print(n)
print(type(n))

#Output
100
<class 'int'>

#The result is an integer

# 3. Add an integer and a float together. What is the result?
n = 200 #int
s = 120.4 # float
sum = n+s
print(sum)
print(type(sum))

#Output
320.4
<class 'float'>

#The result is a float.

# 4. What happens when you try to multiply a string by a number?
s = '8'
n = 10
result = s*n
print(result)

#Output
8888888888
# String is repeated many times as multiplying a string by an integer repeats the string.

### Challenge
#Write a program that:

#1. Asks the user to enter two numbers (as strings)
#2. Converts them to integers or floats
#3. prints their sum and type

a = input("Enter a number: ")
b = input("Enter a number: ")

def convert(n):
    try:
        return int(n)
    except ValueError:
        return float(n)

num1 = convert(a)
num2 = convert(b)

# Compute sum
sum = num1 + num2

# Print result and type
print(sum)
print(type(sum))

#Output
Enter a number: 2
Enter a number: 3.6
5.6
<class 'float'>















