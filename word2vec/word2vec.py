import sys
sys.path.append("..")
from common.util import preprocess

text = 'you ays goodbye and I say hello'
corpus, word_to_id ,id_to_word = preprocess(text)
print(corpus)