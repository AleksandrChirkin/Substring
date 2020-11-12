from benchmark import Algorithm
from typing import Any


class BoyerMoore(Algorithm):
    """
    BOYER-MOORE ALGORITHM

    It finds all symbols in template and their rightest positions in it.
    Then, algorithm 'leaps' through the text:
    if current position does not contain symbol from template,
     algorithm jumps on the length of template;
    if it does, it firstly compares from the left,
     and then from the right from current position.

    Speed - O(n + k), where n - length of string and k - length of substring
    """
    def run(self, text: Any, template: str) -> int:
        file_length = text.seek(0, 2)
        counter = 0
        alphabet = []
        rightest = {}
        for temp_index in range(len(template)):
            if template[temp_index] not in alphabet:
                alphabet.append(template[temp_index])
                rightest[template[temp_index]] = temp_index
            elif temp_index > rightest[template[temp_index]]:
                rightest[template[temp_index]] = temp_index
        file_index = len(template) - 1
        while file_index < file_length:
            text.seek(file_index)
            current = text.readline(1)
            if current not in alphabet:
                file_index += len(template)
            else:
                matches = 1
                steps = rightest[current]
                for temp_index in range(1, steps+1):
                    text.seek(file_index-temp_index)
                    if text.readline(1) != template[steps - temp_index]:
                        break
                    matches += 1
                for temp_index in range(1, len(template) - steps):
                    text.seek(file_index+temp_index)
                    if text.readline(1) != template[steps + temp_index]:
                        break
                    matches += 1
                if matches == len(template):
                    counter += 1
                file_index += len(template) - steps
        return counter
