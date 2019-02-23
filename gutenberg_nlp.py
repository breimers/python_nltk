import nltk

def avg_word_len(num_chars, num_words):
    return int(num_chars / num_words)
def avg_sent_len(num_words, num_sents):
    return int(num_words / num_sents)

for file_id in nltk.corpus.gutenberg.fileids():
    num_chars = len(nltk.corpus.gutenberg.raw(file_id))
    num_words = len(nltk.corpus.gutenberg.words(file_id))
    num_sents = len(nltk.corpus.gutenberg.sents(file_id))

    print(file_id +
            "\n  Avg word length    : " +str(avg_word_len(num_chars, num_words)) +
            "\n  Avg sentence length: " +str(avg_sent_len(num_words, num_sents)))
