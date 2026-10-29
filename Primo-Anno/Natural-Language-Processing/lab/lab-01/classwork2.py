import nltk

tokens = nltk.word_tokenize("On 14 March 2026, Dr. Smith sent 3 reports.")
print(nltk.pos_tag(tokens))