#!usr/bin/env python3
import argparse
import io
import os

from algorithms import ALGORITHMS
from reporting import Reporting


class AlgorithmRunner:
    def __init__(self):
        pass

    def run(self, arguments):
        try:
            if arguments.algorithm == 'report':
                if arguments.clear:
                    try:
                        os.remove('reporting/report.txt')
                    except OSError:
                        print('Report file does not exist!')
                    else:
                        print('Report file successfully deleted!')
                else:
                    report = Reporting()
                    result = report.run(arguments.key)
                    for item in result:
                        print(item)
            else:
                text = None
                if arguments.input_file is not None:
                    text = open(arguments.input_file, 'r',
                                encoding=arguments.encoding)
                elif arguments.stdin is not None:
                    text = io.StringIO(arguments.stdin)
                with text:
                    if arguments.algorithm == 'all':
                        for algorithm in ALGORITHMS:
                            self.launch_and_report(text, algorithm,
                                                   arguments.fragment)
                    else:
                        self.launch_and_report(text, arguments.algorithm,
                                               arguments.fragment)
        except AttributeError:
            print('Argument not entered!')
        except OSError:
            print('Entered file does not exist!')
        except TypeError:
            print('Invalid arguments!')

    @staticmethod
    def launch_and_report(text, algorithm, fragment):
        algorithm_runner = algorithm()
        result = algorithm_runner.run(text, fragment)
        fragments = ["Algorithm: " + algorithm.__name__,
                     "Current template: " + fragment,
                     "Fragments found: " + str(result),
                     "Time elapsed: " + str(algorithm_runner.time),
                     "Memory spent: " + str(algorithm_runner.memory),
                     120 * '-']
        result = '\n'.join(fragments) + '\n'
        print(result)


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
        group.add_argument('--input_file', '-f', default=None)
        group.add_argument('--stdin', '-s', default=None)
        _parser.add_argument('--encoding', '-e', default='utf-8')
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

    report_parser = subparsers.add_parser("report", help=Reporting.__doc__)
    report_parser.set_defaults(algorithm='report')
    report_group = report_parser.add_mutually_exclusive_group()
    report_group.add_argument('--key', metavar='k', help='Key')
    report_group.add_argument('--clear', action='store_true',
                              help='Deletes the report')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    runner = AlgorithmRunner()
    runner.run(args)
