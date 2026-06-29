class TrieNode:
    def __init__(self):
        self.is_leaf = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_leaf = True

    def search(self, word: str) -> bool:
        return self.search_from_node(0, word, self.root)

    def search_from_node(self, i, word, node):
        if i >= len(word):
            return node.is_leaf
        if word[i] == '.':
            for next_node in node.children.values():
                if self.search_from_node(i + 1, word, next_node):
                    return True
            return False
        elif word[i] in node.children:
            return self.search_from_node(i + 1, word, node.children[word[i]])
        return False
            
