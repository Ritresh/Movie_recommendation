from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def stem(text):

    y=[]

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)