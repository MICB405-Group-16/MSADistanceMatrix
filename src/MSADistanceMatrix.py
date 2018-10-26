import numpy as np
import sys

class Sequence:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

class MSADistanceMatrix:
    def __init__(self):
        pass

    def _strip_newline(self, string):
        if string[len(string) - 1] == "\n":
            return string[0:len(string) - 1]
        else:
            return string

    def _parse_file(self, file):
        sequences = []
        buf = [None, None]
        line = file.readline()
        while line:
            line = self._strip_newline(line)
            if(line[0] == '>'):
                if(buf[0] != None):
                    sequence = Sequence(buf[0], buf[1])
                    sequences.append(sequence)
                name = line[1:]
                buf[0] = name
                buf[1] = ''
            else:
                buf[1] += line
            line = file.readline()
        sequence = Sequence(buf[0], buf[1])
        sequences.append(sequence)
        return sequences

    def _get_header_row(self, names):
        string = 'Sequence'
        for sequence in names:
            string += "," + sequence.name
        string += '\n'
        return string

    def _parse_to_string(self, names, matrix):
        string = self._get_header_row(names)
        for i in range(len(names)):
            row = names[i].name
            for j in range(len(names)):
                row += ',' + str(int(matrix[i][j]))
            row += '\n'
            string += row
        return string

    def _count_num_differences(self, string1, string2):
        differences = 0
        length = min(len(string1), len(string2))
        for i in range(length):
            if string1[i] != string2[i]:
                differences += 1
        return differences + (max(len(string1), len(string2)) - length)

    def _generate_matrix(self, sequences):
        dim = len(sequences)
        matrix = np.zeros((dim, dim))
        for i in range(dim):
            row_sequence = sequences[i].sequence
            for j in range(len(sequences)):
                column_sequence = sequences[j].sequence
                matrix[i][j] = self._count_num_differences(row_sequence, column_sequence)
        return matrix

    def get_distance_matrix_string(self, path):
        file = open(path, "r")
        sequences = self._parse_file(file)
        matrix = self._generate_matrix(sequences)
        string = self._parse_to_string(sequences, matrix)
        return string

def main():
    path = sys.argv[1]
    matrix = MSADistanceMatrix()
    string = matrix.get_distance_matrix_string(path)
    print(string)

if __name__ == "__main__":
    main()