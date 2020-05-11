from movie import Movie
from user import User

user = User("Tiffany")
my_movie = Movie("Ever After", "Romantic", True)

user.movies.append(my_movie)
print(user.watched_movies())
