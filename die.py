from random import choice


class Die:
    bag = (
        ("M", "O", "T", "T", "E", "T"),
        ("A", "E", "E", "M", "E", "E"),
        ("HE", "AN", "QU", "IN", "ER", "TH"),
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
        ("B", "X", "Z", "J", "K", "QU"),
        ("M", "A", "N", "G", "E", "N"),
        ("P", "C", "T", "I", "S", "E"),
        ("I", "I", "T", "L", "C", "E"),
        ("W", "U", "I", "L", "K", "QU"),
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
