import io
import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from benchmark import Automat, BoyerMoore, BruteForce, MorrisPratt, \
    QuadraticHash, RabinKarp, SimpleHash, ALGORITHMS


class AlgorithmsTest(unittest.TestCase):
    def setUp(self):
        self.text = io.StringIO(1000 * 'A')
        self.fragments = [100*'A', 100*'A'+'B', 'B'+100*'A']

    def testBruteForce(self):
        for fragment in self.fragments:
            runner = BruteForce()
            result = runner.run(self.text, fragment)
            if fragment == 100 * 'A':
                self.assertEqual(901, result)
            else:
                self.assertEqual(0, result)

    def testSimpleHash(self):
        for fragment in self.fragments:
            runner = SimpleHash()
            result = runner.run(self.text, fragment)
            if fragment == 100 * 'A':
                self.assertEqual(901, result)
            else:
                self.assertEqual(0, result)

    def testQuadraticHash(self):
        for fragment in self.fragments:
            runner = QuadraticHash()
            result = runner.run(self.text, fragment)
            if fragment == 100 * 'A':
                self.assertEqual(901, result)
            else:
                self.assertEqual(0, result)

    def testRabinKarp(self):
        for fragment in self.fragments:
            runner = RabinKarp()
            result = runner.run(self.text, fragment)
            if fragment == 100 * 'A':
                self.assertEqual(901, result)
            else:
                self.assertEqual(0, result)

    def testAutomat(self):
        for fragment in self.fragments:
            runner = Automat()
            result = runner.run(self.text, fragment)
            if fragment == 100 * 'A':
                self.assertEqual(901, result)
            else:
                self.assertEqual(0, result)

    def testMorrisPratt(self):
        for fragment in self.fragments:
            runner = MorrisPratt()
            result = runner.run(self.text, fragment)
            if fragment == 100 * 'A':
                self.assertEqual(901, result)
            else:
                self.assertEqual(0, result)

    def testBoyerMoore(self):
        for fragment in self.fragments:
            runner = BoyerMoore()
            result = runner.run(self.text, fragment)
            if fragment == 100 * 'A':
                self.assertEqual(901, result)
            else:
                self.assertEqual(0, result)

    def testAll(self):
        for fragment in self.fragments:
            for algorithm in ALGORITHMS:
                runner = algorithm()
                result = runner.run(self.text, fragment)
                if fragment == 100 * 'A':
                    self.assertEqual(901, result)
                else:
                    self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
