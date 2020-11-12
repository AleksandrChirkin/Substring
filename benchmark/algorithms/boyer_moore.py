from benchmark import Algorithm


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
    def run(self, text, template) -> int:
        file_length = text.seek(0, 2)
        counter = 0
        alphabet = []
        rightest = {}
        for j in range(len(template)):
            if template[j] not in alphabet:
                alphabet.append(template[j])
                rightest[template[j]] = j
            elif j > rightest[template[j]]:
                rightest[template[j]] = j
        i = len(template) - 1
        while i < file_length:
            text.seek(i)
            current = text.readline(1)
            if current not in alphabet:
                i += len(template)
            else:
                matches = 1
                steps = rightest[current]
                for j in range(1, steps+1):
                    text.seek(i-j)
                    if text.readline(1) != template[steps - j]:
                        break
                    matches += 1
                for j in range(1, len(template) - steps):
                    text.seek(i+j)
                    if text.readline(1) != template[steps + j]:
                        break
                    matches += 1
                if matches == len(template):
                    counter += 1
                i += len(template) - steps
        return counter
