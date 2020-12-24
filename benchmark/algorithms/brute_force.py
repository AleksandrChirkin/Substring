from benchmark import Algorithm
from io import StringIO, TextIOWrapper
from typing import Iterable, Union


class BruteForce(Algorithm):
    """
    BRUTE FORCE ALGORITHM

    Stops at the each symbol of string,
     and checks it for being the start of substring.
    Then it checks next symbols, until the irrelevant symbol found,
     or wanted substring found.

    Speed - O(nk), where n - length of string, k - length of substring"""
    def run(self, text: Union[StringIO, TextIOWrapper],
            template: str, number: int) -> Iterable[int]:
        file_length = text.seek(0, 2)
        counter = 0
        for file_index in range(file_length):
            text.seek(file_index)
            file_pointer = file_index
            matches = 0
            while file_pointer < file_length and\
                    template[matches] == text.readline(1):
                file_pointer += 1
                text.seek(file_pointer)
                matches += 1
                if matches == len(template):
                    break
            if matches == len(template):
                yield file_index
                counter += 1
                if counter == number:
                    return
