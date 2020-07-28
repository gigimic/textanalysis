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

for index, paragraph in enumerate(paragraphs):
    text = clean_text_string(paragraph)
    tokenized_word=word_tokenize(text)
    tagged_tokens=nltk.pos_tag(tokenized_word)

    all_entity = [token[1] for token in tagged_tokens]
    # print(all_entity)
    ref_entity = list(dict.fromkeys(all_entity)) #remove duplicates in the list
    # print(ref_entity)

    name_entities = {}
    for entry in ref_entity:
        name_entities[entry]=[]

    # need to import pandas to use dataframe {} and save entity and name 

    for token in tagged_tokens:
        for entry in ref_entity:
            if(token[1] == entry):
                # print(token[0], token[1])
                name_entities[entry].append(token[0])

    # print('....following are the named entities...')
    # for entry in ref_entity:
    #     print(entry, name_entities[entry])

    # if index <4:
    print(index, '.............following are the main  entities...')
    doc = nlp(text)
    ents = [(x.text, x.label_) for x in doc.ents]
    # print(ents)
    for ent in ents:
        print(ent)




if __name__ == "__main__":
    import doctest
    doctest.testmod()