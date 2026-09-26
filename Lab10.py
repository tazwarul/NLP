import nltk

from nltk.tokenize import word_tokenize

from nltk import pos_tag, ne_chunk

# Download NER resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

# Take input from user
text = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(text)

# Perform POS tagging
pos_tags = pos_tag(words)

# Perform Named Entity Recognition and chunking
ner_tree = ne_chunk(pos_tags)

# Display the NER result
print(ner_tree)