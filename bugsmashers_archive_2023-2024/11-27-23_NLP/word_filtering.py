import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK stop words data
nltk.download('stopwords')
nltk.download('punkt')

# Example usage
input_sentence = "NLTK is a powerful tool for natural language processing in Python if the the if if because if the"

# Tokenize the sentence into words
words = word_tokenize(input_sentence)

# Get the list of English stop words and filter them out
filtered_words = [word for word in words if word.lower() not in set(stopwords.words('english'))]

# Join the filtered words back into a sentence
filtered_sentence = ' '.join(filtered_words)

# Display the results
print("Original Sentence:", input_sentence)
print("Filtered Sentence:", filtered_sentence)
