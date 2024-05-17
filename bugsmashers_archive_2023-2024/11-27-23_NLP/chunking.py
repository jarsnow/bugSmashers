import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize

# Example sentence
sentence = "The quick brown fox jumps over the lazy dog"

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Part-of-speech tagging
pos_tags = nltk.pos_tag(words)

# Define a simple grammar pattern for chunking
grammar = r"""
    NP: {<DT>?<JJ>*<NN>}   # NP: Noun Phrase
    VP: {<VB.*><NP|PP|CLAUSE>+$}  # VP: Verb Phrase
    CLAUSE: {<NP><VP>}  # Clause
"""

# Create a RegexpParser with the defined grammar
chunk_parser = RegexpParser(grammar)

# Apply chunking
tree = chunk_parser.parse(pos_tags)

# Display the result
print("Original Sentence:", sentence)
print("Part-of-Speech Tags:", pos_tags)
print("Chunked Tree:", tree)
