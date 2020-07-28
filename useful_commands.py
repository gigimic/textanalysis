
import spacy
# print(spacy.__version__)

nlp = spacy.load("en_core_web_lg")
doc = nlp(u"This is a sentence.")

# #assign the default stopwords list to a variable
STOP_WORDS = spacy.lang.en.stop_words.STOP_WORDS
# print(nlp.Defaults.stop_words)

# stop words can be added or removed
# Add a single stopword:
nlp.Defaults.stop_words.add("add")
# Add several stopwords:
nlp.Defaults.stop_words |= {"stop","word",}
# Remove a single stopword:
nlp.Defaults.stop_words.remove("remove")
# Remove several stopwords:
nlp.Defaults.stop_words -= {"stop", "word"}

# similarity matching
doc1 = nlp("How do I turn sound on/off?")
doc2 = nlp("How do I obtain a pet?")
doc1.similarity(doc2)

# here doc1 and doc2 are very different sentences. but we get a similarity of 0.86
# therefore we need to preprocess the text
doc1 = nlp("turn sound on/off?")
doc2 = nlp("obtain a pet?")
doc1.similarity(doc2)

# Here the similarity of 0.48

# custom functions for preprocessing the text
# remove stopwords
def remove_stopwords_fast(text):
    doc = nlp(text.lower())
    result = [token.text for token in doc if token.text not in nlp.Defaults.stop_words]
    return " ".join(result)

# remove pronouns 
def remove_pronoun(text):
    doc = nlp(text.lower())
    result = [token for token in doc if token.lemma_ != '-PRON-']
    return " ".join(result)

# If you intend to get only the lemmatization form of the word, 
# you can modify the code into the following:

def remove_pronoun(text):
    doc = nlp(text.lower())
    result = [token.lemma_ for token in doc if token.lemma_ != '-PRON-']
    return " ".join(result)

Remove stopwords, punctuation, and pronouns together
def process_text(text):
    doc = nlp(text.lower())
    result = []
    for token in doc:
        if token.text in nlp.Defaults.stop_words:
            continue
        if token.is_punct:
            continue
        if token.lemma_ == '-PRON-'
            continue
        result.append(token.lemma_)
    return " ".join(result)

# Calculate similarity with pre-processing functions
#  call the pre-processing function right before the similarity function
 def calculate_similarity(text1, text2):
    base = nlp(process_text(text1))
    compare = nlp(process_text(text2))
    return base.similarity(compare)

# Evaluation
faq_questions= [What can I do if there is emergent game issue?
What can I do if my Flash Player version is too old?
What can I do if the game stuck on loading page?
What can I do if the Flash Player crashed?
What can I do if I can't login?
How could I get the chance to play the game?
Will my Beta Release account be deleted? Can I recharge during Beta Release?
Can I get high quality souls with my low quality souls?
How many qualities of Hero Souls there are?
What's the usage of Hero Soul?
Why some players get better reward from Conquest?
What's the benefit if a guild occupied a mine area?
Why can't I attack some players' mine?
Is all the mining area the same?
Why other player get better reward than I do?
Can I control the skills manually in Arena?
Why I can't explore a certain stage?
Can I challenge the stage I already passed?
What's the usage of Mount?]

customer_questions=['What can I do if my Flash Player version is too old?'
'How could I get the chance to play the game?' 
"Why can't I enter the game?" 
"What's the highest level I can reach?" 
"Why I can't explore a certain stage?" 
'How do I gain Activity points?']


# following are the references for spacy
# https://spacy.io/usage/vectors-similarity
# https://spacy.io/models
# https://support.gtarcade.com/faq?gid=182&cid=651
# https://stackoverflow.com/questions/41170726/add-remove-stop-words-with-spacy



if __name__ == "__main__":
    import doctest
    doctest.testmod()