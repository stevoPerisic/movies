import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = open("templates/main_page_head.html").read()

# The main page layout and title bar
main_page_content = open("templates/main_page_content.html").read()

# A single movie entry html template
movie_tile_content = open("templates/movie_tile_content.html").read()

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.Title,
            poster_image_url=movie.Poster,
            trailer_youtube_id=trailer_youtube_id,
            plot=movie.Plot,
            actors=movie.Actors,
            rating=movie.Rated,
            director=movie.Director,
            writer=movie.Writer,
            awards=movie.Awards,
            released=movie.Released,
            runtime=movie.Runtime
        )
    return content

def open_movies_page(movies):
  # Check if user already has output folder
  if not os.path.exists("output"):
    os.makedirs("output")

  # Create or overwrite the output file
  output_file = open('output/fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://output/' + url, new=2) # open in a new tab, if possible


