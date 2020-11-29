from algos.global_align import *

class KBandAlign(GlobalAlign):


    def __init__(self, v_text, h_text, match=1, mismatch=-1, gap=-2, kvalue=1):

        self.kvalue = kvalue
        super().__init__(v_text, h_text, match, mismatch, gap)


    @timeit
    def calc_matrix(self):

        self.init_matrix()
        self.validate_sizes()

        for i, h in it.product(range(1, self.shape[0]), range(-self.kvalue, self.kvalue)):

            j = i + h
            if 1 <= j <= self.shape[0] - 1:

                neighbors = self.calc_neighbors(i, j)
                diag = neighbors[2]

                if self.inside_band(i - 1, j):
                    up = neighbors[0]
                    best_val = max(up, diag)
                    self.matrix[i, j] = max(up, diag)
                    self.arrows[i, j] = self.calc_arrow(
                        best_val, [up, Row.UP_AND_DIAG])

                if self.inside_band(i, j - 1):
                    left = neighbors[1]
                    best_val = max(left, diag)
                    self.matrix[i, j] = max(left, diag)
                    self.arrows[i, j] = self.calc_arrow(
                        best_val, [left, Row.LEFT_AND_DIAG])

        memit(self)
        return self.matrix


    def inside_band(self, row, column):
        return -self.kvalue <= row - column <= self.kvalue


    def validate_sizes(self):
        if len(self.v_text) != len(self.h_text):
            raise Exception("For this alignment, both sequences must be of the same size.")


    def calc_arrow(self, best_val, neighbors):
        if best_val == neighbors[0]:
            arrow = Row.UP if neighbors[1] == Row.UP_AND_DIAG else Row.LEFT
        else:
            arrow = Row.DIAG
        return arrow

