class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        word_set = set(wordList)

        queue = deque([beginWord])
        res = 0
        while queue:
            res += 1
            n = len(queue)
            for _ in range(n):
                word = queue.popleft()
                print(word)
                for i in range(len(word)):
                    for c in 'qwertyuiopasdfghjklzxcvbnm':
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in word_set:
                            if new_word == endWord:
                                return res + 1
                            queue.append(new_word)
                            word_set.discard(new_word)
        print(res)         
        return 0