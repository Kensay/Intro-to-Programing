# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toy that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")

#print (toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print (avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock", "Storyline", "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "Storyline", "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=niD-jahFURU")

midnight_in_paris = media.Movie("Midnight in Paris", "Storyline", "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games", "Storyline", "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)