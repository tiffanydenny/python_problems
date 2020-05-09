import random

magic_numbers = [random.randint(0,9), random.randint(0,9)]

def check_number():
    user_number = input("Enter a number between 0 and 9: ")
    if user_number in magic_numbers:
        print("Correct!")
    elif user_number not in magic_numbers:
        print("Incorrect :(")


def run_program(chances):
    for attempt in range(chances):
        print("Attempt {}: ".format(attempt+1))
        check_number()

attempts = input("How many guesses do you want? ")
run_program(attempts)
