#!usr/bin/env python3
import argparse
import os

from algorithms import Automat, BruteForce, MorrisPratt, QuadraticHash,\
                       RabinKarp, SimpleHash
from reporting import Reporting


class AlgorithmRunner:
    def __init__(self, arguments):
        self.arguments = arguments

    def run(self):
        if self.arguments.clear:
            os.remove('reporting/report.txt')
        if self.arguments.assist:
            self.help()
        if self.arguments.algorithm == 'report':
            report = Reporting()
            report.run()
        text = open('samples/Voyna_i_mir.txt', 'r', encoding='windows-1251')
        if self.arguments.algorithm == 'all':
            self.launch_all(text)
        else:
            self.launch(text, self.arguments.fragment)

    def help(self):
        if self.arguments.algorithm == 'all':
            print('Launches all algorithms')
        elif self.arguments.algorithm == 'auto':
            print(Automat.__doc__)
        elif self.arguments.algorithm == 'bf':
            print(BruteForce.__doc__)
        elif self.arguments.algorithm == 'mp':
            print(MorrisPratt.__doc__)
        elif self.arguments.algorithm == 'qh':
            print(QuadraticHash.__doc__)
        elif self.arguments.algorithm == 'report':
            print('Analyzes report')
        elif self.arguments.algorithm == 'rk':
            print(RabinKarp.__doc__)
        elif self.arguments.algorithm == 'sh':
            print(SimpleHash.__doc__)

    def launch_all(self, text):
        algorithms = ['bf', 'sh', 'qh', 'rk', 'auto', 'mp']
        for item in algorithms:
            self.launch(text, item)
            text.seek(0)

    def launch(self, text, current_algorithm):
        if current_algorithm == 'auto':
            auto = Automat(text, self.arguments.fragment)
            auto.run()
        elif current_algorithm == 'bf':
            auto = BruteForce(text, self.arguments.fragment)
            auto.run()
        elif current_algorithm == 'mp':
            auto = MorrisPratt(text, self.arguments.fragment)
            auto.run()
        elif current_algorithm == 'qh':
            auto = QuadraticHash(text, self.arguments.fragment)
            auto.run()
        elif current_algorithm == 'rk':
            auto = RabinKarp(text, self.arguments.fragment)
            auto.run()
        elif current_algorithm == 'sh':
            auto = SimpleHash(text, self.arguments.fragment)
            auto.run()


def parse_args():
    parser = argparse.ArgumentParser(description='Program manager')
    parser.add_argument('algorithm', metavar='A',
                        choices=['all', 'auto', 'bf', 'mp', 'qh',
                                 'report', 'rk', 'sh'],
                        help='Determines searching algorithms')
    arg_group = parser.add_mutually_exclusive_group()
    arg_group.add_argument('--fragment', metavar='F',
                           help='Determines wanted fragment')
    arg_group.add_argument('--assist', action='store_true',
                           help='Opens info about algorithm')
    parser.add_argument('--clear', action='store_true', help='Clears report')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    runner = AlgorithmRunner(args)
    runner.run()
