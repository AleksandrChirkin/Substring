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


class ReportTest(unittest.TestCase):
    def setUp(self):
        report = open('reporting/report.txt', 'w')
        report.close()
        text = io.StringIO(1000*'A')
        fragment = 100*'A'
        runner = BruteForce(text, fragment, True)
        runner.run()
        runner = SimpleHash(text, fragment, True)
        runner.run()
        runner = QuadraticHash(text, fragment, True)
        runner.run()
        runner = RabinKarp(text, fragment, True)
        runner.run()
        runner = Automat(text, fragment, True)
        runner.run()
        runner = MorrisPratt(text, fragment, True)
        runner.run()
        self.reporting = Reporting(True)

    def testZero(self):
        sorted_results = self.reporting.run('10')
        self.assertEqual(6, len(sorted_results))
        previous = sorted_results[0]
        for item in sorted_results[1:]:
            self.assertLess(previous['Time elapsed:'], item['Time elapsed:'])
            previous = item

    def testOne(self):
        sorted_algorithms = self.reporting.run('11')
        self.assertEqual(6, len(sorted_algorithms))


if __name__ == '__main__':
    unittest.main()
