import requests
from bs4 import BeautifulSoup
movielist = open('Insert path to text document containg list of movies, with each movie name on a new line'); # Opens file to read list of movies
content = movielist.readlines(); # Read names of movies into a list, content
imdbfile = open('Insert path to text document in which you want to store the imdb ratings','a'); # Open a file to store imdb ratings
for moviename in content:
    url = 'http://google.com/search?q=' + str(moviename);
    print("Downloading from" + str(url));
    res = requests.get(url);# get source code of html page
    res.raise_for_status();# Raise error if problem
    soup = BeautifulSoup(res.text,'html.parser');
    movie_info1 = soup.select('.s div'); # search for div tag inside class element s
    for result in movie_info1: # search over list of results found by select method
        if result.getText().find("Rating") != -1: # If content has a string called Rating in it,
            start = result.getText().index("Rating"); # Get start index of rating
            rating = result.getText()[start:start+14]; # rating is a substring containing rating of file
            imdbfile.write(str(moviename) + str(rating)+'\n'+'\n'); # Write to rating file ->the name of the movie and rating.
            break;
imdbfile.close();        
