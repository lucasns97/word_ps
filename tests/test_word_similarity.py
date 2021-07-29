# Word PS: Test Wird Similarity
#
# Author: Lucas Nunes Sequeira <lucasnseq@gmail.com>
# URL: <https://github.com/lucasns97/word_ps>
# For license information, see LICENSE

from unittest import TestCase

from word_ps.word_similarity import weighted_similarity, ngrams_weighted_similarity

class TestWordSimilarity(TestCase):

    def setUp(self):
        """Unecessary"""
        pass

    def test_weighted_similarity(self):
        '''Tests weighted similarity method'''

        # Params
        trg = "Batata frita quente"
        hyp = "Batata frita"

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = weighted_similarity(trg, hyp, bidirectional, split_method)
                self.assertEqual(score > 0. and score < 1., True)
                score = weighted_similarity(hyp, trg, bidirectional, split_method)
                self.assertEqual(score > 0. and score < 1., True)

        # Params
        trg = "Batata frita"
        hyp = "Batata frita"

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = weighted_similarity(trg, hyp, bidirectional, split_method)
                self.assertEqual(score == 1.0, True)
                score = weighted_similarity(hyp, trg, bidirectional, split_method)
                self.assertEqual(score == 1.0, True)

        # Params
        trg = ""
        hyp = "Batata frita"

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = weighted_similarity(trg, hyp, bidirectional, split_method)
                self.assertEqual(score == 0, True)
                score = weighted_similarity(hyp, trg, bidirectional, split_method)
                self.assertEqual(score == 0, True)

    def test_ngrams_weighted_similarity(self):
        '''Tests ngrams weighted similarity method'''

        # Params
        trg = "Batata frita quente"
        hyp = "Batata frita"

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = ngrams_weighted_similarity(trg, hyp, bidirectional, split_method, 3)
                self.assertEqual(score > 0. and score < 1., True)
                score = ngrams_weighted_similarity(hyp, trg, bidirectional, split_method, 3)
                self.assertEqual(score > 0. and score < 1., True)

        # Params
        trg = "Batata frita"
        hyp = "Batata frita"

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = ngrams_weighted_similarity(trg, hyp, bidirectional, split_method, 3)
                self.assertEqual(score == 1.0, True)
                score = ngrams_weighted_similarity(hyp, trg, bidirectional, split_method, 3)
                self.assertEqual(score == 1.0, True)

        # Params
        trg = ""
        hyp = "Batata frita"

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = ngrams_weighted_similarity(trg, hyp, bidirectional, split_method, 3)
                self.assertEqual(score == 0, True)
                score = ngrams_weighted_similarity(hyp, trg, bidirectional, split_method, 3)
                self.assertEqual(score == 0, True)