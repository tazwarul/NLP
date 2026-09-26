import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams

nltk.download('punkt')
nltk.download('punkt_tab')

# Take input from user
text = input("Enter a text: ")

# Tokenize the text
words = word_tokenize(text)

# Generate bigrams
bigram_list = list(bigrams(words))

# Display the bigrams
print("\nBigrams:")
print(bigram_list)