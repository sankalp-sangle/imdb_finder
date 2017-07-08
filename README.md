# IMDb_finder #

A Python script that reads movie names from a specified directory and creates a file having IMDb ratings for each movie. I had a huge collection of movies taken from a friend and wanted to watch the best ones (Disclaimer : I do not agree that IMDb ratings are the best judge of a movie ;) ). This script scrapes IMDB ratings for each movie and lists them in a file.
Here is a non-exhaustive list of movies that I had :
![Movie list](https://github.com/sankalp-sangle/imdb_finder/blob/master/Sample_Images/movielist.png)

Here is the ratings file that the script produces.
Ratings file
![Ratings file](https://github.com/sankalp-sangle/imdb_finder/blob/master/Sample_Images/ratings.png)

One need not worry about jumbled and messy file names like 'Cinema.Paradiso.1988.1080p.BluRay.x264.anoXmos.mp4', the script takes care of the same.

## Requirements and Installation ##

The Python script uses Beautiful Soup python module. To install it, use
```bash
$pip install bs4
```

## Usage ##
The path to the directory containing your movies is passed as a command line argument, as shown:
```bash
$python3 imdbfinder.py enter_complete_path_to_directory_here
```
### Example ###
```bash
$python3 imdbfinder.py /home/sankalp/Movies
```

**NOTE** 
Ensure that you are using Python 3 and not Python 2. There may be Unicode-related errors in Python 2.

## Future improvements ##

A simple sort function can be added to arrange the movies in order of IMDb ratings.
Suggestions are welcome!
