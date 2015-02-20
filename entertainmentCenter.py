# entertainmentCenter.py
import media
import fresh_tomatoes
import json

# load movies from a JSON file
jsonData = open("movies_json.json")
movies_json = json.load(jsonData)

# create instances of our Movie class
toy_story = media.Movie(movies_json['toy_story'], 'http://youtu.be/KYz2wyBy3kc')
avatar = media.Movie(movies_json['avatar'], "http://youtu.be/5PSNL1qE6VY")
frozen = media.Movie(movies_json['frozen'], "http://youtu.be/TbQm5doF_Uc")
cars = media.Movie(movies_json['cars'], "http://youtu.be/SbXIj2T-_uk")
spider_man = media.Movie(movies_json['spider_man'], "http://youtu.be/BWsLc3j1AWg")
lego_movie = media.Movie(movies_json['lego_movie'], "http://youtu.be/Q2dFVnp5K0o")

movies = [toy_story, avatar, frozen, cars, spider_man, lego_movie]

# open a webpage with a graphical representation of our movies JSON
fresh_tomatoes.open_movies_page(movies)










