import sys
import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def visualize_word_cloud(text: str):
    wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show(block=False)
