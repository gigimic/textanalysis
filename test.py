import spacy

text1 = "In early 2002, Musk was seeking staff for his new space company, soon to be named SpaceX. Musk approached rocket engineer Tom Mueller"
nlp = spacy.load('en')

doc = nlp(text1)
ents = [(x.text, x.label_) for x in doc.ents]
print(ents)
for ent in ents:
    print(ent)

# GPE is Geopolitical Environment eg. countries, cities, states

# displacy.render # check it

# sentence = "Apple is looking at buying U.K. startup for $1 billion"
  
# doc1 = nlp(sentence) 
  
# for ent in doc1.ents: 
#     print(ent.text, ent.start_char, ent.end_char, ent.label_) 


# story1 = open("story1.txt", "r")
# full_story = story1.read()
# paragraphs = full_story.split('\n\n') 
# print(paragraphs[7])
# print('number of paragraphs ..', len(paragraphs))
# print('..........done')