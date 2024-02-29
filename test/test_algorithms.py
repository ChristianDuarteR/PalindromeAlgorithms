import unittest
from python import algorithms

words = ["radar", "level", "stats", "hello", "racecar", "python", "civic", "madam"]
expected = [True, True, True, False, True, False, True, True]


class AlgorithmsTests(unittest.TestCase):

    def test_comparative(self):
        for i in range(len(words)):
            word = words[i]
            exp = expected[i]
            answer = algorithms.directiveComparative(word)
            self.assertEquals(answer, exp)

    def test_reversive(self):
        for i in range(len(words)):
            word = words[i]
            exp = expected[i]
            answer = algorithms.reversiComparative(word)
            self.assertEquals(answer, exp)

    def test_recursive(self):
        for i in range(len(words)):
            word = words[i]
            exp = expected[i]
            answer = algorithms.recursiveApproach(word)
            self.assertEquals(answer, exp)


if __name__ == "__main__":
    unittest.main()
