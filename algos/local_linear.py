from algos.semiglobal_linear import *

class LocalLinear(SemiglobalLinear):

    def __init__(self, v_text, h_text, match=1, mismatch=-1, gap=-2):
        super().__init__(v_text, h_text, match, mismatch, gap)
        self.calc_matrix()
        global matrixLineal
        self.matrixLineal = self.matrix

    def calc_score(self):

        i, j = self.calc_score_index(False)
        return self.matrix[i, j]

    def calc_neighbors(self,row, column):

        neighbors = super().calc_neighbors(row, column)
        neighbors.append(0)
        return neighbors


    def calc_score_index(self,isTraceback):
        maxval = i = j = 0
        for row in range(self.shape[0]):
            argmax = np.argmax(self.matrixLineal[0, :])
            maxtmp = self.matrixLineal[0, argmax]
            if isTraceback:
                print('Delete Row ')
                print(self.matrixLineal,'\n')
                self.matrixLineal = np.delete(self.matrixLineal, 0, 0)

            if maxtmp > maxval:
                maxval, j, i = maxtmp, argmax, row
        return i, j


    def traceback(self):

        v_align = ""
        h_align = ""
        h_text = self.h_text[0::]
        v_text = self.v_text[0::]
        i, j = self.calc_score_index(True)

        neighbors = self.calc_neighbors(i, j)
        argmax = np.argmax(neighbors)
        maxval = neighbors[argmax]

        while maxval > 0:

            if maxval == neighbors[2]:
                v_align = v_text[i] + v_align
                h_align = h_text[j] + h_align
                i -= 1
                j -= 1

            elif maxval == neighbors[1]:
                v_align = "_" + v_align
                h_align = h_text[j] + h_align
                j -= 1

            elif maxval == neighbors[0]:
                v_align = v_text[i] + v_align
                h_align = "_" + h_align
                i -= 1

            neighbors = self.calc_neighbors(i, j)
            argmax = np.argmax(neighbors)
            maxval = neighbors[argmax]

        return v_align, h_align

# ----------------------------------------------------------------------------------------------------------------------
