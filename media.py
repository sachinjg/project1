"""Defines the Movie class that contains the details of a movie."""
import webbrowser


class Movie():
    """This class provides a way to store movie related information.
    Attributes:
        favorite: A string to store the hit movies.
        title: A string to store the title of the movie.
        poster_image_url: A string to store the URL of the movie poster.
        trailer_youtube_url: A string to store the URL of the movie trailer.
    """
    def __init__(self, favorite_movie, movie_title, poster_image, trailer_youtube):  # noqa
        self.movie = favorite_movie
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


def show_trailer(self):
    """Plays the movie trailer in the web browser."""
    webbrowser.open(self.trailer_youtube_url)
