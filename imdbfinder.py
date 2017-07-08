import requests, sys, os
from bs4 import BeautifulSoup


# cleanname() replaces periods,underscores,hyphens in filename with spaces and returns a substring till the earliest occuring element in keylist.
def cleanname(filename):
    filename = filename.replace('.', ' ').replace('_',' ').replace('-',' ')
    keylist = ['720','1080','19','20','bluray','dvdrip','brrip','extended','final cut','directors cut','director\'s cut','cdrip']
    indices = map(filename.lower().find,keylist)
    indices = [x for x in indices if x!= -1]
    if indices == []:
        return filename
    else:    
        return filename[:min(indices)-1]

# scrape() fetches the IMDb rating from the Google search webpage.
def scrape(movie,ratingfile):
    url = 'http://google.com/search?q=' + movie
    print("Downloading from" + url)
    res = requests.get(url) # get source code of html page
    res.raise_for_status() # Raise error if problem
    soup = BeautifulSoup(res.text,'html.parser')
    movie_info1 = soup.select('.s div') # search for div tag inside class element s
    for result in movie_info1: # search over list of results found by select method
        if result.getText().find("Rating") != -1: # If content has a string called Rating in it,
            start = result.getText().index("Rating") # Get start index of rating
            rating = result.getText()[start:start+14] # rating is a substring containing rating of file
            ratingfile.write(movie + ' ' + rating + '\n' + '\n') # Write to rating file ->the name of the movie and rating.
            return

def main():
    directory = sys.argv[1]
    imdbfile = open('imdb.txt','w') # Open a file to store imdb ratings
    content =[]
    

    for _,_,filenames in os.walk(directory):
        for files in filenames:
            if files[-4:] in ['.mp4', '.mkv', '.avi']:
                content.append(cleanname(files[:-4]))

    for moviename in content:
        scrape(moviename,imdbfile)
        
    imdbfile.close()


if __name__ == "__main__":
    main()
