from algorithms import Algorithm


class SimpleHash(Algorithm):
    """
    SIMPLE HASH ALGORITHM

    It takes the length of wanted substring and counts codes of this number symbols,/n
     starting from the current position.
    After moving to the new position, code of previous symbol is removed
        and code of the next rightest position of new fragment.
    If hash of current fragment is equal to hash of template,
     then symbolwise comparision of fragment and templated launches.
    If, after that, algorithm found that fragment and template are not the same, it counts it as collision.

    Speed - O(n) in the best case, O(nk) in the worst case, where n - length of string and k - length of substring

    ATTENTION! Procedure of taking code of symbol can take long time!
    """
    def run(self, text, template) -> int:
        file_length = text.seek(0, 2)
        counter = 0
        collisions = 0
        hash_sum_template = 0
        for j in range(len(template)):
            hash_sum_template += ord(template[j])
        hash_sum_line = 0
        text.seek(0)
        for k in range(len(template)):
            hash_sum_line += ord(text.readline(1))
            text.seek(k+1)
        for i in range(file_length):
            text.seek(i)
            t = i
            m = 0
            if i >= 1 and i+len(template)-1 < file_length:
                text.seek(i+len(template)-1)
                new_order = ord(text.readline(1))
                text.seek(i-1)
                old_order = ord(text.readline(1))
                hash_sum_line = hash_sum_line+new_order-old_order
            if hash_sum_line == hash_sum_template:
                text.seek(i)
                while t < file_length and text.readline(1) == template[m]:
                    t += 1
                    text.seek(t)
                    m += 1
                    if m == len(template):
                        break
                if m == len(template):
                    counter += 1
                else:
                    collisions += 1
        self.update_report('Simple Hash', counter, template)
        return counter


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
    def run(self, text, template) -> int:
        file_length = text.seek(0, 2)
        counter = 0
        collisions = 0
        hash_sum_template = 0
        for j in range(len(template)):
            hash_sum_template += ord(template[j]) * ord(template[j])
        hash_sum_line = 0
        text.seek(0)
        for k in range(len(template)):
            order = ord(text.readline(1))
            hash_sum_line += order * order
            text.seek(k + 1)
        for i in range(file_length):
            text.seek(i)
            t = i
            m = 0
            if i >= 1 and i + len(template) - 1 < file_length:
                text.seek(i + len(template) - 1)
                new = ord(text.readline(1))
                text.seek(i - 1)
                old = ord(text.readline(1))
                hash_sum_line = hash_sum_line + new * new - old * old
            if hash_sum_line == hash_sum_template:
                text.seek(i)
                while t < file_length and text.readline(1) == template[m]:
                    t += 1
                    text.seek(t)
                    m += 1
                    if m == len(template):
                        break
                if m == len(template):
                    counter += 1
                else:
                    collisions += 1
        self.update_report('Quadratic Hash', counter, template)
        return counter


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
    def run(self, text, template) -> int:
        file_length = text.seek(0, 2)
        multiplier = 1
        for _ in range(len(template) - 1):
            multiplier *= 2
        counter = 0
        collisions = 0
        hash_sum_template = 0
        for j in range(len(template)):
            hash_sum_template = hash_sum_template * 2 + ord(template[j])
        hash_sum_line = 0
        text.seek(0)
        for k in range(len(template)):
            hash_sum_line = hash_sum_line * 2 + ord(text.readline(1))
            text.seek(k+1)
        for i in range(file_length):
            text.seek(i)
            t = i
            m = 0
            if i >= 1 and i + len(template) - 1 < file_length:
                text.seek(i+len(template)-1)
                new = ord(text.readline(1))
                text.seek(i-1)
                old = ord(text.readline(1))
                hash_sum_line = (hash_sum_line-(old*multiplier)) * 2 + new
            if hash_sum_line == hash_sum_template:
                text.seek(i)
                while t < file_length and text.readline(1) == template[m]:
                    t += 1
                    text.seek(t)
                    m += 1
                    if m == len(template):
                        break
                if m == len(template):
                    counter += 1
                else:
                    collisions += 1
        self.update_report('Rabin-Karp', counter, template)
        return counter
