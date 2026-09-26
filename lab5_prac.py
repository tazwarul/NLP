import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

text = input("Enter text ")
words=word_tokenize(text)

lemm_word=[lemmatizer.lemmatize(word,pos='v') for word in words]

print(words)
print(lemm_word)
