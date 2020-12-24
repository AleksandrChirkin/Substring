from io import StringIO
from pathlib import Path
import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from benchmark import ALGORITHMS # noqa


class AlgorithmsTest(unittest.TestCase):
    def test_for_string_ios(self) -> None:
        string_io = StringIO(1000 * 'A')
        string_fragments = [100 * 'A', 100 * 'A' + 'B', 'B' + 100 * 'A']
        for algorithm in ALGORITHMS:
            for fragment in string_fragments:
                runner = algorithm()
                result = [index for index in
                          runner.run(string_io, fragment, 10)]
                if fragment == 100 * 'A':
                    self.assertListEqual([i for i in range(10)], result)
                else:
                    self.assertEqual(0, len(result))

    def test_for_text_files(self) -> None:
        text = Path('samples/Voyna_i_mir.txt').open(encoding='1251')
        for algorithm in ALGORITHMS:
            runner = algorithm()
            result = [index for index in runner.run(text, 'князь', 10)]
            self.assertEqual(10, len(result))


if __name__ == '__main__':
    unittest.main()
