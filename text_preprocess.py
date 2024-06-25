import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk import sent_tokenize,word_tokenize
nltk.download("stopwords")
mystop_words=set(stopwords.words("english"))
lemmatizer=WordNetLemmatizer()
stemmer=PorterStemmer()
from string import punctuation

def text_preprocessing(text):
    text = text.lower()
    # text = ' '.join(text.split())
    text = word_tokenize(text)
    text = [word for word in text if word.isalnum() and word not in mystop_words and word not in punctuation]
    # Lemmatize the words
    text = [lemmatizer.lemmatize(word) for word in text]
    return text

    

if __name__ == "__main__":
   pass