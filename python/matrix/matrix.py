class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(n) for n in row.split()]
                     for row in matrix_string.split("\n")]
        self.columns = [list(elements) for elements in zip(*self.rows)]

    def row(self, index):
        pass

    def column(self, index):
        pass
