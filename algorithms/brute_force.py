from algorithms import Algorithm


class BruteForce(Algorithm):
    """
    BRUTE FORCE ALGORITHM

    Stops at the each symbol of string,
     and checks it for being the start of substring.
    Then it checks next symbols, until the irrelevant symbol found,
     or wanted substring found.

    Speed - O(nk), where n - length of string, k - length of substring"""
    def run(self, text, template) -> int:
        file_length = text.seek(0, 2)
        counter = 0
        for j in range(file_length):
            text.seek(j)
            t = j
            m = 0
            while t < file_length and template[m] == text.readline(1):
                t += 1
                text.seek(t)
                m += 1
                if m == len(template):
                    break
            if m == len(template):
                counter += 1
        return counter
