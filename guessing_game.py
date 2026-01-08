# Number Guessing Game
# Codveda Internship - Level 1 Task 2

import random

print("===== NUMBER GUESSING GAME =====")

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)

# Maximum attempts
max_attempts = 5
attempts = 0

print("I have selected a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.\n")

# Game loop
while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Try again.\n")

    elif guess > secret_number:
        print("Too High! Try again.\n")

    else:
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
        break

# If user fails all attempts
if attempts == max_attempts and guess != secret_number:
    print("❌ Game Over!")
    print("The correct number was:", secret_number)
