#importing the random module
import random


#Generate a random number between 1 and 10

secret_number = random.randint(1,10)


#Maximun attempts allowed

max_attempts = 3


#Function for the recursivee giessing

def welcome_message():

    print("\nWelcome to the Number Gudessing Game!")

    print(f"You have {max_attempts} attempts tp guess the correct number.")

#Function for recursive guessting

def guess_recursive(attempts_left):

    #get user input
    guess = int(input("\nWelcome to the Number Guessing Game!: "))
#Check if thee guess is correct

    if guess == secret_number:
        print("congrtulations! You guessed the correct number!")

    else:

        print(f"Wrong guess. Attempts left : {attempts_left-1}")

    if attempts_left > 1:

        #Make a recursive call for another guess

        guess_recursive(attempts_left - 1)

    else:

        print(f"\nSorry, you couldn't guess the number. The correct number was {secret_number}.")
    

    #Calling the function

welcome_message()

guess_recursive(max_attempts)


#using id() to get memory addresses

print(f"Memory address of Secret Number {secret_number} is : {id(secret_number)}")
