import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape (archived version of Empire's top 100 movies)
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to the URL to retrieve the webpage's content
response = requests.get(URL)
# Store the HTML content of the webpage
website_html = response.text

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(website_html, "html.parser")

# Find all the <h3> tags with the class "title" which contain the movie titles
all_movies = soup.find_all(name="h3", class_="title")

# Extract the text from each <h3> tag and store it in a list
movie_titles = [movie.getText() for movie in all_movies]
# Reverse the list to have the movies start from 1 instead of 100
movies = movie_titles[::-1]

# Open (or create) a file called "movies.txt" in write mode with UTF-8 encoding
with open("movies.txt", mode="w", encoding="utf-8") as file:
    # Write each movie title on a new line in the file
    for movie in movies:
        file.write(f"{movie}\n")
