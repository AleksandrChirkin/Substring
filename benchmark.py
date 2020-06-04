#!usr/bin/env python3
import argparse
import io
import sys
from time import perf_counter
from pympler import muppy, summary

from algorithms import ALGORITHMS


class AlgorithmRunner:
    def run(self, arguments):
        try:
            text = None
            if arguments.input_file is not None:
                text = open(arguments.input_file,
                            encoding=arguments.encoding)
            elif arguments.stdin:
                text = io.StringIO(sys.stdin.read())
            with text:
                if arguments.algorithm == 'all':
                    for algorithm in ALGORITHMS:
                        self.launch(algorithm, arguments.fragment, text,
                                    arguments.report_file)
                else:
                    self.launch(arguments.algorithm, arguments.fragment,
                                text, arguments.report_file)
        except AttributeError:
            print('Argument was not entered!')
        except OSError:
            print('File not found!')
        except TypeError:
            print('Invalid arguments!')

    def launch(self, algorithm, fragment, text, report_file):
        algorithm_runner = algorithm()
        memory = self.count_memory()
        start_time = perf_counter()
        result = algorithm_runner.run(text, fragment)
        time = perf_counter()-start_time
        memory = self.count_memory()-memory
        results = (algorithm, fragment, text, result, time, memory)
        self.report(results, report_file)

    @staticmethod
    def count_memory():
        all_objects = muppy.get_objects()
        sum1 = summary.summarize(all_objects)
        total_memory = 0
        for item in sum1:
            total_memory += item[2]
        return total_memory

    @staticmethod
    def report(result, report_file):
        elements = ['Algorithm: %s' % result[0].__name__,
                    'Fragment: %s' % result[1],
                    'Text size: %s' % result[2].seek(0, 2),
                    'Fragments found: %s' % result[3],
                    'Time elapsed (sec): %s' % result[4],
                    'Memory spent (KB): %s' % result[5], 120*'-']
        report = '\n'.join(elements)
        if report_file is not None:
            with open(report_file, 'a+') as stream:
                stream.write(report+'\n')
        else:
            print(report)


def parse_args():
    parser = argparse.ArgumentParser(description='Program manager')
    subparsers = parser.add_subparsers(title='algorithm')
    for algorithm in ALGORITHMS:
        _parser = subparsers.add_parser(algorithm.__name__.lower(),
                                        help=algorithm.__doc__)
        _parser.set_defaults(algorithm=algorithm)
        _parser.add_argument('fragment', metavar='F',
                             help='Determines wanted fragment')
        group = _parser.add_mutually_exclusive_group()
        group.add_argument('--input_file', metavar='f', default=None,
                           help='Input file')
        group.add_argument('--stdin', action='store_true',
                           help='Enter text in stdin')
        _parser.add_argument('--encoding', metavar='e', default='utf-8',
                             help='Determines encoding of text stream')
        _parser.add_argument('--report_file', metavar='r', default=None,
                             help='Determines report file')
    all_parser = subparsers.add_parser("all", help='Launches all algorithms')
    all_parser.set_defaults(algorithm='all')
    all_parser.add_argument('fragment', metavar='F',
                            help='Determines wanted fragment')
    group = all_parser.add_mutually_exclusive_group()
    group.add_argument('--input_file', metavar='f', default=None,
                       help='Input file')
    group.add_argument('--stdin', action='store_true',
                       help='Enter text in stdin')
    all_parser.add_argument('--encoding', metavar='e', default='utf-8',
                            help='Determines encoding of text stream')
    all_parser.add_argument('--report_file', metavar='r', default=None,
                            help='Determines report file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    runner = AlgorithmRunner()
    runner.run(args)
