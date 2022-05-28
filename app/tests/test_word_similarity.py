# Word PS: Test Wird Similarity
#
# Author: Lucas Nunes Sequeira <lucasnseq@gmail.com>
# URL: <https://github.com/lucasns97/word_ps>
# For license information, see LICENSE

# LIBS
from unittest import TestCase
from src.base.calculator import Calculator

# TEST VARIABLES
TRG_1 = "Batata frita quente"
HYP_1 = "Batata frita"


class TestWordSimilarity(TestCase):

    def setUp(self):
        """Unecessary"""
        pass

    def get_calculator(self):
        """Returns calculator object"""
        return Calculator()

    def test_weighted_similarity(self):
        '''Tests weighted similarity method'''

        # Get calculator
        calculator = self.get_calculator()

        # Params
        trg = TRG_1
        hyp = HYP_1

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = calculator.weighted_similarity(trg, hyp, bidirectional, split_method)
                self.assertEqual(score > 0. and score < 1., True)
                score = calculator.weighted_similarity(hyp, trg, bidirectional, split_method)
                self.assertEqual(score > 0. and score < 1., True)

        # Params
        trg = HYP_1
        hyp = HYP_1

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = calculator.weighted_similarity(trg, hyp, bidirectional, split_method)
                self.assertEqual(score == 1.0, True)
                score = calculator.weighted_similarity(hyp, trg, bidirectional, split_method)
                self.assertEqual(score == 1.0, True)

        # Params
        trg = ""
        hyp = HYP_1

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = calculator.weighted_similarity(trg, hyp, bidirectional, split_method)
                self.assertEqual(score == 0, True)
                score = calculator.weighted_similarity(hyp, trg, bidirectional, split_method)
                self.assertEqual(score == 0, True)

    def test_ngrams_weighted_similarity(self):
        '''Tests ngrams weighted similarity method'''

        # Get calculator
        calculator = self.get_calculator()

        # Params
        trg = "Batata quente"
        hyp = HYP_1

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = calculator.ngrams_weighted_similarity(trg, hyp, bidirectional, split_method, 3)
                self.assertEqual(score > 0. and score < 1., True)
                score = calculator.ngrams_weighted_similarity(hyp, trg, bidirectional, split_method, 3)
                self.assertEqual(score > 0. and score < 1., True)

        # Params
        trg = HYP_1
        hyp = HYP_1

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = calculator.ngrams_weighted_similarity(trg, hyp, bidirectional, split_method, 3)
                self.assertEqual(score == 1.0, True)
                score = calculator.ngrams_weighted_similarity(hyp, trg, bidirectional, split_method, 3)
                self.assertEqual(score == 1.0, True)

        # Params
        trg = ""
        hyp = HYP_1

        for split_method in ['split', 'tokenize']:
            for bidirectional in [True, False]:
                score = calculator.ngrams_weighted_similarity(trg, hyp, bidirectional, split_method, 3)
                self.assertEqual(score == 0, True)
                score = calculator.ngrams_weighted_similarity(hyp, trg, bidirectional, split_method, 3)
                self.assertEqual(score == 0, True)