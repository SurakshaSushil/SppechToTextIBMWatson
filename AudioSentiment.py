from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tdm import *
from transcriber import *
def create_listoflists(lists):
    docs = list()
    docs.append(str(lists))
    #docs.append('several severe tornadoes') #remove this you need to keep appending lists later, just for testing!!!!
    print(docs)
    if len(docs) == 1:  #mentioning the number of files before one can construct a tdm, thought 10!
        construct_tdm(docs)

def frequentlyusedwords_negativewords(sentence):
    freq = {}
    for item in sentence:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    frequentwords = list()

    with open('negative.txt', 'r') as file:
        for line in file:
            for word in line.split():
                if word in freq:
                    frequentwords.append(word)
                else:
                    continue
    count = 0
    for i in range(7):
        Keymax = max(freq, key=freq.get)
        frequentwords.append(Keymax)
        freq.pop(Keymax)
        count = count + 1
    newlist = list(set(frequentwords))
    listToStr = ' '.join([str(elem) for elem in newlist])
    create_listoflists(listToStr)

def stopwords_stemming(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    frequentlyusedwords_negativewords(filtered_sentence)

def speechtotext(filename):
    text = convert(filename)
    print(text)
    stopwords_stemming(text)

speechtotext('audio-file.wav')