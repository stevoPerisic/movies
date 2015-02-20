# media.py
import webbrowser

class Movie():
	""" This class provides a way to store movie related information """
	
	def __init__(self, movie, trailer_youtube_url):
		for movie_attr in movie:
			setattr(self, movie_attr, movie[movie_attr])
		
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)