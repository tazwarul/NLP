import string

text = input("Enter a text: ")

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

print("Result:", text)