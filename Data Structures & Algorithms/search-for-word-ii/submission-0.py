class TrieNode:
    def __init__(self):
        self.word = ""
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word
        return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        self.res = []

        trie = Trie()
        for word in words:
            trie.insert(word)

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n_rows = len(board)
        n_cols = len(board[0])
        
        def dfs(r, c, node):
            if not 0 <= r < n_rows or not 0 <= c < n_cols or board[r][c] not in node.children:
                return
            
            cur_character = board[r][c]
            next_node = node.children[cur_character]
            if next_node.word:
                self.res.append(next_node.word)
                next_node.word = ""

            board[r][c] = "*"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, next_node)
            board[r][c] = cur_character
            return 

        for r in range(n_rows):
            for c in range(n_cols):
                dfs(r, c, trie.root)

        return self.res