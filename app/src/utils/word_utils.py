# Word PS: Utils
#
# Author: Lucas Nunes Sequeira <lucasnseq@gmail.com>
# URL: <https://github.com/lucasns97/word_ps>
# For license information, see LICENSE

from nltk import word_tokenize, ngrams
from typing import Union


def extract_ngrams(text: Union[str, list], max_size: int, split_method: str="split") -> list:
    '''Function to generate max_size-grams from a given text.

    Parameters:
        text (str) or (list): The text to be used to generate the grams or a list 
                              of tokens to be used to generate the grams.
        max_size (int): The max size of grams to be generated.
        assert split_method in ["split", "tokenize"]

    return (list): A list of grams of max_size, an empty list if max_size is greater then tokenized strings.
    '''

    assert split_method in ["split", "tokenize"]

    if isinstance(text, str):
        word_list = text.split() if split_method == "split" else word_tokenize(text)
    else:
        word_list = text

    n_grams = ngrams(word_list, max_size)

    return [' '.join(grams) for grams in n_grams]
