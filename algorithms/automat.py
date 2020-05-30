from algorithms import Algorithm


class Automat(Algorithm):
    """
    FINITE DETERMENISTIC AUTOMAT

    Before processing a string, algorithm finds automat states.
    Each state - is a substring of entered template
    (starting from empty string, ending on template itself).
    After that, algorithm creates a table of states.
    It would be used to find the next state of automat, to which would go in each case.
    And, finally, the string is processed through automat.
    Each symbol leads to a new state without checking next symbols.

    Speed of automat build-up - O(k).
    Speed of check - O(n). n - length of string, k - length of substring
    """
    def run(self, text, template) -> int:
        file_length = text.seek(0, 2)
        counter = 0
        size = len(template)
        alph = {}
        alphabet = []
        for i in range(size):
            alph[template[i]] = 0
            k = 0
            for j in range(len(alphabet)):
                if template[i] != alphabet[j]:
                    k += 1
            if k == len(alphabet):
                alphabet.append(template[i])
        matrix = self.generate_matrix(alph, size, template)
        state_number = 0
        for index in range(file_length):
            text.seek(index)
            k = 0
            current = text.readline(1)
            while k < len(alphabet) and current != alphabet[k]:
                k += 1
            state_number = self.get_state_number(k, alphabet, matrix,
                                                 state_number)
            if state_number == size:
                counter += 1
        return counter

    @staticmethod
    def generate_matrix(alph, size, template):
        matrix = []
        for _ in range(size + 1):
            matrix.append({})
        for i in alph:
            matrix[0][i] = 0
        for j in range(size):
            prev = matrix[j][template[j]]
            matrix[j][template[j]] = j + 1
            for i in alph:
                matrix[j + 1][i] = matrix[prev][i]
        return matrix

    @staticmethod
    def get_state_number(k, alphabet, matrix, state_number):
        if k == len(alphabet):
            return 0
        else:
            return matrix[state_number][alphabet[k]]
