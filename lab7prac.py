import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('punkt_tab')

text = input("Enter a text: ")
words = word_tokenize(text)
fdist=FreqDist(words)

print("\nMost Frequent Words:")
print(fdist.most_common(5))