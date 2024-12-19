from die import Die
from random import choice


class Board:
    def __init__(self, dimension: int):
        self.BOARD_DIMENSION = dimension

        self.board = [
            [choice(Die().die) for _ in range(self.BOARD_DIMENSION)]
            for _ in range(self.BOARD_DIMENSION)
        ]

    def __str__(self):
        header_footer = self.generate_header_footer()
        rows = [self.format_row(row) for row in self.board]
        board_string = header_footer + "\n".join(rows) + "\n" + header_footer
        return board_string

    def generate_header_footer(self):
        return "-" * (self.BOARD_DIMENSION * 3 + 2) + "\n"

    def format_row(self, row):
        return "|" + "".join(f" {col} " for col in row) + "|"

    def get_letter(self, row: int, col: int) -> str:
        return self.board[row][col]


if __name__ == "__main__":
    board = Board()
    print(board)
