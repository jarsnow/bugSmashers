import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "NLTK makes natural language processing easy!"
words = word_tokenize(text)
sentences = sent_tokenize(text)

print("Words:", words)
print("Sentences:", sentences)
