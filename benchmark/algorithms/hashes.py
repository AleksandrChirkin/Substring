from benchmark import Algorithm
from dataclasses import dataclass
from io import StringIO, TextIOWrapper
from typing import Iterable, Union


@dataclass
class HashAlgorithmData:
    hash_sum_line: int
    hash_sum_template: int
    text: Union[StringIO, TextIOWrapper]
    file_index: int
    file_pointer: int
    file_length: int
    template: str
    matches: int


class HashAlgorithm:
    def __init__(self):
        self.counter = 0
        self.collisions = 0

    def update_counter_and_collisions(self, data: HashAlgorithmData) -> int:
        if data.hash_sum_line == data.hash_sum_template:
            data.text.seek(data.file_index)
            while data.file_pointer < data.file_length and \
                    data.text.readline(1) == data.template[data.matches]:
                data.file_pointer += 1
                data.text.seek(data.file_pointer)
                data.matches += 1
                if data.matches == len(data.template):
                    break
            if data.matches == len(data.template):
                self.counter += 1
                return data.file_index
            else:
                self.collisions += 1
        return -1


class SimpleHash(Algorithm, HashAlgorithm):
    """
    SIMPLE HASH ALGORITHM

    It takes the length of wanted substring
     and counts codes of this number symbols,
     starting from the current position.
    After moving to the new position, code of previous symbol is removed
        and code of the next rightest position of new fragment.
    If hash of current fragment is equal to hash of template,
     then symbolwise comparison of fragment and template launches.
    If, after that, algorithm found that fragment
     and template are not the same, it counts it as collision.

    Speed - O(n) in the best case, O(nk) in the worst case,
     where n - length of string and k - length of substring

    ATTENTION! Procedure of taking code of symbol can take long time!
    """

    def run(self, text: Union[StringIO, TextIOWrapper],
            template: str, number: int) -> Iterable[int]:
        file_length = text.seek(0, 2)
        hash_sum_template = 0
        for temp_index in range(len(template)):
            hash_sum_template += ord(template[temp_index])
        hash_sum_line = 0
        text.seek(0)
        for text_index in range(len(template)):
            hash_sum_line += ord(text.readline(1))
            text.seek(text_index + 1)
        for file_index in range(file_length):
            text.seek(file_index)
            file_pointer = file_index
            matches = 0
            if file_index >= 1 and file_index + len(template) - 1 < file_length:
                text.seek(file_index + len(template) - 1)
                new_order = ord(text.readline(1))
                text.seek(file_index - 1)
                old_order = ord(text.readline(1))
                hash_sum_line = hash_sum_line + new_order - old_order
            update_result = self.update_counter_and_collisions \
                (HashAlgorithmData(hash_sum_line, hash_sum_template, text,
                                   file_index, file_pointer, file_length,
                                   template, matches))
            if update_result != -1:
                yield update_result
                if self.counter == number:
                    return


class QuadraticHash(Algorithm, HashAlgorithm):
    """
    QUADRATIC HASH ALGORITHM

    It takes the length of wanted substring
     and counts quads of codes of this number symbols,
     starting from the current position.
    After moving to the new position,
     quad of code of previous symbol is removed
     and quad of code of the next rightest position of new fragment.
    If hash of current fragment is equal to hash of template,
     then symbolwise comparision of fragment and template launches.
    If, after that, algorithm found that fragment
     and template are not the same, it counts it as collision.

    Speed - O(n) in the best case, O(nk) in the worst case,
     where n - length of string and k - length of substring

    ATTENTION! Procedure of taking code of symbol can take long time!
    """

    def run(self, text: Union[StringIO, TextIOWrapper],
            template: str, number: int) -> Iterable[int]:
        file_length = text.seek(0, 2)
        hash_sum_template = 0
        for temp_index in range(len(template)):
            hash_sum_template += ord(template[temp_index]) * \
                                 ord(template[temp_index])
        hash_sum_line = 0
        text.seek(0)
        for text_index in range(len(template)):
            order = ord(text.readline(1))
            hash_sum_line += order * order
            text.seek(text_index + 1)
        for file_index in range(file_length):
            text.seek(file_index)
            file_pointer = file_index
            matches = 0
            if file_index >= 1 and \
                    file_index + len(template) - 1 < file_length:
                text.seek(file_index + len(template) - 1)
                new = ord(text.readline(1))
                text.seek(file_index - 1)
                old = ord(text.readline(1))
                hash_sum_line = hash_sum_line + new * new - old * old
            update_result = self.update_counter_and_collisions \
                (HashAlgorithmData(hash_sum_line, hash_sum_template, text,
                                   file_index, file_pointer, file_length,
                                   template, matches))
            if update_result != -1:
                yield update_result
                if self.counter == number:
                    return


class RabinKarp(Algorithm, HashAlgorithm):
    """
    RABIN-KARP ALGORITHM

    It takes the length of wanted substring
     and counts codes of this number symbols,
     starting from the current position.
    Then, after adding a new symbol, the previous hash sum is doubled.
    After moving to the new position,
     code of previous symbol in degree of the length of substring is removed
     and code of the next rightest position of new fragment is added.
    If hash of current fragment is equal to hash of template,
     then symbolwise comparision of fragment and template launches.
    If, after that, algorithm found that fragment
     and template are not the same, it counts it as collision.

    Speed - O(n) in the best case, O(nk) in the worst case,
     where n - length of string and k - length of substring

    ATTENTION! Procedure of taking code of symbol can take long time!
    """

    def run(self, text: Union[StringIO, TextIOWrapper],
            template: str, number: int) -> Iterable[int]:
        file_length = text.seek(0, 2)
        multiplier = 1
        for _ in range(len(template) - 1):
            multiplier *= 2
        hash_sum_template = 0
        for temp_index in range(len(template)):
            hash_sum_template = hash_sum_template * 2 + \
                                ord(template[temp_index])
        hash_sum_line = 0
        text.seek(0)
        for text_index in range(len(template)):
            hash_sum_line = hash_sum_line * 2 + ord(text.readline(1))
            text.seek(text_index + 1)
        for file_index in range(file_length):
            text.seek(file_index)
            file_pointer = file_index
            matches = 0
            if file_index >= 1 and \
                    file_index + len(template) - 1 < file_length:
                text.seek(file_index + len(template) - 1)
                new = ord(text.readline(1))
                text.seek(file_index - 1)
                old = ord(text.readline(1))
                hash_sum_line = (hash_sum_line - (old * multiplier)) * 2 + new
            update_result = self.update_counter_and_collisions \
                (HashAlgorithmData(hash_sum_line, hash_sum_template, text,
                                   file_index, file_pointer, file_length,
                                   template, matches))
            if update_result != -1:
                yield update_result
                if self.counter == number:
                    return
