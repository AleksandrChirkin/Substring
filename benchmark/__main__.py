#!usr/bin/env python3
from argparse import ArgumentParser, Namespace
from benchmark import Algorithm, ALGORITHMS
from dataclasses import dataclass
from io import StringIO, TextIOWrapper
from memory_profiler import memory_usage
from pathlib import Path
from time import perf_counter
from typing import List, Type, Union
import logging
import numpy
import sys
logging.basicConfig(format=u'%(message)s', level=logging.INFO,
                    stream=sys.stdout)


@dataclass
class BenchmarkResult:
    algorithm: type
    fragment: str
    text: Union[StringIO, TextIOWrapper]
    fragments_found: List[int]
    time_elapsed: float
    memory_spent: float


class AlgorithmRunner:
    def run(self, arguments: Namespace) -> None:
        try:
            text = None
            report_file = arguments.report_file
            number = int(arguments.number)
            if arguments.input_file is not None:
                text = Path(arguments.input_file)\
                    .open(encoding=arguments.encoding)
            elif arguments.stdin:
                text = StringIO(sys.stdin.read())
            with text:
                if arguments.algorithm == 'all':
                    for algorithm in ALGORITHMS:
                        self.launch(algorithm, arguments.fragment, text,
                                    number, report_file)
                else:
                    self.launch(arguments.algorithm, arguments.fragment,
                                text, number, report_file)
        except AttributeError:
            logging.error('Attribute not found!')
        except OSError:
            logging.error('File not found!')
        except TypeError:
            logging.error('Inappropriate argument type!')

    def launch(self, algorithm: Type[Algorithm], fragment: str,
               text: Union[StringIO, TextIOWrapper],
               number: int, report_file: str) -> None:
        memory = numpy.mean(memory_usage())
        time = perf_counter()
        alg_runner = algorithm()
        result = [index for index in alg_runner.run(text, fragment, number)]
        time = perf_counter()-time
        memory_expr = (algorithm.run, (alg_runner, fragment, text, number))
        memory = max(memory_usage(memory_expr))-memory
        results = BenchmarkResult(algorithm, fragment, text, result, time,
                                  memory)
        self.report(results, number, report_file)

    @staticmethod
    def report(result: BenchmarkResult, number: int,
               report_file: str) -> None:
        elements = [f'Algorithm: {result.algorithm.__name__}',
                    f'Fragment: {result.fragment}',
                    f'Text size: {result.text.seek(0, 2)}',
                    f'First {number} fragments begin there: '
                    f'{result.fragments_found}',
                    f'Time elapsed (sec): {result.time_elapsed}',
                    f'Memory spent (KB): {result.memory_spent}', 120*'-']
        report = '\n'.join(elements)
        if report_file is not None:
            with Path(report_file).open('a+') as report_stream:
                report_stream.write(report+'\n')
        else:
            logging.info(report)


def parse_args() -> Namespace:
    parser = ArgumentParser(description='Program manager')
    subparsers = parser.add_subparsers(title='algorithm')
    for algorithm in ALGORITHMS:
        _parser = subparsers.add_parser(algorithm.__name__.lower(),
                                        help=algorithm.__doc__)
        _parser.set_defaults(algorithm=algorithm)
        add_args_to_algorithm_subparser(_parser)
    all_parser = subparsers.add_parser("all", help='Launches all benchmark')
    all_parser.set_defaults(algorithm='all')
    add_args_to_algorithm_subparser(all_parser)
    return parser.parse_args()


def add_args_to_algorithm_subparser(parser: ArgumentParser) -> None:
    parser.add_argument('fragment', metavar='F',
                        help='Determines wanted fragment')
    parser.add_argument('number', metavar='N',
                        help='Determines number of fragments')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--input-file', metavar='f', default=None,
                       help='Input file')
    group.add_argument('--stdin', action='store_true',
                       help='Enter text in stdin')
    parser.add_argument('--encoding', metavar='e', default='utf-8',
                        help='Determines encoding of text stream')
    parser.add_argument('--report-file', metavar='r', default=None,
                        help='Determines report file')


if __name__ == '__main__':
    AlgorithmRunner().run(parse_args())
