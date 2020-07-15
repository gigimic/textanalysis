import spacy
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

from plot_word_cloud import visualize_word_cloud
from help_functions import clean_text_string
nlp = spacy.load('en')

story1 = open("story1.txt", "r")
full_story = story1.read()
paragraphs = full_story.split('\n\n') 

for paragraph in paragraphs:
    text = clean_text_string(paragraph)
    tokenized_word=word_tokenize(text)
    tagged_tokens=nltk.pos_tag(tokenized_word)

    all_entity = [token[1] for token in tagged_tokens]
    # print(all_entity)
    ref_entity = list(dict.fromkeys(all_entity)) #remove duplicates in the list
    print(ref_entity)



if __name__ == "__main__":
    import doctest
    doctest.testmod()