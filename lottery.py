import random
#using list comprehension, sets, set comprehension


def play_lotto():
    # Ask player for numbers
    user_numbers = get_player_numbers()
    # Calculate lottery numbers
    lotto_numbers = lottery_numbers()
    # Print winnings
    matched_numbers = ", ".join(str(n) for n in user_numbers.intersection(lotto_numbers))
    print ("You matched {}. You won ${}!".format(matched_numbers, 100 ** len(matched_numbers)))

# User can pick 6 numbers (between 1 and 20)

def get_player_numbers():
    number_csv = input("Pick 6 numbers, separated by commas: ")
    integer_set = {int(number) for number in number_csv}
    return integer_set

# Lottery calculates 6 random numbers
#
def lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values

play_lotto()
