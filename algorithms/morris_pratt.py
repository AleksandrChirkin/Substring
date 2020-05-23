from algorithms import Algorithm


class MorrisPratt(Algorithm):
    """
    MORRIS-PRATT ALGORITHM

    It counts prefix function for fragment.
    After the launch of algorithm, it use this function to move forward on respective number of steps.

    Speed - O(k + n)
    """
    def run(self, text, template) -> int:
        file_length = text.seek(0, 2)
        counter = 0
        m = len(template)
        pi = [0]
        k = 0
        for i in range(1, m):
            while k > 0 and template[k] != template[i]:
                k = pi[k-1]
            if template[k] == template[i]:
                k += 1
            pi.append(k)
        i = 0
        while i < file_length:
            text.seek(i)
            j = 0
            while (j < m and i + j < file_length and
                    text.readline(1) == template[j]):
                j += 1
                text.seek(i+j)
            if j == m:
                counter += 1
            i += self.inc(j, pi)
        self.update_report('Morris-Pratt', counter, template)
        return counter

    @staticmethod
    def inc(j, pi) -> int:
        if j != 0:
            return j-pi[j-1]
        else:
            return 1
