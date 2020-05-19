from time import perf_counter
from algorithms import Algorithm


class MorrisPratt(Algorithm):
    """
    MORRIS-PRATT ALGORITHM

    It counts prefix function for fragment.
    After the launch of algorithm, it use this function to move forward on respective number of steps.

    Speed - O(k + n)
    """
    def run(self):
        begin_time = perf_counter()
        counter = 0
        m = len(self.template)
        pi = [0]
        k = 0
        for i in range(1, m):
            while k > 0 and self.template[k] != self.template[i]:
                k = pi[k-1]
            if self.template[k] == self.template[i]:
                k += 1
            pi.append(k)
        for line in self.text:
            i = 0
            while i < len(line):
                j = 0
                while (j < m and i + j < len(line) and
                       line[i + j] == self.template[j]):
                    j += 1
                if j == m:
                    counter += 1
                i += self.inc(j, pi)
        self.output("Morris-Pratt", counter, perf_counter()-begin_time)

    @staticmethod
    def inc(j, pi) -> int:
        if j != 0:
            return j-pi[j-1]
        else:
            return 1
