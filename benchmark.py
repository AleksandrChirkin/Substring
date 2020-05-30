#!usr/bin/env python3
import argparse
import io
from time import perf_counter

from algorithms import ALGORITHMS


class AlgorithmRunner:
    def __init__(self):
        pass

    def run(self, arguments):
        try:
            text = None
            if arguments.input_file is not None:
                text = open(arguments.input_file, 'r',
                            encoding=arguments.encoding)
            elif arguments.stdin is not None:
                text = io.StringIO(arguments.stdin)
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
        except TypeError:
            print('Invalid arguments!')

    def launch(self, algorithm, fragment, text, report_file):
        algorithm_runner = algorithm()
        start_time = perf_counter()
        result = algorithm_runner.run(text, fragment)
        time = perf_counter()-start_time
        results = (algorithm, fragment, text, result, time)
        self.report(results, report_file)

    @staticmethod
    def report(result, report_file):
        elements = ['Algorithm: '+result[0].__name__,
                    'Fragment: '+result[1],
                    'Text size: '+str(result[2].seek(0, 2)),
                    'Fragments found: '+str(result[3]),
                    'Time elapsed: '+str(result[4]), 120*'-']
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
        group.add_argument('--stdin', metavar='s', default=None,
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
    group.add_argument('--stdin', metavar='s', default=None,
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