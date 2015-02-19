# media.py
import webbrowser
import urllib2
import json

class Movie():
	""" This class provides a way to store movie related information """
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	def __init__(self, title, trailer_youtube_url):
		response = urllib2.urlopen('http://www.omdbapi.com/?t='+title+'&y=&plot=short&r=json')
		# arguments = locals()
		# return ''.join(str(arguments[k]) for k in sorted(arguments.keys()) if arguments[k] is not None)
		data = json.load(response)
		for movie_attr in data:
			# print movie_attr
			# print data[movie_attr]
			# setattr(object, name, value)
			setattr(self, movie_attr, data[movie_attr])
		
		# print '****************************'
		# print self.Title
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)