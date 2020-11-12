from benchmark import Algorithm
from typing import Any


class Automat(Algorithm):
    """
    FINITE DETERMENISTIC AUTOMAT

    Before processing a string, algorithm finds automat states.
    Each state - is a substring of entered template
    (starting from empty string, ending on template itself).
    After that, algorithm creates a table of states.
    It would be used to find the next state of automat,
     to which would go in each case.
    And, finally, the string is processed through automat.
    Each symbol leads to a new state without checking next symbols.

    Speed of automat build-up - O(k^2).
    Speed of check - O(n). n - length of string, k - length of substring
    """
    def run(self, text: Any, template: str) -> int:
        file_length = text.seek(0, 2)
        counter = 0
        size = len(template)
        alphabet_dict = {}
        alphabet_list = []
        for temp_index in range(size):
            alphabet_dict[template[temp_index]] = 0
            diffs = 0
            for alphabet_index in range(len(alphabet_list)):
                if template[temp_index] != alphabet_list[alphabet_index]:
                    diffs += 1
            if diffs == len(alphabet_list):
                alphabet_list.append(template[temp_index])
        matrix = self.generate_matrix(alphabet_dict, size, template)
        state_number = 0
        for index in range(file_length):
            text.seek(index)
            diffs = 0
            current = text.readline(1)
            while diffs < len(alphabet_list) and\
                    current != alphabet_list[diffs]:
                diffs += 1
            state_number = self.get_state_number(diffs, alphabet_list, matrix,
                                                 state_number)
            if state_number == size:
                counter += 1
        return counter

    @staticmethod
    def generate_matrix(alphabet, size, template):
        matrix = []
        for _ in range(size + 1):
            matrix.append({})
        for index in alphabet:
            matrix[0][index] = 0
        for number in range(size):
            prev = matrix[number][template[number]]
            matrix[number][template[number]] = number + 1
            for index in alphabet:
                matrix[number + 1][index] = matrix[prev][index]
        return matrix

    @staticmethod
    def get_state_number(diffs, alphabet, matrix, state_number):
        if diffs == len(alphabet):
            return 0
        else:
            return matrix[state_number][alphabet[diffs]]
