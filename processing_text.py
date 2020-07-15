import spacy
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from functools import reduce

from plot_word_cloud import visualize_word_cloud
from help_functions import clean_text_string
nlp = spacy.load('en')

story1 = open("story1.txt", "r")
# print(story1.read())
# full_story = story1.read()
# doc1 = nlp(full_story) 
  
# for ent in doc1.ents: 
#     print(ent.text, ent.start_char, ent.end_char, ent.label_) 

# Loop through the file line by line:
# f = open("demofile.txt", "r")
lines = []
# for x in story1:
#   print(x)

for i in range(3):
    line = story1.readline()
    lines.append(line.replace('\n',''))


# print(lines)

text = str(reduce(lambda x,y: x+" "+y, lines))
# print(text)

# The text is cleaned: everything except alphabets will be removed
clean_text = clean_text_string(text)
print(clean_text)

# following functions shows the word cloud visualization
# visualize_word_cloud(clean_text)


tokenized_text=sent_tokenize(text)
# print(tokenized_text)

# tokenized_word=word_tokenize(clean_text)
tokenized_word=word_tokenize(text)
print(tokenized_word)

fdist = FreqDist(tokenized_word)
print(fdist)

print(fdist.most_common(10))

# import matplotlib.pyplot as plt
# fdist.plot(30,cumulative=False)
# plt.show()

stop_words=set(stopwords.words("english"))

filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence ......:",tokenized_word)
print("Filterd Sentence ......:",filtered_sent)
print('\n ----------Next step')
# tagged_tokens=nltk.pos_tag(tokenized_word)
tagged_tokens=nltk.pos_tag(filtered_sent)
print(nltk.pos_tag(tokenized_word))

all_entity = [token[1] for token in tagged_tokens]
print(all_entity)
ref_entity = list(dict.fromkeys(all_entity)) #remove duplicates in the list
print(ref_entity)

name_entities = {}
for entry in ref_entity:
    name_entities[entry]=[]

# need to import pandas to use dataframe {} and save entity and name 

for token in tagged_tokens:
    for entry in ref_entity:
        if(token[1] == entry):
            # print(token[0], token[1])
            name_entities[entry].append(token[0])

print('....following are the named entities...')
for entry in ref_entity:
    print(entry, name_entities[entry])
    

# print(name_entities)
print('\n ----------Done')

if __name__ == "__main__":
    import doctest
    doctest.testmod()