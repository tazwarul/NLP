import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

# User input
text = input("Enter a text: ")

# Tokenize the text
words = word_tokenize(text)

# Get English stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords
filtered = [w for w in words if w.lower() not in stop_words]

print("After removing stopwords:", filtered)