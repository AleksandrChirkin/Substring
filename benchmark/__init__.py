from benchmark.algorithms.algorithm import Algorithm
from benchmark.algorithms.automat import Automat
from benchmark.algorithms.boyer_moore import BoyerMoore
from benchmark.algorithms.brute_force import BruteForce
from benchmark.algorithms.hashes import SimpleHash, QuadraticHash, RabinKarp
from benchmark.algorithms.morris_pratt import MorrisPratt

ALGORITHMS = [Automat, BoyerMoore, BruteForce, MorrisPratt, QuadraticHash,
              RabinKarp, SimpleHash]
__all__ = ['Algorithm', 'Automat', 'BoyerMoore', 'BruteForce', 'MorrisPratt',
           'QuadraticHash', 'RabinKarp', 'SimpleHash', ALGORITHMS]
