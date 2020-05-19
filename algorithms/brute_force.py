from time import perf_counter
from algorithms import Algorithm


class BruteForce(Algorithm):
    """
    BRUTE FORCE ALGORITHM

    Stops at the each symbol of string and checks it for being the start of substring.
    Then it checks next symbols, until the irrelevant symbol found, or wanted substring found.

    Speed - O(nk), where n - length of string, k - length of substring"""
    def run(self):
        begin_time = perf_counter()
        counter = 0
        for line in self.text:
            for j in range(len(line)):
                t = j
                if t > len(line):
                    break
                m = 0
                while (t < len(line) and
                       self.template[m] == line[t]):
                    t += 1
                    m += 1
                    if m == len(self.template):
                        break
                if m == len(self.template):
                    counter += 1
        self.output("Brute force", counter, perf_counter()-begin_time)
