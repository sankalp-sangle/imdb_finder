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
            if '.' not in rating:
                rating=rating[:-2]
            ratingfile.write(movie + ' ' + rating + '\n' + '\n') # Write to rating file ->the name of the movie and rating.
            return

#This function scrapes the IMDb from the movie list.
def scrape_imdb(s):
    values=s.split()

    if values != []:
        temp=values[-1]
        rating=float(temp[:-3])
        return rating


#A sort function which sort the movie list in either ascending or descending order!
def sort_imdb(rating_file_txt,order):
    rating_file=open(rating_file_txt,'r')
    data=" "
    ele=[]
    while data!="":
        data=rating_file.readline()
        if data!='\n' and data!="":
            ele.append(data)
    rating_file.close()

    rating_file=open(rating_file_txt,'w')


    if order == 'A' or order=='a':
        ele.sort(key=lambda x : scrape_imdb(x))
    else:
        ele.sort(key=lambda x : scrape_imdb(x),reverse=True)

    for line in ele:
        rating_file.write(line+"\n")




def main():
    directory = sys.argv[1]
    order=sys.argv[2] # Order for sorting the IMDb list.
    imdbfile = open('imdb.txt','w') # Open a file to store imdb ratings.
    content =[]
    

    for _,_,filenames in os.walk(directory):
        for files in filenames:
            if files[-4:] in ['.mp4', '.mkv', '.avi']:
                content.append(cleanname(files[:-4]))


    for moviename in content:
        scrape(moviename,imdbfile)

    imdbfile.close()
    #The user enters the order in which the IMDb list will be sorted.
    sort_imdb('imdb.txt',order)    #'a'/'A' for Ascending Sort and 'd'/'D' for Descending Sort




if __name__ == "__main__":
    main()
