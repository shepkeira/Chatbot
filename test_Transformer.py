from unittest import TestCase
import Transformer


class TestTransformer(TestCase):
    def test_transformer_pronoun(self):
        transformer = Transformer.Transformer()
        #transformer.transformerPronoun(self, "I")
        test = transformer.transformerPronoun("I")
        self.assertEqual("You", test)
