import random

magic_numbers = [random.randint(0,9), random.randint(0,9)]  #choose 2 random numbers for people to guess

def check_number(): #let user enter a number, check wither it matches one of the random numbers, and respond to the user.
    user_number = input("Enter a number between 0 and 9: ")
    if user_number in magic_numbers:
        print("Correct!")
    elif user_number not in magic_numbers:
        print("Incorrect :(")


def run_program(chances): #Runs the check number method
    for attempt in range(chances):
        print("Attempt {}: ".format(attempt+1))
        check_number()

attempts = input("How many guesses do you want? ") #Allows user to choose number of guesses they want
run_program(attempts) #Runs check number method the appropriate number of times
