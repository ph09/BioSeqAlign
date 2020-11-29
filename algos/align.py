import numpy as np
import itertools as it

class Row:

    UP = 0
    LEFT = 1
    DIAG = 2
    NONE = 3

    UP_AND_LEFT_AND_DIAG = 4
    UP_AND_LEFT = 5
    UP_AND_DIAG = 6
    LEFT_AND_DIAG = 7

    row_dic = {
        0: u"\u2191",
        1: u"\u2190",
        2: u"\u2196",
        3: " "
    }

    @staticmethod
    def get(row_type):
        string = Row.row_dic[row_type]
        return string


class Align(object):

    def __init__(self, v_text, h_text, match=1, mismatch=-1, gap=-2):

        self.v_text = "_" + v_text
        self.h_text = "_" + h_text

        self.match = match
        self.mismatch = mismatch
        self.gap = gap
        self.show_arrows = True

        self.shape = len(self.v_text), len(self.h_text)
        self.matrix = np.zeros(self.shape, dtype="int32")
        self.arrows = np.copy(self.matrix)
        self.arrows[:, :] = Row.NONE
        self.aligned_strings = None


    def calc_arrow(self, best_val, neighbors):

        left = neighbors[0]
        up = neighbors[1]
        diag = neighbors[2]
        arrow = np.argmax(neighbors)

        if best_val == up and best_val == left and best_val == diag:
            arrow = Row.UP_AND_LEFT_AND_DIAG
        elif best_val == up and best_val == left:
            arrow = Row.UP_AND_LEFT
        elif best_val == up and best_val == diag:
            arrow = Row.UP_AND_DIAG
        elif best_val == left and best_val == diag:
            arrow = Row.LEFT_AND_DIAG

        return arrow


    def get_string_without_arrows(self):
        matrix = self.matrix.astype(str)
        matrix = np.insert(matrix, [0], list(self.h_text), axis=0)
        matrix = np.insert(matrix, [0], np.matrix([[" "] + list(self.v_text)]).T, axis=1)
        return self.format_matrix_as_string(matrix)


    def get_string_with_arrows(self):

        matrix = np.copy(self.matrix)
        str_matrix = matrix.astype(str)
        arrows = np.copy(self.arrows)

        str_matrix = np.insert(str_matrix, range(1, str_matrix.shape[0]), " ", axis=0)
        str_matrix = np.insert(str_matrix, range(1, str_matrix.shape[1]), " ", axis=1)

        for i, j in it.product(range(matrix.shape[0]), range(matrix.shape[1])):

            if arrows[i, j] == Row.UP_AND_LEFT_AND_DIAG:
                str_matrix[i * 2 - 1, j * 2] = Row.get(Row.UP)
                str_matrix[i * 2, j * 2 - 1] = Row.get(Row.LEFT)
                str_matrix[i * 2 - 1, j * 2 - 1] = Row.get(Row.DIAG)

            elif arrows[i, j] == Row.UP_AND_LEFT:
                str_matrix[i * 2 - 1, j * 2] = Row.get(Row.UP)
                str_matrix[i * 2, j * 2 - 1] = Row.get(Row.LEFT)

            elif arrows[i, j] == Row.UP_AND_DIAG:
                str_matrix[i * 2 - 1, j * 2] = Row.get(Row.UP)
                str_matrix[i * 2 - 1, j * 2 - 1] = Row.get(Row.DIAG)

            elif arrows[i, j] == Row.UP_AND_DIAG:
                str_matrix[i * 2 - 1, j * 2] = Row.get(Row.UP)
                str_matrix[i * 2 - 1, j * 2 - 1] = Row.get(Row.DIAG)

            elif arrows[i, j] == Row.UP:
                str_matrix[i * 2 - 1, j * 2] = Row.get(Row.UP)

            elif arrows[i, j] == Row.LEFT:
                str_matrix[i * 2, j * 2 - 1] = Row.get(Row.LEFT)

            elif arrows[i, j] == Row.DIAG:
                str_matrix[i * 2 - 1, j * 2 - 1] = Row.get(Row.DIAG)

        h_text = np.insert(list(self.h_text), range(1, len(self.h_text)), [" "], axis=0)
        v_text = np.insert(list(self.v_text), range(len(self.v_text)), [" "], axis=0)
        str_matrix = np.insert(str_matrix, [0], h_text, axis=0)
        str_matrix = np.insert(str_matrix, [0], np.matrix(v_text).T, axis=1)
        return self.format_matrix_as_string(str_matrix)


    def format_matrix_as_string(self, matrix):

        string = ""
        for i in range(matrix.shape[0]):
            row = ' '.join('%04s' % matrix[i, j] for j in range(matrix.shape[1]))
            string += '[%s ]' % row + '\n'
        return string

    def __str__(self):
        if self.show_arrows:
            return self.get_string_with_arrows()
        return self.get_string_without_arrows()

