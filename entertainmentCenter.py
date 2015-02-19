# entertainmentCenter.py
import media
import fresh_tomatoes

# Stub movie

toy_story = media.Movie('Toy+Story', 'http://youtu.be/KYz2wyBy3kc')

# toy_story = media.Movie(
# 	"Toy Story", 
# 	"A story of a boy and his toys that come to life", 
# 	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
# 	"http://youtu.be/KYz2wyBy3kc")

# print(toy_story.storyline)

avatar = media.Movie("Avatar", "http://youtu.be/5PSNL1qE6VY")
# avatar = media.Movie(
# 	"Avatar",
# 	"A marine on an alien planet",
# 	"http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
# 	"http://youtu.be/5PSNL1qE6VY")

# print(avatar.storyline)
# avatar.show_trailer()

frozen = media.Movie("Frozen", "http://youtu.be/TbQm5doF_Uc")
# frozen = media.Movie(
# 	"Frozen",
# 	"Two sisters prove that the power of real love can thaw a frozen heart",
# 	"http://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
# 	"http://youtu.be/TbQm5doF_Uc")

# frozen.show_trailer()

cars = media.Movie("Cars", "http://youtu.be/SbXIj2T-_uk")
# cars = media.Movie(
# 	"Cars",
# 	"A hot-shot race-car named Lightning McQueen gets waylaid in Radiator Springs, where he finds the true meaning of friendship and family.",
# 	"http://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
# 	"http://youtu.be/SbXIj2T-_uk")

spider_man = media.Movie("Spider+Man+2", "http://youtu.be/BWsLc3j1AWg")
# spider_man = media.Movie(
# 	"Spider Man 2",
# 	"Peter Parker is beset with troubles in his failing personal life as he battles a brilliant scientist named Doctor Otto Octavius, who becomes Doctor Octopus (aka Doc Ock), after an accident causes him to bond psychically with mechanical tentacles that do his bidding.",
# 	"http://upload.wikimedia.org/wikipedia/en/0/02/Spider-Man_2_Poster.jpg",
# 	"http://youtu.be/BWsLc3j1AWg")

lego_movie = media.Movie("Lego+Movie", "http://youtu.be/Q2dFVnp5K0o")
# box_trolls = media.Movie(
# 	"Box Trolls",
# 	"The story of Eggs, a human boy raised by trash-collecting trolls, as he attempts to save them from Archibald Snatcher, a pest exterminator.",
# 	"http://upload.wikimedia.org/wikipedia/en/d/db/The_Boxtrolls_poster.jpg",
# 	"http://youtu.be/Q2dFVnp5K0o")

movies = [toy_story, avatar, frozen, cars, spider_man, lego_movie]
fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)
# response = urllib2.urlopen('http://www.omdbapi.com/?t=Toy+Story&y=&plot=short&r=json')
# data = json.load(response)
# args = []
# # print len(data)
# for x in data:
# 	# print data[x]
# 	args.append(x)

# print args
# print data['Title']  
# toy_story = media.Movie(args)
# print toy_story.Title
# print data









