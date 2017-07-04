# IMDb_finder #

A Python script that reads movie names from a file and creates a file having IMDb ratings for each movie. I had a huge collection of movies taken from a friend and wanted to watch the best ones. This script scrapes IMDB ratings for each movie and lists them in a file.
Movie list
![Movie list](https://github.com/sankalp-sangle/imdb_finder/blob/master/Sample_Images/movielist.png)

Ratings file
![Ratings file](https://github.com/sankalp-sangle/imdb_finder/blob/master/Sample_Images/Generated_ratings.png)


## Requirements and Installation ##

The Python script uses Beautiful Soup python module. To install it, use
```bash
$pip install bs4
```

## Usage ##

#### Making a list of movie names ####

Navigate to the directory containing your movies and type the following command to create a file `movielist.txt` that contains names of movies, each name on a new line:
```bash
$ls > movielist.txt
```

Next, in line number _3_ of `imdbfinder.py` script,
```python
movielist = open('Insert path to text document containg list of movies, with each movie name on a new line');
```
insert the path to `movielist.txt` file that was created above.

In line number _5_ of `imdbfinder.py` script,

```python
imdbfile = open('Insert path to text document in which you want to store the imdb ratings','a'); # Open a file to store imdb ratings
```
insert the path to the file you want to store the ratings in.

Sample image - 
![Sample Paths](https://github.com/sankalp-sangle/imdb_finder/blob/master/Sample_Images/Sample_paths.png)

Finally, navigate to repository and type the following to execute the script.

```bash
$python3 imdbfinder.py
```

## Future improvements ##

A simple sort function can be added to arrange the movies in order of IMDb ratings.
Suggestions are welcome!
