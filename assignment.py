import random

def number_guessing_game():
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("Welcome to the Number Guessing Game!")
    print(f"Guess the number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    else:
       
        print(f"Game Over! The number was {number_to_guess}.")


number_guessing_game()
