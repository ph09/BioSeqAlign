from algos.align import *
from timem import *

class SemiglobalLinear(Align):

    def __init__(self, v_text, h_text, match=1, mismatch=-1, gap=-2):

        super().__init__(v_text, h_text, match, mismatch, gap)
        self.calc_matrix()


    @timeit
    def calc_matrix(self):

        for i, j in it.product(range(1, len(self.v_text)), range(1, len(self.h_text))):
            neighbors = self.calc_neighbors(i, j)
            best_val = neighbors[np.argmax(neighbors)]
            self.matrix[i, j] = best_val
            self.arrows[i, j] = self.calc_arrow(best_val, neighbors)

        memit(self)
        return self.matrix


    def calc_neighbors(self, row, column):
        diag = self.v_text[row] == self.h_text[column]
        diag = (self.match if diag else self.mismatch)
        diag = self.matrix[row - 1, column - 1] + diag
        up = self.matrix[row - 1, column] + self.gap
        left = self.matrix[row, column - 1] + self.gap
        return [up, left, diag]


    def calc_score(self):

        i, j = self.calc_score_index(False)
        return self.matrix[i, j]


    def calc_score_index(self,isTraceback):

        return self.shape[0] - 1, self.shape[1] - 1


    def reconstruction(self):

        if self.aligned_strings is not None:
            return self.aligned_strings

        self.aligned_strings = self.traceback()
        return self.aligned_strings


    def traceback(self):

        v_align = ""
        h_align = ""
        self.matrixLineal = self.matrix
        h_text = self.h_text[0::]
        v_text = self.v_text[0::]
        i, j = self.calc_score_index(False)
        banderaR = False
        banderaC = False
        print(self.matrixLineal)
        while i > 0 or j > 0:

            neighbors = self.calc_neighbors(i, j)
            if banderaR:
                self.matrixLineal = np.delete(self.matrixLineal, i+1, 0)
                print('\n Delete Row')
                print(self.matrixLineal)
                banderaR = False

            if banderaC:
                self.matrixLineal = np.delete(self.matrixLineal, j+1, 1)
                print('\n Delete Column')
                print(self.matrixLineal)
                banderaC = False

            if i > 0 and j > 0 and  self.matrixLineal[i, j] == neighbors[2]:
                v_align = v_text[i] + v_align
                h_align = h_text[j] + h_align
                i -= 1
                j -= 1
                banderaR = True
                banderaC = True


            elif i > 0 and  self.matrixLineal[i, j] == neighbors[0]:
                v_align = v_text[i] + v_align
                h_align = "_" + h_align
                i -= 1
                banderaR = True

            else:
                v_align = "_" + v_align
                h_align = h_text[j] + h_align
                j -= 1
                banderaC = True

        return v_align, h_align
