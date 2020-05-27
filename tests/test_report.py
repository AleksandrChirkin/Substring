import io
import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))

try:
    from algorithms import ALGORITHMS
    from reporting import Reporting
except OSError:
    print("Без 6-14 строк ругается то компилятор, то PEP((")


class ReportTest(unittest.TestCase):
    def setUp(self):
        report = open('reporting/report.txt', 'w')
        report.close()
        text = io.StringIO(1000*'A')
        fragment = 100*'A'
        for algorithm in ALGORITHMS:
            runner = algorithm()
            runner.run(text, fragment)
        self.reporting = Reporting()

    def testZero(self):
        results = self.reporting.run('0')
        self.assertEqual(7, len(results))

    def testOneZero(self):
        sorted_results = self.reporting.run('10')
        self.assertEqual(7, len(sorted_results))
        previous = sorted_results[0]
        for item in sorted_results[1:]:
            self.assertLessEqual(previous['Time elapsed:'],
                                 item['Time elapsed:'])
            previous = item

    def testOneOne(self):
        sorted_algorithms = self.reporting.run('11')
        self.assertEqual(7, len(sorted_algorithms))
        previous = sorted_algorithms[0]
        for item in sorted_algorithms[1:]:
            self.assertLessEqual(previous[1], item[1])
            previous = item

    def testTwo(self):
        sorted_results = self.reporting.run('2')
        self.assertEqual(7, len(sorted_results))
        previous = sorted_results[0]
        for item in sorted_results[1:]:
            self.assertLessEqual(previous['Memory spent:'],
                                 item['Memory spent:'])
            previous = item

    def testIgnoreWrongKey(self):
        self.reporting.run('12')
        self.assertRaises(NameError)

    def testFailsWhenReportFileRemoved(self):
        os.remove('reporting/report.txt')
        self.reporting.run('0')
        self.assertRaises(OSError)


if __name__ == '__main__':
    unittest.main()
