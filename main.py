import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
link = response.text
soup = BeautifulSoup(link, 'html.parser')

lists = soup.find_all(name = "h3")

movies = [movie.getText() for movie in lists]
movies.reverse()
print(movies)

with open("C:/Users/Asanka/Desktop/Python Practice/100 movies to watch/movies.txt",'w', encoding='utf-8') as f:
    for movie in movies:
        f.write("%s\n" % movie)
