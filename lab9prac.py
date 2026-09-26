import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

text=input("Enter Text: ")

sia=SentimentIntensityAnalyzer()

scores = sia.polarity_scores(text)

compound = scores ['compound']
if compound >= 0.05:
    senti ="positive"
elif compound <=-0.05:
    senti = "Negative"
else :
    senti ="Neutral"

print("\n Scores: ",scores)
print("\n Overall Sentiment:  ",senti)
