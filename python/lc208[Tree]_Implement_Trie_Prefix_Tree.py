"""
2021.4
idea: recursive trie
  - list to store English low-case character.
  - set ending char for every word
"""

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._children = [None] * 26
        self._is_ending_char = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self
        for index, char in map(lambda x: (ord(x) - ord('a'), x),word):
            if not root._children[index]:
                root._children[index] = Trie()
            root = root._children[index]
        root._is_ending_char = True            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self
        for index in map(lambda x: ord(x) - ord('a'), word):
            if not root._children[index]:
                return False
            root = root._children[index]
        return root._is_ending_char

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self
        for index in map(lambda x: ord(x) - ord('a'), prefix):
            if not root._children[index]:
                return False
            else:
                root = root._children[index]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    print(trie.search('apple'))     # True
    print(trie.search('app'))       # False
    print(trie.startsWith('app'))   # True
    trie.insert('app')
    print(trie.search('app'))       # True
