import logging
from trie import Trie, Node
from board import Board
from time import perf_counter


class Solver:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        # filemode="w",
        # filename="solver.log",
    )

    def __init__(self, board: Board, words: set):
        self.words = words
        self.board = board
        self.dictionary: Trie = Trie.load("dictionary.trie")
        self.positions_searched = 0

    def solve_board(self, dimension: int):
        start = perf_counter()

        for i in range(dimension):
            for j in range(dimension):
                solver.find_words_from_position(i, j, "", [])

        finish = perf_counter()
        elapsed_time = round(finish - start, 3)
        self.log_results(elapsed_time)

    def find_words_from_position(self, row: int, col: int, word: str, path: set):
        self.positions_searched += 1

        if (
            self.out_of_bounds(row, col, self.board.BOARD_DIMENSION)
            or (row, col) in path
            or not self.dictionary.contains(word)
        ):
            return

        path.append((row, col))
        word += self.board.get_letter(row, col)

        if self.dictionary.is_word(word):
            self.words.add(word)

        for new_row, new_col in self.get_neighbors(row, col):
            self.find_words_from_position(new_row, new_col, word, path)

        path.remove((row, col))

    def get_neighbors(self, row: int, col: int):
        directions = [
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]
        for dr, dc in directions:
            yield row + dr, col + dc

    def out_of_bounds(self, row: int, col: int, dimension: int) -> bool:
        return (
            True
            if (row < 0 or col < 0 or row > dimension - 1 or col > dimension - 1)
            else False
        )

    def log_results(self, elapsed_time):
        logging.info(
            f"Searched {self.positions_searched} positions in {elapsed_time} seconds"
        )
        logging.info(f"Found {len(self.words)} solutions")

    def print_results(self):
        print()
        print(self.board)
        print(self.words)


if __name__ == "__main__":
    board = Board(5)
    solver = Solver(board, words=set())

    solver.solve_board(board.BOARD_DIMENSION)
    solver.print_results()
