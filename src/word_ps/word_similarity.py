# Word PS: Word Similarity
#
# Author: Lucas Nunes Sequeira <lucasnseq@gmail.com>
# URL: <https://github.com/lucasns97/word_ps>
# For license information, see LICENSE


from word_ps.utils import extract_ngrams


def _pairwise_sim(trg: str, hyp: str, max_steps: int=None) -> tuple:
    '''Calculate the pairwise similarity between two strings.

    Parameters:
        trg (str): String with the target word.
        hyp (str): String with the hypothesis word.
        max_steps (int): Maximum number of steps to be taken in the similarity.
    
    Returns:
        tuple: Pairwise score and string weight between the two strings.
    '''

    # Verify if both exists, returns score 0 and weight 0
    if not trg or not hyp: return 0.0, 0

    # String sizes
    trg_len, hyp_len = len(trg), len(hyp)

    # Max size, min size and difference
    max_size = max(trg_len, hyp_len)
    min_size = min(trg_len, hyp_len)
    dif_size = max_size-min_size

    # If strings are identical, returns score 1.0 and weight max_size
    if trg == hyp: return 1.0, max_size

    # Define maximizer and minimizer
    if trg_len > hyp_len:
        maximizer = trg
        minimizer = hyp

    elif trg_len <= hyp_len:
        maximizer = hyp
        minimizer = trg

    # Set max_steps
    if not max_steps:
        max_steps = min_size-1
    else:
        max_steps = min(max_steps, min_size-1)

    # Iterate by minimizer according max_steps
    # until find a match substring
    found_substring = False
    for step in range(0, max_steps):
        
        mw = minimizer[:-step] if step else minimizer
        
        if mw in maximizer:
            found_substring = True
            break   
    
    # If no match substring, return 0.0 and max_size
    if not found_substring:
        return 0.0, max_size

    score = 1-(step + dif_size)/max_size
    weight = max_size

    return score, weight
  
def _exc_pairwise_sim(trg: str, hyp: str, bidirectional: bool=False, weights: list=[2,1]) -> tuple:
    '''Execute the pairwise similarity between two strings.

    Parameters:
        trg (str): String with the target word.
        hyp (str): String with the hypothesis word.
        bidirectional (bool): If true, the similarity is calculated in both directions.
        weights (list): Weights to be applied to the similarity iff bidirectional == True.
    
    Returns:
        tuple: Pairwise score and string weight between the two strings.
    '''

    if bidirectional:
        # Execute the similarity in both directions
        sc1, wg = _pairwise_sim(trg, hyp)
        sc2, _  = _pairwise_sim(trg[::-1], hyp[::-1])

        # weighted average for the similarity
        sc = (weights[0]*sc1 + weights[1]*sc2)/sum(weights)
        
    else:
        # Execute the similarity
        sc, wg = _pairwise_sim(trg, hyp)

    return sc, wg

def weighted_similarity(trg: str, hyp: str, bidirectional: bool=False, split_method: str="split") -> float:
    '''Calculate the weighted similarity between two strings.

    Parameters:
        trg (str): String with the target word.
        hyp (str): String with the hypothesis word.
        bidirectional (bool): If true, the similarity is calculated in both directions.
        split_method (str): Method to be used to split the strings. Should be "split" or "tokenize".

    Returns:
        float: Weighted similarity between the two strings.
    '''

    assert split_method in ["split", "tokenize"]

    # Verify if exists or are identical
    if not trg or not hyp: return 0.0
    if trg == hyp: return 1.0

    # Split in words
    trg_words, hyp_words = extract_ngrams(trg, 1, split_method), extract_ngrams(hyp, 1, split_method)

    # Initialize weight and score
    score, weight  = 0, 0

    # String sizes
    trg_len, hyp_len = len(trg_words), len(hyp_words)

    # Extract grams according to the size of the smallest string
    if trg_len > hyp_len:
        maximizer_grams = extract_ngrams(trg_words, hyp_len)
        minimizer = hyp_words
        
    elif trg_len <= hyp_len:
        maximizer_grams = extract_ngrams(hyp_words, trg_len)
        minimizer = trg_words

    # Calculare pairwise similarity for each gram
    for maximizer_text in maximizer_grams:

        # Get maximizer words
        maximizer = extract_ngrams(maximizer_text, 1, split_method)

        # Calculate similarity for each word pair
        for min_w, max_w in zip(minimizer, maximizer):

            sc, wg = _exc_pairwise_sim(min_w, max_w, bidirectional)
            score  += sc*wg
            weight += wg
        
    return score/weight

def ngrams_weighted_similarity(trg: str, hyp: str, bidirectional: bool=False, split_method: str="split", ngrams: int = 3) -> float:
    '''Calculates the weighted similarity between the ngrams of target and hypotheis

        Parameters:
            trg (str): String with the target word.
            hyp (str): String with the hypothesis word.
            bidirectional (bool): If true, the similarity is calculated in both directions.
            split_method (str): Method to be used to split the strings. Should be "split" or "tokenize".
            ngrams (int): Number of ngrams (from 1 to ngrams) to be extracted from target and hypothesis

        Returns:
            float: Weighted similarity between the two strings considering number of ngrams (from 1 to ngrams, max_sentgrams).
    '''

    assert split_method in ["split", "tokenize"]

    # Iniailize score
    score = 0
    ngrams_loop_count = 0

    for i in range(1, ngrams+1):

        # Extract ngrams
        trg_ngrams = extract_ngrams(trg, i, split_method)
        hyp_ngrams = extract_ngrams(hyp, i, split_method)

        # Ngram score and loop count
        ngram_score = 0
        loop_count = 0

        # Calculate weigthed similarity for each ngram pair
        for trg_ngram, hyp_ngram in zip(trg_ngrams, hyp_ngrams):

            if not trg_ngram or not hyp_ngram: break

            # Accumulate score
            ngram_score = ngram_score + weighted_similarity(trg_ngram, hyp_ngram, bidirectional, split_method)
            loop_count += 1
        
        if loop_count > 0:
            ngrams_loop_count += 1
            ngram_score = ngram_score/loop_count

            # Add ngram score to the total score
            score = score + ngram_score
    
    # Normalize score
    score = score/ngrams_loop_count

    return score

