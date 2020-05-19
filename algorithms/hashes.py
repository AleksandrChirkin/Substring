from time import perf_counter
from algorithms import Algorithm


class SimpleHash(Algorithm):
    """
    SIMPLE HASH ALGORITHM

    It takes the length of wanted substring and counts codes of this number symbols,
     starting from the current position.
    After moving to the new position, code of previous symbol is removed
        and code of the next rightest position of new fragment.
    If hash of current fragment is equal to hash of template,
     then symbolwise comparision of fragment and templated launches.
    If, after that, algorithm found that fragment and template are not the same, it counts it as collision.

    Speed - O(n) in the best case, O(nk) in the worst case, where n - length of string and k - length of substring

    ATTENTION! Procedure of taking code of symbol can take long time!
    """
    def run(self):
        begin_time = perf_counter()
        counter = 0
        collisions = 0
        hash_sum_template = 0
        for j in range(len(self.template)):
            hash_sum_template += ord(self.template[j])
        for line in self.text:
            if len(line) < len(self.template):
                continue
            hash_sum_line = 0
            for k in range(len(self.template)):
                hash_sum_line += ord(line[k])
            for j in range(len(line)):
                if j+len(self.template)-1 >= len(line):
                    break
                t = j
                m = 0
                if j >= 1:
                    hash_sum_line = hash_sum_line + \
                                    ord(line[j+len(self.template)-1]) - \
                                    ord(line[j-1])
                if hash_sum_line == hash_sum_template:
                    while (t < len(line) and
                           line[t] == self.template[m]):
                        t += 1
                        m += 1
                        if m == len(self.template):
                            break
                    if m == len(self.template):
                        counter += 1
                    else:
                        collisions += 1
        self.output("Simple Hash", counter, perf_counter()-begin_time)


class QuadraticHash(Algorithm):
    """
    QUADRATIC HASH ALGORITHM

    It takes the length of wanted substring and counts quads of codes of this number symbols,
     starting from the current position.
    After moving to the new position, quad of code of previous symbol is removed
     and quad of code of the next rightest position of new fragment.
    If hash of current fragment is equal to hash of template,
     then symbolwise comparision of fragment and templated launches.
    If, after that, algorithm found that fragment and template are not the same, it counts it as collision.

    Speed - O(n) in the best case, O(nk) in the worst case, where n - length of string and k - length of substring

    ATTENTION! Procedure of taking code of symbol can take long time!
    """
    def run(self):
        begin_time = perf_counter()
        counter = 0
        collisions = 0
        hash_sum_template = 0
        for j in range(len(self.template)):
            hash_sum_template += ord(self.template[j])*ord(self.template[j])
        for line in self.text:
            if len(line) < len(self.template):
                continue
            hash_sum_line = 0
            for k in range(len(self.template)):
                hash_sum_line += ord(line[k]) * ord(line[k])
            for j in range(len(line)):
                if j+len(self.template)-1 >= len(line):
                    break
                t = j
                m = 0
                if j >= 1:
                    hash_sum_line = hash_sum_line + \
                                    ord(line[j+len(self.template)-1]) * \
                                    ord(line[j+len(self.template)-1]) - \
                                    ord(line[j-1]) * \
                                    ord(line[j-1])
                if hash_sum_line == hash_sum_template:
                    while (t < len(line) and
                           line[t] == self.template[m]):
                        t += 1
                        m += 1
                        if m == len(self.template):
                            break
                    if m == len(self.template):
                        counter += 1
                    else:
                        collisions += 1
        self.output("Quadratic Hash", counter, perf_counter()-begin_time)


class RabinKarp(Algorithm):
    """
    RABIN-KARP ALGORITHM

    It takes the length of wanted substring and counts codes of this number symbols,
     starting from the current position.
    Then, after adding a new symbol, the previous hash sum is doubled.
    After moving to the new position, code of previous symbol in degree of the length of substring is removed
     and code of the next rightest position of new fragment is added.
    If hash of current fragment is equal to hash of template,
     then symbolwise comparision of fragment and templated launches.
    If, after that, algorithm found that fragment and template are not the same, it counts it as collision.

    Speed - O(n) in the best case, O(nk) in the worst case, where n - length of string and k - length of substring

    ATTENTION! Procedure of taking code of symbol can take long time!
    """
    def run(self):
        begin_time = perf_counter()
        multiplier = 1
        for _ in range(len(self.template) - 1):
            multiplier *= 2
        counter = 0
        collisions = 0
        hash_sum_template = 0
        for j in range(len(self.template)):
            hash_sum_template = hash_sum_template * 2 + ord(self.template[j])
        for line in self.text:
            if len(line) < len(self.template):
                continue
            hash_sum_line = 0
            for k in range(len(self.template)):
                hash_sum_line = hash_sum_line * 2 + ord(line[k])
            for j in range(len(line)):
                if j+len(self.template)-1 >= len(line):
                    break
                t = j
                m = 0
                if j >= 1:
                    hash_sum_line = (hash_sum_line-ord(line[j-1]) *
                                     multiplier)*2 +\
                                     ord(line[j+len(self.template)-1])
                if hash_sum_line == hash_sum_template:
                    while (t < len(line) and
                           line[t] == self.template[m]):
                        t += 1
                        m += 1
                        if m == len(self.template):
                            break
                    if m == len(self.template):
                        counter += 1
                    else:
                        collisions += 1
        self.output("Rabin-Karp", counter, perf_counter()-begin_time)
