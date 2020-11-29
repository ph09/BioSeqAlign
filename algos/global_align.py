from algos.semiglobal_align import *

class GlobalAlign(SemiglobalAlign):

    def init_matrix(self):

        self.matrix[0, :] = np.arange(0, self.gap * len(self.h_text), self.gap)
        self.matrix[:, 0] = np.arange(0, self.gap * len(self.v_text), self.gap)

    def calc_matrix(self):

        self.arrows[:, 0] = Row.UP
        self.arrows[0, :] = Row.LEFT
        self.arrows[0, 0] = Row.NONE
        self.init_matrix()
        return super().calc_matrix()
