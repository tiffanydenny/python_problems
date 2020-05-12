from user import User
import json
import os

def menu():
    # Ask for user's name
    name = input("Enter your name: ")
    # Check if a file exists for user
    filename = "{}.txt".format(name)
    # If it exists, welcome them and load their data
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    # If not, create a User object
    else:
        user = User(name)

    #Give them options:
    user_input = input("What would you like to do? Type corresponding letter: \n a: Add a movie \n"
                " b: See list of movies \n c: See list of watched movies \n d: Delete a movie \n w: Set a movie as watched \n s: Save \n q: Quit \n")

    while user_input != 'q':
        # Add a movie
        if user_input == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter the movie genre: ")
            user.add_movie(movie_name, movie_genre)
            # See list of movies
        elif user_input == 'b':
            for movie in user.movies:
                print("Name: {}, Genre: {}, Watched: {}".format(movie.name, movie.genre, movie.watched))
                # Set a movie as watched
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched: ")
            user.set_watched(movie_name)
                # Delete a movie by name
        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)
            # See list of watched movies
        elif user_input == 'c':
            for movie in user.watched_movies():
                print("Name: {}, Genre: {}, Watched: {}".format(movie.name, movie.genre, movie.watched))
            # Save and quit
        elif user_input == 's':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)

        user_input = input("What would you like to do? Type corresponding letter: \n a: Add a movie \n"
                    " b: See list of movies \n c: See list of watched movies \n d: Delete a movie \n w: Set a movie as watched \n s: Save \n q: Quit \n")

def file_exists(filename):
    return os.path.isfile(filename)

menu()






# Write to JSON file
# with open('movie_file.txt', 'w') as f:
#     json.dump(user.json(), f)

# Load from JSON file
# with open('movie_file.txt', 'r') as f:
#     json_data = json.load(f)
#     user = User.from_json(json_data)
#     print(user.json())
