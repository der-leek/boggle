from trie import Trie

trie = Trie()

import_filename = "dictionary.txt"
with open(import_filename, "r") as dictionary:
    for line in dictionary.readlines():
        trie.insert(line.strip())

export_filname = "dictionary.trie"
Trie.save(trie, export_filname)
