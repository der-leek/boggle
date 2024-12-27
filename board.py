from die import Die
from random import choice


class Board:
    def __init__(self, dimension: int, load_board: bool = False):
        self.BOARD_DIM = dimension

        if load_board:
            self.board = []
            self.load_board()
        else:
            self.board = [
                [choice(Die().die) for _ in range(self.BOARD_DIM)]
                for _ in range(self.BOARD_DIM)
            ]

    def __str__(self):
        header_footer = self._generate_header_footer()
        rows = [self._format_row(row) for row in self.board]
        board_string = header_footer + "\n".join(rows) + "\n" + header_footer
        return board_string

    def load_board(self):
        while True:
            row = input().split()

            if len(row) != self.BOARD_DIM:
                print(f"Each row must have {self.BOARD_DIM} letters. Try again")
                continue

            self.board.append(row)

            if len(self.board) == self.BOARD_DIM:
                break

    def get_letter(self, row: int, col: int) -> str:
        return self.board[row][col]

    def _generate_header_footer(self) -> str:
        return "-" * (self.BOARD_DIM * 3 + 2) + "\n"

    def _format_row(self, row) -> str:
        return "|" + "".join(f" {col} " for col in row) + "|"


if __name__ == "__main__":
    board = Board(5, True)
    print(board)
