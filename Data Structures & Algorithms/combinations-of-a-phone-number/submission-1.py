class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        self.res = []

        def dfs(idx, ans):
            if idx >= len(digits):
                if ans:
                    self.res.append("".join(ans))
                return

            characters = d[digits[idx]]
            for c in characters:
                ans.append(c)
                dfs(idx + 1, ans)
                ans.pop()
            return

        dfs(0, [])
        return self.res