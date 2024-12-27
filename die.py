from random import choice


class Die:
    bag = (
        ("T", "O", "E", "S", "S", "I"),
        ("A", "S", "P", "F", "F", "K"),
        ("N", "U", "I", "H", "M", "QU"),
        ("O", "B", "J", "O", "A", "B"),
        ("L", "N", "H", "N", "R", "Z"),
        ("A", "H", "S", "P", "C", "O"),
        ("R", "Y", "V", "D", "E", "L"),
        ("I", "O", "T", "M", "U", "C"),
        ("L", "R", "E", "I", "X", "D"),
        ("T", "E", "R", "W", "H", "V"),
        ("T", "S", "T", "I", "Y", "D"),
        ("W", "N", "G", "E", "E", "H"),
        ("E", "R", "T", "T", "Y", "L"),
        ("O", "W", "T", "O", "A", "T"),
        ("A", "E", "A", "N", "E", "G"),
        ("E", "I", "U", "N", "E", "S"),
    )

    def __init__(self):
        self.die = choice(self.bag)

    def __str__(self):
        return self.die
