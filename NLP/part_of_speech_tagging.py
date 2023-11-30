from nltk import pos_tag, word_tokenize
words = word_tokenize("NLTK is a fantastic library for NLP")
pos_tags = pos_tag(words)

print("Part-of-Speech Tags:", pos_tags)
