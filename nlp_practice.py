# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:58:04 2019

@author: black
"""


#NLTK Book Scripts go here
#Chapter 1
from nltk.book import text3 as bible,  \           #to avoid star imports
text1 as moby_dick, text4 as inaugural_address, \
text2 as Jane_austen, text5 as chat

text1.concordance('monstrous') #Search for word, ONLY WORKS with * import! 
text2.similar('monstrous')     #similar words, differs per text!
text3.similar('God')

Jane_austen.common_contexts(["monstrous", 'very'])  #Common contexts for words

#Dispersion text tells us distribution of each word along the text's progression
inaugural_address.dispersion_plot(['citizens' , 'democracy', 'freedom', 'duties', 'America', 'God']) 
bible.dispersion_plot(['Jesus', 'God'])

chat.generate()      #generate text based on style of input
bible.generate()      #each time is different
inaugural_address.generate()  #according to the text!

texts = [bible, moby_dick, inaugural_address,
         Jane_austen, chat]

for text in texts:
    print('{}'.format(text), len(text))  #sample chosen texts' nominal sizes
    
def lexical_diversity(text):
    '''
       How many times a word appears on average on given text. 
       Higher means poorer diversity, lower better diversity
    '''   
    return(len(text) / len(set(text)))
    
def percent_word(text,word):
  ''' What percent of the text constitutes of the target- word'''
    count = text.count(word)
    percent = 100*count/ len(text)
    return percent

#print(percent_word(chat, 'lol'))
#list.append("item") -> append to end of list

' '.join(['Monty' ,'Python']) #join list to str
'Monty Python'.split()        #split str to list
import matplotlib.pyplot as plt
import pandas as pd
from nltk.probability import FreqDist
fdist_moby = FreqDist(moby_dick)  #frequency distribution
fdist_bible = FreqDist(bible)
fdist_chat = FreqDist(chat)

print(fdist_moby.most_common(10))
fdist_moby.plot(50, cumulative=True); plt.show()
print(fdist_bible.most_common(10))
print(fdist_chat.most_common(10))

print(len(fdist_moby.hapaxes()))  #words that occur once only
long_words = [word for word in moby_dick if len(word) >= 15] #long words 
long_words = sorted(set([w for w in chat if len(w) > 6 and 
              fdist_chat[w] > 7])) #long words w/ more conditions
#length of word and numer of occurences via FreqDist
from nltk import *
print(bigrams(['more', 'is' , 'said', 'than', 'done']))    

print('; '.join(chat.collocation_list())) #common bigrams

fmoby = FreqDist([len(w) for w in moby_dick]) #freq dist of lenghts of words!
print(fmoby.items())  #keys-values : length, apperances of words

#page 44 for more functions!
#page 45 for word comparison operators

#Examples of list comprehensions 
words_with_gnt = [w for w in moby_dick if 'gnt' in w]
words_with_initial_capital = [w for w in Jane_austen if w.istitle()]
words_only_digits = [w for w in chat if w.isdigit()]
words_lower_unique = len(set([w.lower() for w in chat if w.isalpha() ])) #true vocab
#HERE: TO SOLVE SOME CHAPTER 1 EXERCISES
#---------------------------------
##CHAPTER 2:Accessing Text Corpora
import nltk
#print(nltk.corpus.gutenberg.fileids()) #prints filenames for nltk.gutenberg
emma = nltk.corpus.gutenberg.words('austen-emma.txt') #select text
#print(len(emma))
emma = nltk.Text(emma)  #to use previous functions as with nltk.book txts
print(emma.concordance('surprise'))
print(' '.join(emma[20:50])) #LIST to STRING - comes out as text

#examples of corpus available in nltk
from nltk.corpus import webtext  #less formal text
print(webtext.fileids())  #filenames

from nltk.corpus import nps_chat #predators
print(nps_chat.fileids()) 

from nltk.corpus import brown #brown uni various texts
print(brown.fileids())

from nltk.corpus import reuters
print(reuters.fileids())

from nltk.corpus import inaugural
print(inaugural.fileids())
#page 72 for a variety of corpus functionality commands



##SPACY SECTION - DataCamp course code collection, starting with 'Feature Engineering for NLP'
import spacy 
# Load model and create Doc object
nlp = spacy.load('en')

# Function to preprocess text
def preprocess(text):
  	# Create Doc object
    doc = nlp(text)
    # Generate lemmas
    lemmas = [token.lemma_ for token in doc]
    # Remove stopwords and non-alphabetic characters
    a_lemmas = [lemma for lemma in lemmas 
            if lemma.isalpha() and lemma not in stopwords]
    
    return ' '.join(a_lemmas)

#POS tagging
pos = [(token.text, token.pos_) for token in doc]  

#NER
ner = [(ent.text, ent.label_) for ent in doc.ents)]

#n-gram creation
from sklearn.feature_extraction.text import CountVectorizer as CVec
vectorizer = CVer(ngram_range=(start, end))
#corpus = pd.Series(['', '', .... ,''])
bow_matrix = vectorizer.fit_transform(corpus)

#Naive Bayes classifier import
#from sklearn.naive_bayes import MultinomialNB

#tf-idf vectors
from sklearn.feature_extraction import TfidfVectorizer as Tf
vec = Tf()
tfidf_matrix= vec.fit_transform(corpus)

#cosine similarity
from sklearn.metrics.pairwise import cosine_similarity #for general cases
from sklearn.metrics.pairwise import linear_kernel #for when norms don't matter, as in tfidf vectors
