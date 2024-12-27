import pickle


class Node:
    def __init__(self):
        self.children = dict()
        self.is_word = False

    def __eq__(self, other):
        assert isinstance(other, Node)
        return self.children == other.children and self.is_word == other.is_word

    def __str__(self):
        return f"is_word: {self.is_word}, children: {self.children}"


class Trie:
    def __init__(self):
        self.root = Node()

    def __eq__(self, other):
        assert isinstance(other, Trie)
        return self.root == other.root

    def __str__(self): ...

    def insert(self, word: str):
        if len(word) < 3:
            return

        current = self.root
        for letter in word:
            letter = letter.upper()
            if letter not in current.children:
                current.children[letter] = Node()
            current = current.children[letter]

        current.is_word = True

    def contains(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            letter = letter.upper()
            if letter not in current.children:
                return False
            current = current.children[letter]

        return True

    def is_word(self, word: str) -> bool:
        current = self.root
        for letter in word:
            letter = letter.upper()
            if letter not in current.children:
                return False
            current = current.children[letter]

        return current.is_word

    @staticmethod
    def save(trie, filename: str):
        with open(filename, "wb") as f:
            pickle.dump(trie, f)

    @staticmethod
    def load(filename: str) -> pickle:
        with open(filename, "rb") as f:
            return pickle.load(f, fix_imports=False)
