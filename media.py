# media.py
import webbrowser

class Movie():
	""" 
	This class provides a way to store movie related information 
	{dict} - movie 
		{params} - Title
				 - Year
				 - Rated
				 - Released
				 - Runtime
				 - Genre
				 - Director
				 - Writer
				 - Actors
				 - Plot
				 - Language
				 - Country
				 - Awards
				 - Poster
				 - Metascore
				 - imdbRating
				 - imdbVotes
				 - imdbID
				 - Type
				 - Response
	"""
	
	def __init__(self, movie, trailer_youtube_url):
		print movie
		for movie_attr in movie:
			setattr(self, movie_attr, movie[movie_attr])
		
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)