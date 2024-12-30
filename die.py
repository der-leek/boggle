from random import choice


class Die:
    bag = (
        ("HE", "AN", "QU", "IN", "ER", "TH"),
        ("W", "U", "I", "L", "K", "QU"),
        ("B", "X", "Z", "J", "K", "QU"),
        ("M", "O", "T", "T", "E", "T"),
        ("A", "E", "E", "M", "E", "E"),
        ("I", "P", "L", "E", "C", "T"),
        ("T", "E", "C", "S", "N", "C"),
        ("I", "S", "Y", "A", "F", "R"),
        ("O", "N", "T", "D", "D", "H"),
        ("S", "S", "E", "S", "N", "U"),
        ("O", "O", "T", "O", "U", "T"),
        ("D", "H", "O", "L", "R", "H"),
        ("D", "H", "N", "L", "O", "R"),
        ("S", "P", "F", "R", "I", "Y"),
        ("A", "E", "E", "A", "E", "E"),
        ("D", "N", "N", "A", "E", "N"),
        ("M", "A", "N", "G", "E", "N"),
        ("P", "C", "T", "I", "S", "E"),
        ("I", "I", "T", "L", "C", "E"),
        ("A", "I", "S", "A", "F", "R"),
        ("O", "H", "L", "D", "H", "N"),
        ("G", "E", "M", "E", "U", "A"),
        ("R", "V", "W", "G", "O", "R"),
        ("I", "E", "T", "I", "I", "T"),
        ("F", "A", "S", "R", "A", "A"),
    )

    def __init__(self):
        self.die = choice(self.bag)

    def __str__(self):
        return self.die
