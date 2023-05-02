import random

while True:
    
    print("New random number generated")
    secret_number = random.randint(1, 100)
    
    while True:
        
        guess = int(input("Guess the number between 1 and 100: "))
        
        if guess == secret_number:
            if input("Congratulations! You guessed the number!. Press 'Q' for Quit or anything else to continue\n").lower() == "q":
                break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")