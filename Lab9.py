import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download('vader_lexicon', quiet=True)

# Create VADER analyzer
sia = SentimentIntensityAnalyzer()

# Take input from user
text = input("Enter a text: ")

# Calculate sentiment scores
scores = sia.polarity_scores(text)

# Get compound score
compound = scores['compound']

# Determine sentiment
if compound >= 0.05:
    sentiment = "Positive"

elif compound <= -0.05:
    sentiment = "Negative"

else:
    sentiment = "Neutral"

# Display results
print("\nScores:", scores)
print("Overall Sentiment:", sentiment)