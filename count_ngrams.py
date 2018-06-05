# This was inspired by: https://www.ibm.com/developerworks/library/cc-patterns-artificial-intelligence-part2/index.html

import sys

from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer

TOKENIZER = RegexpTokenizer(r"[a-z_]+")

def count_ngrams(fp, frequencies, n, chunk_size=1024):
    """Read the text content of a file and keep a running count of how often
    each ngram word sequence  appears.

    Args:
        fp: file pointer to the corpus
        frequencies: dictionary of ngram to count
        n: number of words in each n-gram
        chunk_size: how many characters to read at a time
    """
    text = fp.read(chunk_size).lower()
    # replace end of sentence punctionation
    for symbol in ['.', '?', '!']:
        text = text.replace(symbol, ' _end_ ')

    while text:
        spans = TOKENIZER.span_tokenize(text)
        tokens = (text[begin:end] for (begin, end) in spans)
        for ngram in ngrams(tokens, n):
            ngram_str = ' '.join(list(ngram))

            count = frequencies.get(ngram_str, 0) + 1
            frequencies[ngram_str] = count

        text = fp.read(chunk_size).lower()

    return


if __name__ == '__main__':
    frequencies = {}
    ngram_size = int(sys.argv[1])
    count_ngrams(sys.stdin, frequencies, ngram_size)

    for ngram in sorted(frequencies, key=frequencies.get, reverse=True):
        print("{}: {}".format(ngram, frequencies[ngram]))
