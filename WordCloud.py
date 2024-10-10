import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, STOPWORDS

df = pd.read_csv(r"F:\py.ex\pythonVisual\youtube+cookery+channels+viewers+comments+in+hinglish\Cooking Data\kabita_preprocessing.csv",
                 encoding='latin-1')
comment_words = ''
stopwords = set(STOPWORDS)

for i in range(4900):
    tokens = str(df.__array__()[i][1]).split()
    for x in tokens:
        token = x.lower()
        comment_words += ''.join(token)+' '

wordcloud = WordCloud(width=800, height=800, background_color='white', stopwords=stopwords, min_font_size=10).generate(comment_words)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad=0)

plt.show()
