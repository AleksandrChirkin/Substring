from algorithms.algorithm import Algorithm
from algorithms.automat import Automat
from algorithms.boyer_moore import BoyerMoore
from algorithms.brute_force import BruteForce
from algorithms.hashes import SimpleHash, QuadraticHash, RabinKarp
from algorithms.morris_pratt import MorrisPratt

ALGORITHMS = [Automat, BoyerMoore, BruteForce, MorrisPratt, QuadraticHash, RabinKarp, SimpleHash]
__all__ = ['Algorithm', 'Automat', 'BoyerMoore', 'BruteForce', 'MorrisPratt', 'QuadraticHash', 'RabinKarp',
           'SimpleHash', ALGORITHMS]
