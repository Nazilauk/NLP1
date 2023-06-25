##----------------------------------------------------------------------------------------------------------------------------------------------------------
##This code creates a function that compares the cosine similarity between the user's input and a database of movie descriptions. 
##It returns the movie with the highest similarity score to the user's input. The movie descriptions are tokenized using the CountVectorizer function 
##and the pre-trained spacy model is used to compute the word embedding vector for each token. 
##The cosine similarity between each movie description and the input is calculated using sklearn's cosine_similarity function. 
##The movie title with the highest cosine similarity is returned.
##-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#import libraries

import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

# Load pre-trained spacy model
nlp = spacy.load('en_core_web_md')

# Read the movies.txt file and store it in the list named movies

with open('movies.txt') as f:
    movies = [line.rstrip() for line in f]

#Define a function to find similar movie based on user's input

def find_similar_movie(description):
    # process user input
    input_doc = nlp(description)

    # create count vectorizer instance
    vectorizer = CountVectorizer()
    
    # tokenize and create document-term matrix
    doc_term_matrix = vectorizer.fit_transform(movies)
    
    # get word vectors for input and movies
    input_vector = np.mean([token.vector for token in input_doc], axis=0)
    movie_vectors = np.vstack([np.mean([token.vector for token in nlp(movie)], axis=0) for movie in movies])

    # calculate cosine similarity between input and movies
    cosine_similarities = cosine_similarity([input_vector], movie_vectors)

    # get index of movie with highest similarity
    most_similar_index = np.argmax(cosine_similarities[0])

    # return title of most similar movie
    return movies[most_similar_index]

# Test the function with an example input
description = '''Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk 
into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately,
Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'''
#print the similar moive with decription 
print(find_similar_movie(description))

