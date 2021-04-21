from typing import List


class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.rows = [[int(n) for n in row.split(" ")]
                     for row in matrix_string.split("\n")]
        self.columns = [list(elements) for elements in zip(*self.rows)]

    def row(self, index: int) -> List:
        return self.rows[index - 1]

    def column(self, index: int) -> List:
        return self.columns[index - 1]
