import nltk
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from urllib.request import urlopen
from bs4 import BeautifulSoup

url=input("Enter a url: ")
lang=input("\nInput langauge: \n  (1)English \n  (2)Espanol \n  (2)Francais \nEnter number(1, 2, or 3): ")


#from web to utf8
raw = urlopen(url).read().decode('utf-8')
#remove html
raw_soup = BeautifulSoup(raw, features="html.parser")
for script in raw_soup(["script", "style"]):
    script.decompose()
soup = raw_soup.get_text()
#tokenize words based nltk libraries
the_words = nltk.Text(nltk.word_tokenize(soup))
#initialize stopwords
if lang == '1': stopwords = nltk.corpus.stopwords.words('english')
elif lang == '2': stopwords = nltk.corpus.stopwords.words('spanish')
elif lang == '3': stopwords = nltk.corpus.stopwords.words('french')
else: stopwords = nltk.corpus.stopwords.words('english')
#make list of 'cleaned' words by filtering out stopwords
clean_words = [w for w in the_words if not w in stopwords]
#tokenize setnences based nltk libraries
sentences = nltk.sent_tokenize(soup)
#create a distribution based on the raw
fdist = nltk.FreqDist(clean_words)
#create a string from list of clean words
full_text = str(''.join(map(str, clean_words)))

#quantify lists
num_chars = int(len(raw))
num_words = int(len(clean_words))
num_sents = int(len(sentences))

#this funtion finds avg word length
def avg_word_len(num_chars, num_words):
    return int(num_chars / num_words)
#this function finds avg sentences length
def avg_sent_len(num_words, num_sents):
    return int(num_words / num_sents)
#this function creates a wordcloud given a string
def plot_cloud(text):
    wordcloud=WordCloud(relative_scaling=0.5).generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

print("\nWORD LENGTH: " + str(avg_word_len(num_chars, num_words)))
print("\nSENT LENGTH: " + str(avg_sent_len(num_words, num_sents)))
print("\nHAPAXES    :  \n")
print(fdist.hapaxes())
plot_cloud(full_text)
