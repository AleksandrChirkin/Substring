from io import StringIO
from pathlib import Path
import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from benchmark import ALGORITHMS # noqa


class AlgorithmsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.string_io = StringIO(1000 * 'A')
        self.string_fragments = [100 * 'A', 100 * 'A' + 'B', 'B' + 100 * 'A']
        self.text = Path('samples/Voyna_i_mir.txt').open(encoding='1251')
        self.text_fragments = ['князь', 'князь Андрей', 'князь Андрей Болконский']

    def test_for_string_ios(self) -> None:
        for algorithm in ALGORITHMS:
            for fragment in self.string_fragments:
                runner = algorithm()
                result = [index for index in
                          runner.run(self.string_io, fragment, 10)]
                if fragment == 100 * 'A':
                    self.assertListEqual([i for i in range(10)], result)
                else:
                    self.assertEqual(0, len(result))

    def test_for_text_files(self) -> None:
        for algorithm in ALGORITHMS:
            for fragment in self.text_fragments:
                runner = algorithm()
                result = [index for index in
                          runner.run(self.text, fragment, 10)]
                if fragment == 'князь Андрей Болконский':
                    self.assertEqual(4, len(result))
                else:
                    self.assertEqual(10, len(result))


if __name__ == '__main__':
    unittest.main()
