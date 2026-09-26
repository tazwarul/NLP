import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Input paragraph
paragraph = input("Enter a paragraph: ")

# Sentence tokenization
sentences = sent_tokenize(paragraph)

print("\nSentences:")
for sentence in sentences:
    print(sentence)

# Word tokenization
words = word_tokenize(paragraph)

print("\nWords:")
print(words)