import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('punkt tab')

text= input("Enter paragraph= ")

sentences= sent_tokenize(text)
print("\nSentence: ")
for sentence in sentences:
    print(sentence)

word= word_tokenize(text)
print(word)

