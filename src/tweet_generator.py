__author__ = 'chow'

import sys
import os
import string
import random


TOTAL_LINES = 31250 * 1 #(1MB * multipler)
TOTAL_WORDS = 8
WORD_SIZE = 3


def word_generator(size=WORD_SIZE, chars=string.ascii_lowercase + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))

def line_generator(words=TOTAL_WORDS):
    return ' '.join(word_generator() for _ in range(words)) + '\n'


dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../tweet_input/tweets_test.txt')



with open(filename, 'w') as f:
    for i in range(TOTAL_LINES):

        # for j in range(TOTAL_WORDS):
        #     line += (word_generator())

        f.write(line_generator())
