# 1. Write a program that checks if a number is positive, negative, or zero.
number = float(input("Enter a number: "))  

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Output
Enter a number: -1
The number is negative.

# 2. Create a program that checks if someone is eligible to vote.
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Output
Enter your age: 12
You are not eligible to vote.
#
Enter your age: 23
You are eligible to vote.

# 3. Write a program that takes 3 numbers and prints the largest one.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}.")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}.")
else:
    print(f"The largest number is {num3}.")

#Output
Enter the first number: 4
Enter the second number: 5
Enter the third number: 7
The largest number is 7.0

# 4. Practice combining and, or, not.
number = int(input("Enter a number: "))

if (number > 0 and number % 2 == 0) or (number < 0 and number % 2 != 0):
    print("The number is either positive and even, or negative and odd.")
else:
    print("The number doesn't meet the conditions.")

#Output 1
Enter a number: 0
The number doesn't meet the conditions.
#Output 2
Enter a number: 2
The number is either positive and even, or negative and odd.

Challenge
# Build a grading system:

# Input score (0–100)
# Output grade: A (90+), B (80–89), etc
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#Output 1
Enter your score: 10
Grade: F
#Output 2
Enter your score: 78
Grade: C
