# Written by Yuta

from collections import defaultdict

class Trie:
    def __init__(self):
        self.is_word = False
        self.extentions = defaultdict(Trie)

    def add_word(self, word):
        current_trie = self
        for c in word:
            current_trie = current_trie.extentions[c]
        current_trie.is_word = True

    def has_been_recorded(self, word):
        current_trie = self
        for c in word:
            if c not in current_trie.extentions:
                return False
            current_trie = current_trie.extentions[c]
        return current_trie.is_word



