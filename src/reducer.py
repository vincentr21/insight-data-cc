# Author: Vincent Ren
# Date: Fri, Jul 10, 15

import sys
import os

# relative paths are needed to reference files properly
dir = os.path.dirname(__file__)
filename_in = os.path.join(dir, '../tweet_output/mapped_sorted.txt')
filename_out1 = os.path.join(dir, '../tweet_output/ft1.txt')

# reads in the sorted list of key value pairs and sums the value for all pairs with the same key, writes result to
# file to complete feature 1
def reducer():

    with open(filename_in, 'r') as fin, open(filename_out1, 'w') as fout1:

        wordTotalCount = 0
        oldWord = None

        for line in fin:
            data = line.strip().split('\t')

            if len(data) != 2:
                continue

            thisWord, thisCount = data

            if oldWord and oldWord != thisWord:
                fout1.write("{}\t{}\n".format(oldWord, wordTotalCount))
                # print("{}\t{}".format(oldWord, wordTotalCount))
                wordTotalCount = 0

            oldWord = thisWord
            wordTotalCount += int(thisCount)

        if oldWord != None:
            fout1.write("{}\t{}\n".format(oldWord, wordTotalCount))
            # print("{}\t{}".format(oldWord, wordTotalCount))

reducer()