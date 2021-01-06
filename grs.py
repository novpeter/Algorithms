import sys

# Есть массив чисел длины N. Все числа - целые. Найти наибольшую возрастающую подпоследовательность
class GRS:
    def run(self):
        #sequence = [8, 1, 3, 4, 2, 5, 10, 322, 50, 100]
        sequence = [10, 2, 9, 3, 5, 4, 6, 8]
        print(self.find_longest_rising_sequence(sequence))

    @staticmethod
    def find_longest_rising_sequence(sequence):
        indexes = []
        lengths = []

        for i in range(0, len(sequence)):
            number = sequence[i]

            smaller_index = sys.maxsize
            smaller_index_length = -1

            for j in range(i, -1, -1):
                if sequence[j] < number and lengths[j] > smaller_index_length:
                    smaller_index = j
                    smaller_index_length = lengths[j]

            if smaller_index == sys.maxsize:
                lengths.append(1)
                indexes.append(0)
            else:
                lengths.append(lengths[smaller_index] + 1)
                indexes.append(smaller_index + 1)

        result_sequence = []

        max_length_index = lengths.index(max(lengths))

        result_sequence.append(sequence[max_length_index])

        next_element_index = indexes[max_length_index] - 1

        while next_element_index >= 0:
            result_sequence.append(sequence[next_element_index])
            next_element_index = indexes[next_element_index] - 1

        result_sequence.reverse()
        return result_sequence


grs = GRS()
grs.run()