# Word PS: Test Utils
#
# Author: Lucas Nunes Sequeira <lucasnseq@gmail.com>
# URL: <https://github.com/lucasns97/word_ps>
# For license information, see LICENSE

from unittest import TestCase

from word_ps.utils import extract_ngrams

class TestUtils(TestCase):

    def setUp(self):
        """Unecessary"""
        pass

    def test_extract_ngrams(self):
        '''Tests extract ngrams method'''

        text = "Eu adoro batata frita, e você?"

        grams = extract_ngrams(text, 1, split_method='split')
        self.assertEqual(grams, ['Eu', 'adoro', 'batata', 'frita,', 'e', 'você?'])

        grams = extract_ngrams(text, 1, split_method='tokenize')
        self.assertEqual(grams, ['Eu', 'adoro', 'batata', 'frita', ',', 'e', 'você', '?'])

        grams = extract_ngrams(text, 2, split_method='split')
        self.assertEqual(grams, ['Eu adoro', 'adoro batata', 'batata frita,', 'frita, e', 'e você?'])

        grams = extract_ngrams(text, 2, split_method='tokenize')
        self.assertEqual(grams, ['Eu adoro', 'adoro batata', 'batata frita', 'frita ,', ', e', 'e você', 'você ?'])

        grams = extract_ngrams(text, 10, split_method='split')
        self.assertEqual(grams, [])

        grams = extract_ngrams(text, 10, split_method='tokenize')
        self.assertEqual(grams, [])