import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Take input from user
text = input("Enter a text: ")

# Tokenize the text
words = word_tokenize(text)

# Calculate word frequency
fdist = FreqDist(words)

# Display 5 most frequent words
print("\nMost Frequent Words:")
print(fdist.most_common(5))