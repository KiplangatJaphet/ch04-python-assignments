# 1. Use a for loop to print numbers from 1 to 10
for i in range(1,11):
  print(i)
# Explanation:
#The range() function generates a sequence of numbers. range(1, 11) gives you numbers from 1 to 10 (since the end value, 11, is exclusive).
#Output
1
2
3
4
5
6
7
8
9
10

#2. Use a while loop to print numbers until the user enters stop.
while True:  # Infinite loop to keep asking the user for input
    user_input = input("Enter a number (or type 'stop' to end): ")  # Ask for input
    
    if user_input.lower() == 'stop':  # If the user types 'stop' (case-insensitive), break the loop
        print("Stopping the loop...")
        break  # Exit the loop
    else:
        print(f"You entered: {user_input}")  # Print what the user entered
#Output
Enter a number (or type 'stop' to end): 5
You entered: 5
Enter a number (or type 'stop' to end): stop
Stopping the loop..

#3. Write a loop that prints even numbers from 1 to 20.
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
#Output
2
4
6
8
10
12
14
16
18
20

# 4. Explain what break and continue do in your own words.
#break:The break statement immediately stops the loop and exits it and is used when you want to end a loop early under a certain condition.

#continue: The continue statement skips the rest of the code inside the loop for the current iteration and moves to the next iteration. It's used when you want to skip specific iterations but continue looping.

Challenge
#Write a guessing game that asks the user to guess a secret number between 1 and 10.
# Give feedback (too high / too low)
#Use a while loop

import random

def guessing_game():
    secret = random.randint(1, 10)  # Secret number between 1 and 10
    guess = None  # Initialize guess
    
    print("Guess the secret number between 1 and 10!")

    while guess != secret:
        guess = int(input("Enter your guess: "))

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print("Correct! The secret number was", secret)

# Run the guess game
guessing_game()

#Output
Guess the secret number between 1 and 10!
Enter your guess: 9
Too high! Try again.
Enter your guess: 2
Too low! Try again.
Enter your guess: 4
Correct! The secret number was 4