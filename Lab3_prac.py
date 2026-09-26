import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt tab')
nltk.download('stopwords')

text = input("Enter Text: ")

words = word_tokenize(text)

stop_word =set(stopwords.words('english'))

filtered =[w for w in words if w.lower()  not in stop_word]

print("After removing: ", filtered)