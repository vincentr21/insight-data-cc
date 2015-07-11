# Author: Vincent Ren
# Date: Fri, Jul 10, 15

import sys
import os
from collections import Counter

# sets the number of bins kept in our histogram, 70 is the max number of words since a tweet is 140 characters
MAX_WORDS_IN_TWEET = 70

# relative paths are needed to reference files properly
dir = os.path.dirname(__file__)
filename_in = os.path.join(dir, '../tweet_input/tweets.txt')
# filename_in = os.path.join(dir, '../tweet_input/tweets_testmedian.txt')

filename_out1 = os.path.join(dir, '../tweet_output/mapped.txt')
filename_out2 = os.path.join(dir, '../tweet_output/ft2.txt')

# for feature 2, basically a histogram
histogram = [0] * (MAX_WORDS_IN_TWEET + 1)

# finds the median value in the histogram, the parameter is just to save some processing, a global variable could
# also have been used
def getMedian(totalElements):

    # integer division to find midpoint of histogram
    # if odd: [ ] [x] [ ]
    # if even, find the right point first: [ ] [ ] [x] [ ]
    midPoint = (totalElements // 2) + 1

    previousBin = 0
    currentBin = 0
    count = 0
    for i in range(MAX_WORDS_IN_TWEET + 1):
        if histogram[i] > 0:
            count += histogram[i]
            # print(count)
            currentBin = i
            if count >= midPoint:
                break
            else:
                previousBin = currentBin

    # if even
    if totalElements % 2 == 0:
        # if median is split between 2 bins
        if count - histogram[currentBin] == midPoint - 1:
            return (previousBin + currentBin)/2.0
        else:
            return currentBin
    # if odd
    else:
        return currentBin


# reads in the input text file and splits each line into words. Writes to file the key value pair for each word and
# also the median number of unique words using the getMedian() function
def mapper():

    # counter keeping track of the number of lines (or tweets) we've processed so far
    totalLines = 0

    # number of unique words for the current line being read
    uniqueWords = 0

    with open(filename_in, 'r') as fin, open(filename_out1, 'w') as fout1, open(filename_out2, 'w') as fout2:

        for line in fin:
            words = line.strip().split(' ')

            wordcount = Counter(words)

            for item in wordcount.items():
                # write key value pairs used later by the reducer
                fout1.write("{}\t{}\n".format(*item))
                # print("{}\t{}".format(*item))

            uniqueWords = len(wordcount)

            # update histogram
            totalLines += 1
            histogram[uniqueWords] += 1

            # for feature 2, write the current median to file
            # since the median is either a whole number or a number with a half, rounding 0.6666666 should never happen
            fout2.write("{}\n".format(format(getMedian(totalLines), '.2f')))
            # print(format(getMedian(totalLines), '.2f'))

mapper()