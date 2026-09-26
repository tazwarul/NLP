import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('punkt_tab')

stemmer=PorterStemmer()

text = input("Enter text: ")

words = word_tokenize(text)

stem_word = [stemmer.stem(word) for word in words]

print(words)
print(stem_word)