import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download required resource
nltk.download('punkt')
nltk.download('punkt_tab')

# Create Porter Stemmer object
stemmer = PorterStemmer()

# Take input from user
text = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(text)

# Apply stemming
stemmed_words = []

for word in words:
    stemmed_words.append(stemmer.stem(word))

# Display output
print("\nOriginal Words:")
print(words)

print("\nStemmed Words:")
print(stemmed_words)