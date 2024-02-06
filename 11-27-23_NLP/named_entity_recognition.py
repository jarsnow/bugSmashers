from nltk import ne_chunk, pos_tag, word_tokenize
sentence = "Steve Jobs was the co-founder of Apple Inc."
ner_result = ne_chunk(pos_tag(word_tokenize(sentence)))

print("Named Entities:", ner_result)
