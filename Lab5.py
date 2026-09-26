import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

# Create lemmatizer
lemmatizer = WordNetLemmatizer()

# Take input from user
text = input("Enter a sentence: ")

# Tokenize
words = word_tokenize(text)

# Lemmatization
lemmatized_words = []

for word in words:
    lemma = lemmatizer.lemmatize(word, pos='v')
    lemmatized_words.append(lemma)

# Output
print("\nOriginal Words:")
print(words)

print("\nLemmatized Words:")
print(lemmatized_words)