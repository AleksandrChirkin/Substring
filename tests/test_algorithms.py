import io
import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))

try:
    from algorithms import Automat, BruteForce, MorrisPratt, QuadraticHash,\
                           RabinKarp, SimpleHash
    from reporting import Reporting
except OSError:
    print("Без 6-14 строк ругается то компилятор, то PEP((")

ALGORITHMS = ['Brute force', 'Simple Hash', 'Quadratic Hash', 'Rabin-Karp',
              'Automat', 'Morris-Pratt']


class AlgorithmsTest(unittest.TestCase):
    def setUp(self):
        report = open('reporting/report.txt', 'w')
        report.close()
        self.text = io.StringIO(1000 * 'A')
        self.fragments = [100*'A', 100*'A'+'B', 'B'+100*'A']

    def testBruteForce(self):
        for fragment in self.fragments:
            runner = BruteForce(self.text, fragment, True)
            runner.run()
        reporting = Reporting(True)
        content = reporting.run('0')
        self.assertEqual(3, len(content))
        for item in content:
            self.assertEqual('Brute force', item['Algorithm:'])
            self.assertIn(item['Template:'], self.fragments)
            if item['Template:'] == 100 * 'A':
                self.assertEqual(901, item['Fragments found:'])
            else:
                self.assertEqual(0, item['Fragments found:'])

    def testSimpleHash(self):
        for fragment in self.fragments:
            runner = SimpleHash(self.text, fragment, True)
            runner.run()
        reporting = Reporting(True)
        content = reporting.run('0')
        self.assertEqual(3, len(content))
        for item in content:
            self.assertEqual('Simple Hash', item['Algorithm:'])
            self.assertIn(item['Template:'], self.fragments)
            if item['Template:'] == 100 * 'A':
                self.assertEqual(901, item['Fragments found:'])
            else:
                self.assertEqual(0, item['Fragments found:'])

    def testQuadraticHash(self):
        for fragment in self.fragments:
            runner = QuadraticHash(self.text, fragment, True)
            runner.run()
        reporting = Reporting(True)
        content = reporting.run('0')
        self.assertEqual(3, len(content))
        for item in content:
            self.assertEqual('Quadratic Hash', item['Algorithm:'])
            self.assertIn(item['Template:'], self.fragments)
            if item['Template:'] == 100 * 'A':
                self.assertEqual(901, item['Fragments found:'])
            else:
                self.assertEqual(0, item['Fragments found:'])

    def testRabinKarp(self):
        for fragment in self.fragments:
            runner = RabinKarp(self.text, fragment, True)
            runner.run()
        reporting = Reporting(True)
        content = reporting.run('0')
        self.assertEqual(3, len(content))
        for item in content:
            self.assertEqual('Rabin-Karp', item['Algorithm:'])
            self.assertIn(item['Template:'], self.fragments)
            if item['Template:'] == 100 * 'A':
                self.assertEqual(901, item['Fragments found:'])
            else:
                self.assertEqual(0, item['Fragments found:'])

    def testAutomat(self):
        for fragment in self.fragments:
            runner = Automat(self.text, fragment, True)
            runner.run()
        reporting = Reporting(True)
        content = reporting.run('0')
        self.assertEqual(3, len(content))
        for item in content:
            self.assertEqual('Automat', item['Algorithm:'])
            self.assertIn(item['Template:'], self.fragments)
            if item['Template:'] == 100 * 'A':
                self.assertEqual(901, item['Fragments found:'])
            else:
                self.assertEqual(0, item['Fragments found:'])

    def testMorrisPratt(self):
        for fragment in self.fragments:
            runner = MorrisPratt(self.text, fragment, True)
            runner.run()
        reporting = Reporting(True)
        content = reporting.run('0')
        self.assertEqual(3, len(content))
        for item in content:
            self.assertEqual('Morris-Pratt', item['Algorithm:'])
            self.assertIn(item['Template:'], self.fragments)
            if item['Template:'] == 100 * 'A':
                self.assertEqual(901, item['Fragments found:'])
            else:
                self.assertEqual(0, item['Fragments found:'])

    def testAll(self):
        for fragment in self.fragments:
            bf_runner = BruteForce(self.text, fragment, True)
            bf_runner.run()
            self.text.seek(0)
            sh_runner = SimpleHash(self.text, fragment, True)
            sh_runner.run()
            self.text.seek(0)
            qh_runner = QuadraticHash(self.text, fragment, True)
            qh_runner.run()
            self.text.seek(0)
            rk_runner = RabinKarp(self.text, fragment, True)
            rk_runner.run()
            self.text.seek(0)
            auto_runner = Automat(self.text, fragment, True)
            auto_runner.run()
            self.text.seek(0)
            mp_runner = MorrisPratt(self.text, fragment, True)
            mp_runner.run()
        reporting = Reporting(True)
        content = reporting.run('0')
        self.assertEqual(18, len(content))
        for item in content:
            self.assertIn(item['Algorithm:'], ALGORITHMS)
            self.assertIn(item['Template:'], self.fragments)
            if item['Template:'] == 100 * 'A':
                self.assertEqual(901, item['Fragments found:'])
            else:
                self.assertEqual(0, item['Fragments found:'])


if __name__ == '__main__':
    unittest.main()
