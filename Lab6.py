import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Take input from user
text = input("Enter a sentence: ")

# Tokenize
words = word_tokenize(text)

# POS tagging
pos_tags = nltk.pos_tag(words)

# Output
print(pos_tags)