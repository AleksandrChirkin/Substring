from benchmark import Algorithm
from typing import Any, List


class MorrisPratt(Algorithm):
    """
    MORRIS-PRATT ALGORITHM

    It counts prefix function for fragment.
    After the launch of algorithm,
     it use this function to move forward on respective number of steps.

    Speed - O(k + n), where k - length of substring and n - length of string
    """
    def run(self, text: Any, template: str) -> int:
        file_length = text.seek(0, 2)
        counter = 0
        temp_length = len(template)
        leap_list = [0]
        leap = 0
        for temp_index in range(1, temp_length):
            while leap > 0 and template[leap] != template[temp_index]:
                leap = leap_list[leap-1]
            if template[leap] == template[temp_index]:
                leap += 1
            leap_list.append(leap)
        file_index = 0
        while file_index < file_length:
            text.seek(file_index)
            current_shift = 0
            while current_shift < temp_length and\
                    file_index + current_shift < file_length and\
                    text.readline(1) == template[current_shift]:
                current_shift += 1
                text.seek(file_index+current_shift)
            if current_shift == temp_length:
                counter += 1
            file_index += self.get_increment(current_shift, leap_list)
        return counter

    @staticmethod
    def get_increment(shift: int, leap_list: List[int]) -> int:
        if shift != 0:
            return shift - leap_list[shift - 1]
        return 1
