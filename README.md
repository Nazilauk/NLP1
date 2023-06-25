

# README

## Project Name 
Movie_next.py

## Project Description 
The Movie_next.py is a Python function that finds the movie similar to the description provided by the user. It uses pre-trained spacy model and cosine similarity to find the best matching movie from the dataset of movie descriptions. The function takes the movie description as input and returns the title of the most similar movie from the dataset. 

## Table of Contents
[ Installation.#Installastion]
- Usage
- Credits

## Installation
1. Clone or download the repository
```
git clone https://github.com/<username>/<reponame>.git
```
2. Create a virtual environment and activate it
```
python3 -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/bin/activate
```
3. Install the required libraries using pip
```
pip install -r requirements.txt
```
4. Run the program in your local machine
```
python movie_next.py
```

## Usage
1. In the command prompt, run the program using the command mentioned above
2. Enter the movie description for which you want to find similar movie
3. The program will print the title of the most similar movie from the dataset along with percentage of similarity between the user input and the most similar movie. 

## Credits
This project is created by Nazila Zadeh I used pre-trained spacy model and sklearn library for calculating cosine similarity between the word embeddings.
The data set has been obtain from hyperion task 21
