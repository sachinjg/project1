"""Stores details of movies and displays them on a website."""
import fresh_tomatoes
import media

home_alone = media.Movie("Home Alone", "Home Alone",       
                       "https://upload.wikimedia.org/wikipedia/en/7/76/Home_alone_poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=IsOlj-xpK9Q")

jurassic_park = media.Movie("Jurassic Parkt", "Jurassic Park",
                          "https://upload.wikimedia.org/wikipedia/en/e/e7/Jurassic_Park_poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=Bim7RtKXv90")

the_terminator = media.Movie("The Terminator", "The Terminator",
                            "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg",  # noqa
                            "https://www.youtube.com/watch?v=k64P4l2Wmeg")

predator = media.Movie("Predator", "Predator",
                     "https://upload.wikimedia.org/wikipedia/en/9/95/Predator_Movie.jpg",  # noqa
                     "https://www.youtube.com/watch?v=Y1txEAywdiw")

robocop = media.Movie("Robocop", "Robocop",
                    "https://upload.wikimedia.org/wikipedia/en/1/16/RoboCop_%281987%29_theatrical_poster.jpg",  # noqa
                    "https://www.youtube.com/watch?v=zbCbwP6ibR4")

the_silence_of_the_lambs = media.Movie("The Silence of the Lambs", "The Silence of the Lambs",  # noqa
                                     "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg",  # noqa
                                     "https://www.youtube.com/watch?v=lQKs169Sl0I")  # noqa

die_hard = media.Movie("Die Hard", "Die Hard",
                        "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg",  # noqa
                        "https://www.youtube.com/watch?v=2TQ-pOvI6Xo")

the_mummy_returns = media.Movie("The Mummy Returns", "The Mummy Returns",
                              "https://upload.wikimedia.org/wikipedia/en/b/b7/The_Mummy_Returns_poster.jpg",  # noqa
                              "https://www.youtube.com/watch?v=3yXjs7BUKYc")

the_lord_of_the_rings = media.Movie("The Lord of the Rings", "The Lord of the Rings",  # noqa
                                  "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",  # noqa
                                  "https://www.youtube.com/watch?v=V75dMMIW2B4")  # noqa

# Store the Movie objects in a list.
movies = [home_alone, jurassic_park, the_terminator, predator, robocop, the_silence_of_the_lambs, die_hard, the_mummy_returns, the_lord_of_the_rings]  # noqa

# Open the movie website in the user's browser, featuring the movies above.
fresh_tomatoes.open_movies_page(movies)
